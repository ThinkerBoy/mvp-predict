import math
import numpy as np
import pandas as pd
from scipy import stats
from mvp_model import zscore_model, stats_of_interest

global num_players
field_zscores = []
players = []

MVP_MODEL = zscore_model()
FILE_PATH = 'mvp2018'

def eucliddist(a,b):
    sum = 0.0
    for i in range(len(a)):
        sum += (a[i]-b[i])**2
    return math.sqrt(sum)

def produceZs():
    global num_players

    field_df = pd.read_csv('data/'+FILE_PATH+'.csv')
    num_players = len(field_df.index)

    for stat in stats_of_interest:
        stat_for_t20 = field_df[stat].tolist()
        math_ready = np.array(stat_for_t20)
        one_stat_zscores = np.array(stats.zscore(math_ready))
        field_zscores.append(one_stat_zscores)

        # print()
        # print(stat)
        # print(one_stat_zscores)

def compilePlayerZ():
    for i in range(num_players):
        player_stats = []
        for zscores in field_zscores:
            player_stats.append(zscores[i])
        players.append(player_stats)

def findMetricRanking():
    field_df = pd.read_csv('data/' + FILE_PATH + '.csv')
    distances = list(map(lambda player: [field_df.iloc[players.index(player)][field_df.columns.get_loc('Player')], eucliddist(player, MVP_MODEL)], players))
    return sorted(distances, key=lambda generated_metric: generated_metric[1])

def getName(index):
    field_df = pd.read_csv('data/' + FILE_PATH + '.csv')
    return field_df.iloc[index][field_df.columns.get_loc('Player')]

#test
print("mvp z-score model compared to top 20 PER players")
print(stats_of_interest)
print(MVP_MODEL)
print()

produceZs()
compilePlayerZ()
ranking = findMetricRanking()
for rank in ranking:
    print('{} {}: {}'.format(ranking.index(rank)+1, rank[0], rank[1]))
