import pandas as pd

df = pd.read_csv("data/capstone_accounting.csv")

print("Shape:", df.shape)
print(df.head())
df.info()
print(df.isnull().sum())
print(df.describe())
print("Exact duplicate rows:", df.duplicated().sum())