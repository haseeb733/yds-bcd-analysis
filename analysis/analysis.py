import pandas as pd

df = pd.read_csv("data/cleaned/cleaned.csv")

print("Total rows:", len(df))
print("Missing values:\n", df.isnull().sum())
