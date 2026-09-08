import pandas as pd

matches=pd.read_csv("matches.csv")
no_of_matches=matches["season"].value_counts()
print(no_of_matches)