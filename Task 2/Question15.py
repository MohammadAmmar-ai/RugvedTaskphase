import pandas as pd
matches=pd.read_csv("matches.csv")
deliveries=pd.read_csv("deliveries.csv")

total_runs=deliveries.groupby("match_id")["total_runs"].sum()
merged=matches.merge(total_runs,left_on="id",right_on="match_id")
print(merged.groupby("season")["total_runs"].sum())