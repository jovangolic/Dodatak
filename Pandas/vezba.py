import pandas as pd
import jinja2
df = pd.read_excel('SaleData.xlsx')
#print(df.head())
print(pd.pivot_table(df,index=['Region','SalesMan']))
