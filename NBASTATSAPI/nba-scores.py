from requests import get
from pprint import PrettyPrinter

BASE_URL = "https://data.nba.net"
ALL_JSON = "/prod/v1/today.json"

printer = PrettyPrinter()

def get_links():
    data = get(BASE_URL + ALL_JSON).json()
    return data['links']

def get_scoreboard():
    scoreboard_url = get_links()['currentScoreboard']
    games = get(BASE_URL + scoreboard_url).json()['games']

    for game in games:
        home_team = game['hTeam']
        away_team = game['vTeam']
        clock = game['clock']
        period = game['period']

        print(f"{home_team['triCode']} vs {away_team['triCode']}")
        print(f"{home_team['score']} - {away_team['score']}")
        print(f"{clock} - Q{period['current']}\n")

def get_stats():
    stats_url = get_links()['leagueTeamStatsLeaders']
    data = get(BASE_URL + stats_url).json()
    teams = data['league']['standard']['regularSeason']['teams']

    # Filter out placeholder teams
    teams = list(filter(lambda x: x['name'] != "Team", teams))

    # Sort by PPG rank (ascending)
    teams.sort(key=lambda x: int(x['ppg']['rank']))

    for i, team in enumerate(teams):
        name = team['name']
        nickname = team['nickname']
        ppg = team['ppg']['avg']
        print(f"{i + 1}. {name} - {nickname} - {ppg}")

    print("\nExample of keys in a team object:")
    printer.pprint(teams[0].keys())

# Call the function to test
get_stats()
