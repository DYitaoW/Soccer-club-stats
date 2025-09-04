import json
from bs4 import BeautifulSoup
from club import TeamStats
from player import PlayerStats
import os


def extract_team_and_players(html_file):
    with open(html_file, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")

    # Get JSON-LD script with structured team/player data
    script_tag = soup.find("script", {"type": "application/ld+json"})
    data = json.loads(script_tag.string)

    team_name = data["name"]
    coach_name = data["coach"]["name"]

    # Build players
    players = []
    for athlete in data.get("athlete", []):
        player_name = athlete["name"]
        players.append(PlayerStats(name=player_name, position="Unknown"))

    # Build the team object
    team = Team(
        name=team_name,
        coach=coach_name,
        players=players,
        manager=coach_name
    )

    return team


if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, "stat.html")
    team = extract_team_and_players(file_path)
    print(team)
    for p in team.players:
        print(" -", p)
