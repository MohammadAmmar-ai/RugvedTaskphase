import pandas as pd
matches=pd.read_csv("matches.csv")
by_runs=matches[matches["win_by_runs"] > 0]
print(by_runs["win_by_runs"].mean())
print(by_runs["win_by_runs"].median())
print(by_runs["win_by_runs"].std())
