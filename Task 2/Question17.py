import pandas as pd
deliveries=pd.read_csv("deliveries.csv")
exclude_kinds=["run out","retired hurt","obstructing the field"]
wickets_bowlers=deliveries[deliveries["dismissal_kind"].notna()& ~deliveries["dismissal_kind"].isin(exclude_kinds)]
wicket_per_bowler=wickets_bowlers.groupby("bowler").size().sort_values(ascending=False).head(10)
print(wicket_per_bowler)