import pandas as pd
matches=pd.read_csv("matches.csv")
by_runs=matches[matches["win_by_runs"]>0]
max_win=by_runs[by_runs["win_by_runs"]==by_runs["win_by_runs"].max()]
min_win=by_runs[by_runs["win_by_runs"]==by_runs["win_by_runs"].min()]

print("Highest win by runs:")
print(max_win[["win_by_runs","winner"]])
print("Lowest win by runs:")
print(min_win[["win_by_runs","winner"]])