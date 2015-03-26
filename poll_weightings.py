import pandas as pd
import math
from pandas import DataFrame

historical_polls = pd.read_csv('israeli_pre_election_polls.csv',delimiter=',')
results = pd.read_csv('israeli_results.csv',delimiter=',')
results = results.set_index('year')
historical_polls = historical_polls.sort('pollster')

#print historical_polls['days_before']

parties = ['Kadima', 'Likud', 'Yis Bet', 'Labor', 'Shas', 'UTJ', 'Hadash', 'Balad', 'Meretz', 'Yesh', 'Otzma', 'Am', 'Hatnuah', 'NU', 'Greens', 'Gil']

final_frame = pd.DataFrame(columns = historical_polls['pollster'].unique(),index=results.index)

for firm in historical_polls['pollster'].unique():
	sum = 0
	for party in parties:
		sum = sum + abs(results[party] - historical_polls[historical_polls['pollster']==firm].set_index('year')[party])*historical_polls[historical_polls['pollster']==firm].set_index('year')[party]/120
		days = historical_polls[historical_polls['pollster']==firm].set_index('year')['days_before']
	final_frame[firm] = sum

for firm in historical_polls['pollster'].unique():
	means = final_frame.mean(axis=1)
	final_frame[firm] = abs(final_frame[firm] - means)

total_error = pd.DataFrame(final_frame.mean(axis=0))
av_error = total_error.mean()[0]
print av_error
df = 1- (final_frame.mean(axis=0) - av_error)

print df

df.to_csv('poll_weights.csv',sep=',')



#print historical_polls[historical_polls['pollster']==firm].set_index('year')['days_before']