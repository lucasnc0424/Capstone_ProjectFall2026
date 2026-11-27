import pandas as pd

df = pd.read_csv("data/capstone_accounting.csv")

print("Shape:", df.shape)
print(df.head())
df.info()
print(df.isnull().sum())
print(df.describe())
print("Exact duplicate rows:", df.duplicated().sum())

# Step 2, cleaning column names
df.columns = df.columns.str.lower()
df.columns = df.columns.str.strip()
df.columns = df.columns.str.replace(" ", "_")

#removing duplicate rows
df = df.drop_duplicates()

#fill in missing department
df["department"] = df["department"].fillna("Unknown")

#invoice to date
df ["invoice_date"] = pd.to_datetime(df["invoice_date"], errors ="coerce")

#removing symbols from amounts and converting them into number values
df["amount"] = df["amount"].str.replace("$", "", regex=False)
df["amount"] = df["amount"].str.replace(",", "", regex=False)
df["amount"] = pd.to_numeric(df["amount"], errors="coerce")

#replace 9999 outlier thats skewing data
df["days_to_pay"] = df["days_to_pay"].replace(9999, None)
df["days_to_pay"] = pd.to_numeric(df["days_to_pay"], errors="coerce")

#results
print("Cleaned shape:", df.shape)
print(df.isnull().sum())
print(df[["invoice_date", "amount", "days_to_pay"]].describe())
print("Data types after cleaning:")
print(df.dtypes)