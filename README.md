Bank Marketing

Data Source: https://archive.ics.uci.edu/ml/datasets/Bank+Marketing

Problem Statement: Predict the clients that have a higher chance to subscribe for a term deposit.

Supervised learning techniques are used to understand the probability of subscription given a set of features about the clients.

Since it is costly to lose customer I focused on identifying the positive cases and compare the recall to find all the relevant cases in dataset.

Random Forest model is chosen for its performance in terms of recall and auc score.

I used bokeh and d3 to create a dashboard to identify the right clients for marketing calls. 
