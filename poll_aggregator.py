import datetime
import numpy as np
import pandas as pd

polls = pd.read_table('israeli_2015_polls.csv',delimiter=',')
polls['date'] = pd.to_datetime(polls['date'],dayfirst=True)

today = datetime.datetime(2015,3,12)

def exp_decay(days):
    days = getattr(days,"days",days)
    return .5 ** (days/30.)

def av_error(N):
    return 0.5*N**-.5

poll_ratings = pd.read_csv('poll_weights.csv',delimiter=',')
poll_ratings.columns = ['pollster','rating']

polls = polls.merge(poll_ratings, how="inner", on="pollster")

recency_weights = []
for i in range(0,len(polls['date'])):
    recency_weights.append(exp_decay(pd.to_datetime(today,dayfirst=True)-polls['date'][i]))

polls['recency_weights']=recency_weights

parties = ["L", "YB", "YA", "ZC", "BY", "S", "UTJ", "M", "A", "Y", "K"]

for party in parties:
	print party+": " + str(np.round(np.sum(polls['rating']*polls['recency_weights']*polls[party]/(polls['rating']*polls['recency_weights']).sum()),2))