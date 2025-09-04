import json
from bs4 import BeautifulSoup
from club import TeamStats
from player import PlayerStats
import re


def extract_team_and_players(html_file):
    with open(html_file, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")

    # Get JSON-LD script with structured team and player data

    script_tag = soup.find("script", {"type": "application/ld+json"})
    data = json.loads(script_tag.string)


    # variables for gathering and storing data for the club information

    team_name = data["name"]
    manager_name = data["coach"]["name"]

    # get the players in the club list

    players = []
    for athlete in data.get("athlete", []):
        player_name = athlete["name"]
        players.append(PlayerStats(name=player_name, position="Unknown"))

    record_p = soup.find("p", string=lambda t: t and "Record:" in t)
    if not record_p:
        record_p = soup.find("p", string=None)

    record_text = record_p.get_text(strip=True)


    parts = record_text.replace("Record:", "").split(",")
    record = parts[0].strip()
    points = int(parts[1].strip().split()[0])

    # more complicated parsing to store int values from strings

    match = re.search(r"\(([\d.]+)\s+per game\)", parts[1])
    if match:
        points_per_game = float(match.group(1))
    match = re.search(r"(\d+)", parts[2])
    position = 0
    if match:
        position = int(match.group(1))

    # parse home/ away records

    home_p = next((p for p in soup.find_all("p") if "Home Record:" in p.get_text()), None)
    home_text = home_p.get_text(strip=True)

    home_parts = home_text.replace("Home Record:", "").split("Away Record:")
    home_bits = home_parts[0].split(",")
    home_record = home_bits[0].strip()
    home_points = int(home_bits[1].strip().split()[0])

    away_bits = home_parts[1].split(",")
    away_record = away_bits[0].strip()
    away_points = int(away_bits[1].strip().split()[0])

    # parse goals and goal stats

    goals_p = next((p for p in soup.find_all("p") if "Goals" in p.get_text()), None)
    goals_text = goals_p.get_text(strip=True)

    g_parts = goals_text.split(",")
    goals = int(g_parts[0].split(":")[1].split("(")[0].strip())
    goals_allowed = int(g_parts[1].split(":")[1].split("(")[0].strip())
    goal_diff = int(g_parts[2].split(":")[1].strip())

    # xG parse

    xg_p = next((p for p in soup.find_all("p") if "xG:" in p.get_text()), None)
    xg_text = xg_p.get_text(strip=True)

    xg_parts = xg_text.split(",")
    xG = float(xg_parts[0].split(":")[1].strip())
    xGA = float(xg_parts[1].split(":")[1].strip())
    xG_difference = float(xg_parts[2].split(":")[1].strip())
    

    # build the club specific data

    team = TeamStats(
        name=team_name,
        players=players,
        manager=manager_name,
        record=record,
        points=points,
        points_per_game=points_per_game,
        position=position,
        home_record=home_record,
        home_points=home_points,
        away_record=away_record,
        away_points=away_points,
        goals = goals,
        goals_allowed= goals_allowed,
        goal_diff = goal_diff,
        xG = xG,
        xGA = xGA,
        xG_difference= xG_difference,

    )

    return team



def fill_goalkeeper_stats(team, html_file):
    with open(html_file, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")

    # Safe converters
    def get_int(td):
        if td and td.get_text(strip=True):
            try:
                return int(td.get_text(strip=True))
            except ValueError:
                return -1
        return -1

    def get_float(td):
        if td and td.get_text(strip=True):
            try:
                return float(td.get_text(strip=True))
            except ValueError:
                return -1.0
        return -1.0

    # Lookup by player name
    player_lookup = {player.name: player for player in team.players}

    # Stats mapping: HTML data-stat → player.stats key
    basic_mapping = {
        "gk_goals_against": "goals_allowed",
        "gk_goals_against_per90": "goals_per_90",
        "gk_saves": "saves",
        "gk_save_pct": "save_percent",
        "gk_clean_sheets": "clean_sheets",
        "gk_pens_saved": "pk_saved"
    }

    advanced_mapping = {
        "gk_psxg_net": "net_psxG",
        "gk_passes_pct_launched": "pass_percent_launched",
        "gk_passes": "passes",
        "gk_passes_length_avg": "avg_pass_length",
        "gk_pct_goal_kicks_launched": "goal_kick_percent_launched",
        "gk_goal_kick_length_avg": "avg_goal_kick_length",
        "gk_def_actions_outside_pen_area_per90": "def_actions_outside_box_per90",
        "gk_passes_completed_launched": "passes_completed",
        "gk_passes_launched": "passes_attempted",
        "gk_passes_pct_launched": "pass_completion_percent"
    }

    # --- Helper function to update only allowed stats ---
    def update_stats_from_row(player, row, mapping):
        for html_stat, stat_key in mapping.items():
            if stat_key not in player.stats:
                continue  # Only update keys that exist
            td = row.find("td", {"data-stat": html_stat})
            if isinstance(player.stats[stat_key], int):
                player.stats[stat_key] = get_int(td)
            else:
                player.stats[stat_key] = get_float(td)

    # --- Process basic table ---
    basic_table = soup.find("table", {"id": "stats_keeper_9"})
    if basic_table:
        for row in basic_table.tbody.find_all("tr"):
            name_cell = row.find("th", {"data-stat": "player"})
            if not name_cell:
                continue
            name = name_cell.get_text(strip=True)
            print(f"Found player in basic table: '{name}'", flush=True)

            if name not in player_lookup:
                print(f"Player '{name}' not found in team.players", flush=True)
                continue

            player = player_lookup[name]
            player.position = "GK"
            update_stats_from_row(player, row, basic_mapping)

    # --- Process advanced table ---
    adv_table = soup.find("table", {"id": "stats_keeper_adv_9"})
    if adv_table:
        for row in adv_table.tbody.find_all("tr"):
            name_cell = row.find("th", {"data-stat": "player"})
            if not name_cell:
                continue
            name = name_cell.get_text(strip=True)
            print(f"Found player in advanced table: '{name}'", flush=True)

            if name not in player_lookup:
                print(f"Player '{name}' not found in team.players", flush=True)
                continue

            player = player_lookup[name]
            update_stats_from_row(player, row, advanced_mapping)

