import pandas as pd
matches=pd.read_csv("matches.csv")

tie_games=matches[matches["result"]=="tie"]

print(tie_games[["team1","team2","winner"]].to_string())
