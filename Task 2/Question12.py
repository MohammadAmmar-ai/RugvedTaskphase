import pandas as pd
matches=pd.read_csv("matches.csv")
deliveries=pd.read_csv("deliveries.csv")

runs_per_match=deliveries.groupby("match_id")["total_runs"].sum()
merged=matches.merge(runs_per_match, left_on="id", right_on="match_id")
avg_by_venue = merged.groupby("venue")["total_runs"].mean()

print(avg_by_venue)