import pandas as pd
matches=pd.read_csv("matches.csv")
umpires_count=pd.concat([matches["umpire1"],matches["umpire2"]])
topumpires=umpires_count.value_counts()

print(topumpires.sort_values(ascending=False).head(10))
