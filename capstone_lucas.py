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


#Step 3, calculate collumns 
df["invoice_month"] = df["invoice_date"].dt.to_period("M")
df["is_over_30_days"] = df["days_to_pay"] > 30

#Total and average amount by department
dept_summary = df.groupby("department")["amount"].agg(["count", "sum", "mean"])
print("Summary by department:")
print(dept_summary)

# Total and average amount by expense category
category_summary = df.groupby("expense_category")["amount"].agg(["count", "sum", "mean"])
print("\nSummary by expense category:")
print(category_summary)

# Average days to pay 
terms_pay = df.groupby("payment_terms")["days_to_pay"].agg(["count", "mean", "median"])
print("\nDays to pay by payment terms:")
print(terms_pay)