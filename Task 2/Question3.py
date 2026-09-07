import pandas as pd

matches=pd.read_csv("matches.csv")

cities_count=matches["city"].value_counts()
print(cities_count)