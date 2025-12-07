import pandas as pd

file = "data/raw/dataset.csv"
df = pd.read_csv(file)

print(df.head())
print(df.info())
