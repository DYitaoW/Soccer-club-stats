from bs4 import BeautifulSoup
from club import TeamStats
from player import PlayerStats
from sortStats import extract_team_and_players
from getStats import fetch_and_clean_html
import os

url = "https://fbref.com/en/squads/cff3d9bb/Chelsea-Stats"

if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, "stat.html")
    fetch_and_clean_html(url, "stat.html")
    team = extract_team_and_players(file_path)
    print(team)

    #for p in team.players:
    #    print(" -", p)