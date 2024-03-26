import pandas as pd
import requests
import time

headers  = {
        'Connection': 'keep-alive',
        'Accept': 'application/json, text/plain, */*',
        'x-nba-stats-token': 'true',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
        'x-nba-stats-origin': 'stats',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Referer': 'https://stats.nba.com/',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9',
    }

from nba_api.stats.endpoints import commonteamroster
from nba_api.stats.static import teams

#Get NBA teams in 
nba_teams = teams.get_teams()

# Initialize an empty list to store team IDs and full names
team_info_list = []

# Iterate through each team and extract 'id' and 'full_name'
for team in nba_teams:
    team_info = {'id': team['id'], 'full_name': team['full_name']}
    team_info_list.append(team_info)

# Print the list of dictionaries
print(team_info_list)

#Iterate through team IDS
teams_roster=[]
for team_info in team_info_list:
    team_id = team_info['id']
    player_stats_data = commonteamroster.CommonTeamRoster(season='2014-15', team_id=team_id, headers=headers, timeout=100)   # <--- ADD YOUR season parameter!
    time.sleep(.600)
    df = player_stats_data.common_team_roster.get_data_frame()
    # print(team_id)
    # print(df)
    teams_roster.append(df)

print("Teams roster:")
print(teams_roster)
result_df = pd.concat(teams_roster, ignore_index=True)
print("Result DF:")
print(result_df)
result_df.to_csv('14-15PlayerInfo.csv', index = False)


# # get teams from the reg season 2021-22
# teamfinder = commonteamroster.CommonTeamRoster(season='2014-15',
#                                               team_id=0,
#                                               league_id_nullable='00')
# teams = teamfinder.get_data_frames()[0]
# print(teams)


# teams_roster=[]

# for team_id in team_ids:
#     player_stats_data = commonteamroster.CommonTeamRoster(season='2014-15', team_id=team_id, headers=headers, timeout=100)   # <--- ADD YOUR season parameter!
#     time.sleep(.600)
#     df = player_stats_data.common_team_roster.get_data_frame()
#     df['TeamID'] = team_id
#     print(team_id)
#     teams_roster.append(df)

# print(teams_roster[0])