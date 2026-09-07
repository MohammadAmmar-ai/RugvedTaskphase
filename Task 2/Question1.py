import pandas as pd
df=pd.read_csv("matches.csv")
matches2008=len(df[df["season"] == 2008])
print("No. of matches played in 2008 :", matches2008)