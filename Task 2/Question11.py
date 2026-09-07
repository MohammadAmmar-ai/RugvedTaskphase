import pandas as pd
deliveries=pd.read_csv("deliveries.csv")
six_count=deliveries[deliveries["batsman_runs"]==6]
print("Total no. of sixes",len(six_count))
print(six_count[['match_id', 'batsman', 'bowler', 'batsman_runs']])