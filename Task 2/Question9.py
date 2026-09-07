import pandas as pd
matches = pd.read_csv("matches.csv")
by_runs=matches[matches["win_by_runs"]>0]
max_win=by_runs[by_runs["win_by_runs"]==by_runs["win_by_runs"].max()]
min_win=by_runs[by_runs["win_by_runs"]==by_runs["win_by_runs"].min()]
print("Venue at which team won by max runs:")
print(max_win[["winner","venue","city"]].to_string())
print("Venue at which team won by min runs:")
print(min_win[["winner","venue","city"]].to_string())