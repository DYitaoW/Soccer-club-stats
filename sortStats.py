import json
from bs4 import BeautifulSoup
from club import TeamStats
from player import PlayerStats
import os
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
    print (xg_parts)
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


if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, "stat.html")
    team = extract_team_and_players(file_path)
    print(team)

    #for p in team.players:
    #    print(" -", p)
