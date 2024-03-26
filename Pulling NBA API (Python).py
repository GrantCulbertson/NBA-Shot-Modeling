#Pull that data in son
from nba_api.stats.static import players
from nba_api.stats.endpoints import shotchartdetail
import pandas as pd
import requests
import json

# players = []
# player_stats = {'name':None,'avg_dribbles':None,'avg_touch_time':None,'avg_shot_distance':None,'avg_defender_distance':None}

# teams ={'wizards':{
#                    'john wall':'202322'
#                    }}



# def find_stats(name,player_id):
#     #NBA Stats API using selected player ID
#     url = 'http://stats.nba.com/stats/playerdashptshotlog?'+ \
#     'DateFrom=&DateTo=&GameSegment=&LastNGames=0&LeagueID=00&' + \
#     'Location=&Month=0&OpponentTeamID=0&Outcome=&Period=0&' + \
#     'PlayerID='+player_id+'&Season=2014-15&SeasonSegment=&' + \
#     'SeasonType=Regular+Season&TeamID=0&VsConference=&VsDivision='
    
#     #Create Dict based on JSON response
#     response = requests.get(url)
#     shots = response.json()['resultSets'][0]['rowSet']
#     data = json.loads(response.text)
    
#     #Create df from data and find averages 
#     headers = data['resultSets'][0]['headers']
#     shot_data = data['resultSets'][0]['rowSet']
#     df = pd.DataFrame(shot_data,columns=headers) 
#     avg_def = df['CLOSE_DEF_DIST'].mean(axis=1)
#     avg_dribbles = df['DRIBBLES'].mean(axis=1)
#     avg_shot_distance = df['SHOT_DIST'].mean(axis=1)
#     avg_touch_time = df['TOUCH_TIME'].mean(axis=1)
     
#     #add Averages to dictionary then to list
#     player_stats['name'] = name
#     player_stats['avg_defender_distance']=avg_def
#     player_stats['avg_shot_distance'] = avg_shot_distance
#     player_stats['avg_touch_time'] = avg_touch_time
#     player_stats['avg_dribbles'] = avg_dribbles
#     players.append(player_stats.copy())


# for x in teams:
#     for y in teams[x]:
#         find_stats(y,teams[x][y])

# cols = ['name','avg_defender_distance','avg_dribbles','avg_shot_distance','avg_touch_time']
# df = pd.DataFrame(players,columns = cols)

# df.head()

# Storing Directory for All Players
player_dictionary = players.get_players()# Returning first 5 players in player_dictionary
player_dictionary[0:5]

# #Test with lebron
lebron = [player for player in player_dictionary if player['full_name'] == 'LeBron James']
lebron

# Pull in some shot log:
shotlog_lebron = shotchartdetail.ShotChartDetail(team_id = 0, player_id = '2544', 
context_measure_simple = 'FGA', 
season_type_all_star = ['Regular Season', 'Playoffs'],
start_period_nullable = "2015")
print(shotlog_lebron)
lebron_df = shotlog_lebron.get_data_frames()
print(lebron_df)
lebron_df.to_csv('LeBron_James.csv', index = False)


##ChatGPT code:
# from nba_api.stats.endpoints import shotchartdetail

# def get_shotchart_for_player(playerid, season):
#     all_shot_data = []
#     for season in seasons:
#         print(season)
#         shot_chart_detail = shotchartdetail.ShotChartDetail(player_id=playerid, season=season,team_id = 0)
#         shot_data = shot_chart_detail.get_data_frames()[0]
#         all_shot_data.append(shot_data)

#     return all_shot_data

# # Example player ID (Stephen Curry) and list of seasons
# player_id = 201939
# seasons = ['2016-17', '2017-18', '2018-19', '2019-20', '2020-21', '2021-22']

# # Get shotchartdetail for each season
# all_season_shot_data = get_shotchart_for_player(player_id, seasons)

# # Display shot data for each season
# for i, season_shot_data in enumerate(all_season_shot_data):
#     print(f"Season: {seasons[i]}")
#     print(season_shot_data)
#     print("---------------------------")





# import pandas as pd
# from nba_api.stats.endpoints import playergamelog
# from nba_api.stats.library.parameters import SeasonAll
# from nba_api.stats.static import players
# from nba_api.stats.endpoints import shotchartdetail


# LeKing_id = next((x for x in players.get_players() if x.get("full_name") == "LeBron James"), None).get("id")

# response = shotchartdetail.ShotChartDetail(
#     team_id=0,
#     player_id=LeKing_id,
#     season_nullable='2003-04',
#     context_measure_simple = 'FGA', #<-- Default is 'PTS' and will only return made shots, but we want all shot attempts
#     season_type_all_star='Regular Season'
# )

# results = content['resultSets'][0]
# headers = results['headers']
# rows = results['rowSet']
# df = pd.DataFrame(rows, columns=headers) #<-- add the columns parameter
# df.columns = headers






