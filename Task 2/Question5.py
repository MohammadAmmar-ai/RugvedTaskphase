import pandas as pd
matches=pd.read_csv("matches.csv")
result=matches["result"].value_counts()
print(result)