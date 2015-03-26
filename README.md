This very basic code computed poll weights and a weighted poll aggregator for the 2015 Israeli parliamentary elections. 

- israeli_pre_election_polls.csv contains final poll data for the last four parliamentary elections
- israeli_results.csv has the actual seat results for these elections
- poll_weightings.py turns this data into weights and outputs it to poll_weights.csv
- israeli_2015_polls.csv contains polls for the thirty days before the moratorium on polling
- poll_aggregator.py computes the poll aggregate, weighting for accuracy and time decay

The model is discussed in a series of posts on my blog beginning [here](http://www.clintonboys.com/israel-poll-aggregator-1/). 
