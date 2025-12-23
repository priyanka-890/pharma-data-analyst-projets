import pandas as pd

# df=pd.read_csv("pharma_sales.csv")
df=pd.read_csv("pharma_sales2.csv")
print("\nHEAD")

print(df.head())
print(df.describe())
print(df.info())
total_cols=['M01AB','M01AE','N02BA','N02BE','N05B','N05C','R03']

df['total_sales']=df[total_cols].sum(axis=1)
print("\ntotalsales")
print(df.head())


print(df[df['total_sales']>100])
