#pandas excel exercises at w3resource.com

# Write a Pandas program to import excel data (coalpublic2013.xlsx ) into a Pandas dataframe.
'''import pandas as pd
data = pd.read_excel('coalpublic2013.xls')
print(data) '''

#Write a Pandas program to get the data types of the given excel data (coalpublic2013.xlsx ) fields
'''import pandas as pd
df = pd.read_excel('coalpublic2013.xlsx')
print(df.dtypes)'''

#Write a Pandas program to read specific columns from a given excel file
'''import pandas as pd
cols = [1,2,4]
df = pd.read_excel('coalpublic2013.xlsx',usecols=cols)
#print(df.loc[:,['MSHA ID','Mine_Name','Labor_Hours']])
print(df)'''

#Write a Pandas program to insert a column in the sixth position of the said excel sheet and fill it with NaN values
'''import pandas as pd
import numpy as np
df = pd.read_excel('coalpublic2013.xlsx')
#print(df.head())
df.insert(5,'column1',np.nan)
print(df.head())'''

#Write a Pandas program to import some excel data (coalpublic2013.xlsx ) skipping first twenty rows into a Pandas dataframe. 
'''import pandas as pd
df = pd.read_excel('coalpublic2013.xlsx')
#df = pd.read_excel('coalpublic2013.xlsx',skiprows=20) #or use skiprows=some number
print(df.truncate(before=19))
#print(df)'''

# Write a Pandas program to add summation to a row of the given excel file
'''import pandas as pd
import numpy as np
df = pd.read_excel('coalpublic2013.xlsx')
sum_row=df[["Production", "Labor_Hours"]].sum()
df_sum=pd.DataFrame(data=sum_row).T
df_sum=df_sum.reindex(columns=df.columns)
print(df_sum)'''

#Write a Pandas program to import excel data (coalpublic2013.xlsx ) into a Pandas dataframe and display the last ten rows
'''import pandas as pd
df = pd.read_excel('coalpublic2013.xlsx')
print(df.tail(10))  '''

#Write a Pandas program to create a subtotal of "Labor Hours" against MSHA ID from the given excel data (coalpublic2013.xlsx )
'''import pandas as pd
df = pd.read_excel('coalpublic2013.xlsx')
#print(df.head())
rez = df[['MSHA ID','Labor_Hours']].groupby('MSHA ID').sum()
print(rez)'''

#Write a Pandas program to import excel data (coalpublic2013.xlsx ) into a dataframe and find a specific MSHA ID
'''import pandas as pd
df = pd.read_excel('coalpublic2013.xlsx')
#print(df.head())
filt = df['MSHA ID'] == 102901
print(df[filt])'''

#Write a Pandas program to import excel data (coalpublic2013.xlsx ) into a dataframe and find details where "Labor Hours" > 20000
'''import pandas as pd
df = pd.read_excel('coalpublic2013.xlsx')
#print(df.head())
filt = (df['Labor_Hours'] > 20000)
print(df[filt])'''

#Write a Pandas program to import excel data (coalpublic2013.xlsx ) into a dataframe and find details where "Mine Name" starts with "P". 
'''import pandas as pd
df = pd.read_excel('coalpublic2013.xlsx')
#print(df)
#filt = (df['Mine_Name'].str.startswith('P'))
#print(df[filt]) 
filt2 = df['Mine_Name'].apply(lambda x: x.startswith('P'))
print(df[filt2])
x = df['Mine_Name'].map(lambda x: x.startswith('P'))
print(df[x])'''

#Write a Pandas program to import excel data (coalpublic2013.xlsx ) into a dataframe and \
#find all records that include two specific MSHA ID
'''import pandas as pd
df = pd.read_excel('coalpublic2013.xlsx')
#print(df.head())
rez = df['MSHA ID'].isin([102976,103380])
print(df[rez])  '''

#Write a Pandas program to import excel data (coalpublic2013.xlsx ) into a Pandas dataframe and find a \
#list of specified customers by name
'''import pandas as pd
df = pd.read_excel('coalpublic2013.xlsx')
#print(df.head())
rez = df['Mine_Name'].isin(['Shoal Creek Mine','Piney Woods Preparation Plant'])
print(df[rez])
print(df.query('Mine_Name == ["Shoal Creek Mine","Piney Woods Preparation Plant"]'))'''

#Write a Pandas program to import excel data (employee.xlsx ) into a Pandas dataframe and find\
#a list of employees where hire_date> 01-01-07
'''import pandas as pd
df = pd.read_excel('employee.xlsx')
#print(df)
filt = (df['hire_date'] >= '01-01-2007')
print(df[filt]) '''

#Write a Pandas program to import excel data (employee.xlsx ) into a Pandas dataframe and to sort the records by the hire_date column.
'''import pandas as pd
df = pd.read_excel('employee.xlsx')
#print(df.head())
filt = df.sort_values(by='hire_date')
print(filt)'''

#Write a Pandas program to import excel data (employee.xlsx ) into a Pandas dataframe and find\
#a list of employees where hire_date between two specific month and year
'''import pandas as pd
df = pd.read_excel('employee.xlsx')
#print(df.head())
filt = ((df['hire_date'] >= 'Jan-2005')&(df['hire_date']<='Dec-2006'))
print(df[filt].head())'''

#Write a Pandas program to import excel data (employee.xlsx ) into a Pandas dataframe and find a list of employees of a specified year. 
'''import pandas as pd
df = pd.read_excel('employee.xlsx')
#print(df.head())
df2 = df.set_index(['hire_date'])
rez = df2.loc['2005']
print(rez.head())'''

#Write a Pandas program to import excel data (employee.xlsx ) into a Pandas dataframe and convert the data to use the hire_date as the index.
'''import pandas as pd
df = pd.read_excel('employee.xlsx')
#print(df.head())
rez = df.set_index(['hire_date'])
print(rez)  '''

#Write a Pandas program to import given excel data (employee.xlsx ) into a Pandas dataframe\
#and sort based on multiple given columns.
'''import pandas as pd
df = pd.read_excel('employee.xlsx')
#print(df.head())
rez = df.sort_values(by=['first_name','last_name'],ascending=[0,1])
print(rez)  '''

#Write a Pandas program to import sheet2 data from a given excel data (employee.xlsx ) into a Pandas dataframe
'''import pandas as pd
df = pd.read_excel('employee2.xlsx',sheet_name=1)
print(df)   '''

#Write a Pandas program to import three datasheets from a given excel data (emp2.xlsx ) and combine in to a single dataframe. 
'''import pandas as pd 
df1 = pd.read_excel('emp2.xlsx',sheet_name=0)
df2 = pd.read_excel('emp2.xlsx',sheet_name=1)
df3 = pd.read_excel('emp2.xlsx',sheet_name=2)
df = pd.concat([df1,df2,df3])
print(df)'''

# Write a Pandas program to import excel data (coalpublic2013.xlsx ) into a dataframe\
#and draw a bar plot where each bar will represent one of the top 10 production.
'''import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_excel('coalpublic2013.xlsx')
#print(df)   
prod_sorted = df.sort_values(by=['Production'],ascending=False)
prod_sorted['Production'].head(10).plot(kind='barh')
plt.show()'''

#Write a Pandas program to import excel data (coalpublic2013.xlsx ) into a dataframe and draw a bar plot comparing\
#year, MSHA ID, Production and Labor_hours of first ten records.
'''import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_excel('coalpublic2013.xlsx')
#print(df)   
df.iloc[:,[0,1,3,4]].head(10).plot(kind='bar',figsize=(14,3))
plt.show()'''

#Write a Pandas program to import three datasheets from a given excel data (employee.xlsx )\
#into a single dataframe and export the result into new Excel file.
'''import pandas as pd
df1 = pd.read_excel('emp2.xlsx',sheet_name=0)
df2 = pd.read_excel('emp2.xlsx',sheet_name=1)
df3 = pd.read_excel('emp2.xlsx',sheet_name=2)
df = pd.concat([df1,df2,df3])
#print(df)
df.to_excel('newEmp.xlsx',sheet_name='sheeter',index=False)'''


