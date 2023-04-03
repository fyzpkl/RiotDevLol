from riotwatcher import LolWatcher, ApiError
import datetime

# Initialize the LolWatcher object with your Riot API key
watcher = LolWatcher('RGAPI-05e60726-58f3-49e9-995d-f834d9faec7c')

# Retrieve the summoner information based on their summoner name and region
region = 'tr1'
summoner_name = 'V_bu8eYFjOpo-V1bz5qdmK9ULHC2zn1oNrvqXnwIABbyNjLvAvvJ_3KNdA'
try:
    summoner = watcher.summoner.by_id(region, summoner_name)
    print(summoner)
except ApiError as err:
    if err.response.status_code == 404:
        print('Summoner not found')
    else:
        raise

# Retrieve the summoner's league information
try:
    league_entries = watcher.league.by_summoner(region, summoner['id'])
    print(league_entries)
except ApiError as err:
    if err.response.status_code == 404:
        print('League not found')
    else:
        raise
timestamp = summoner['revisionDate'] // 1000
updated_datetime = datetime.datetime.fromtimestamp(timestamp)
# Print out the summoner's information
print(f"Summoner name: {summoner['name']}")
print(f"Summoner level: {summoner['summonerLevel']}")
print(f"Profile icon ID: {summoner['profileIconId']}")
print(f"Summoner information last updated: {updated_datetime}")
for entry in league_entries:
    if entry['queueType'] == 'RANKED_SOLO_5x5':
        print(f"Rank: {entry['tier']} {entry['rank']}")
        print(f"League points: {entry['leaguePoints']}")
