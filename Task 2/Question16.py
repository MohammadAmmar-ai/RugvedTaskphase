import pandas as pd
matches=pd.read_csv("matches.csv")
deliveries=pd.read_csv("deliveries.csv")

runs_batsman=deliveries.groupby("batsman")["batsman_runs"].sum()
most_runs=runs_batsman.sort_values(ascending=False).head(10)
print(most_runs)
