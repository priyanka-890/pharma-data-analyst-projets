import pandas as pd

df=pd.read_csv('pharma_sales.csv')

print(df.head())
# print(df.describe())
# print(df.info())

# drug_cols=['M01AB','M01AE','N02BA','N02BE','N05B','N05C','R03','R06']
           
# df['total_sales']=df[drug_cols].sum(axis=1)

# print(df[df['total_sales']>80])
# df.to_csv('day3_python.csv',index=False)
