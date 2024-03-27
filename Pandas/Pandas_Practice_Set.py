#pandas practice set exercises at w3resource.com
#use these 'https://raw.githubusercontent.com/mwaskom/seaborn-data/master/diamonds.csv'
#'http://bit.ly/uforeports'

#Write a Pandas program to read a csv file from a specified source and print the first 5 rows.
'''import pandas as pd
pd.set_option('display.max_rows',50)
pd.set_option('display.max_columns',50)
df = pd.read_csv('diamonds.csv')
print(df.head(5))'''

#Write a Pandas program to read a dataset from diamonds DataFrame and modify the default columns\
#values and print the first 6 rows
'''import pandas as pd
pd.set_option('display.max_rows',50)
pd.set_option('display.max_columns',50)
df = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/diamonds.csv')
#print(df.head())
cols = ['carat','cut','x','y','z']
print(df[cols].head(6))
rez = df[['carat','cut','x','y','z']]
print(rez.head(6))'''

#Write a Pandas program to select a series from diamonds DataFrame. Print the content of the series
'''import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/diamonds.csv')
#print(df.head())
s = pd.Series(df['carat'])
print(s)'''

#Write a Pandas program to create a new 'Quality -color' Series (use bracket notation to define the Series name)\
#of the diamonds DataFrame
'''import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/diamonds.csv')
#print(df.head())
df['Quality-color'] = df['cut']+','+df['color']
print(df.head())'''

#Write a Pandas program to find the number of rows and columns and data type of each column of diamonds Dataframe
'''import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/diamonds.csv')
#print(df.head())
print('number of rows and columns')
print(df.shape)
print('data type of each column:')
print(df.dtypes)'''

#Write a Pandas program to summarize only 'object' columns of the diamonds Dataframe
'''import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/diamonds.csv')
#print(df.head())
print('summarize of "object" columns')
rez = df.describe(include=[object])
print(rez)'''

# Write a Pandas program to rename two of the columns of the diamonds Dataframe.
'''import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/diamonds.csv')
#print(df.head())
rez = df.rename(columns={'color':'diamond_color','clarity':'diamond_clarity'})
#print(rez.head())
df.rename(columns={'color':'diamond_color','clarity':'diamond_clarity'},inplace=True)
print(df.head())'''

#Write a Pandas program to rename all the columns of the diamonds Dataframe
'''import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/diamonds.csv')
#print(df.head())
#df.rename(columns={'carat':'new_carat','cut':'new_cut','color':'new_color','clarity':'new_clarity',\
    #'depth':'new_depth','table':'new_table','price':'new_price','x':'new_x','y':'new_y','z':'new_z'},inplace=True)
#print(df.head()) 
diamonds_cols = ['new_carat', 'new_cut', 'new_color', 'new_clarity', 'new_depth', 'new_table', 'new_price', 'new_x', 'new_y', 'new_z']
df.columns = diamonds_cols
print(df.head())'''

#Write a Pandas program to remove the second column of the diamonds Dataframe.
'''import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/diamonds.csv')
#print(df.head())
print('remove the second column of the dataframe')
df.drop(columns='cut',axis=1,inplace=True)
print(df.head())'''

#Write a Pandas program to remove multiple columns at once of the diamonds Dataframe
'''import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/diamonds.csv')
#print(df.head())
print('remove multiple columns')
df.drop(columns=['carat','color','y'],axis=1,inplace=True)
print(df.head())'''

#Write a Pandas program to remove multiple rows at once (axis=0 refers to rows) from diamonds dataframe
'''import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/diamonds.csv')
#print(df.head())
print('remove multiple rows')
df.drop(df.index[[2,4,5]],axis=0,inplace=True)
#df.drop([2,4,5],axis=0,inplace=True)
print(df.head())'''

#Write a Pandas program to sort the 'cut' Series in ascending order (returns a Series) of diamonds Dataframe.
'''import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/diamonds.csv')
#print(df.head())
print("cut Series in ascending order")
s = pd.Series(df['cut'].sort_values(ascending=True))
print(s)
#rez = df['cut'].sort_values(ascending=True)
#print(rez)'''

#Write a Pandas program to sort the 'price' Series in descending order (returns a Series) of diamonds Dataframe
'''import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/diamonds.csv')
#print(df.head())
print('price Series in descending order')
#s = pd.Series(df['price'].sort_values(ascending=False))
#print(s)
rez = df['price'].sort_values(ascending=False)
print(rez)'''

#Write a Pandas program to sort the entire diamonds DataFrame by the 'carat' Series in ascending and descending order
'''import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/diamonds.csv')
#print(df.head())
print('sort by carat in ascending order')
rez1 = df.sort_values(by='carat',ascending=True)
#print(rez1.head())
print('sort by carat in descending order')
rez2 = df.sort_values(by='carat',ascending=False)
print(rez2.head())'''

#Write a Pandas program to filter the DataFrame rows to only show carat weight at least 0.3.
'''import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/diamonds.csv')
#print(df.head())
lst = []
for row in df['carat']:
    if row>0.3:
        lst.append(True)
    else:
        lst.append(False)
print(lst[:20]) '''

#Write a Pandas program to convert a python list to pandas series
'''import pandas as pd
lst = [1,3,5,7,9,11]
print('convert the list to a Series')
s = pd.Series(data=lst)
print(s)'''

#Write a Pandas program to find the details of the diamonds where length>5, width>5 and depth>5.
'''import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/diamonds.csv')
#print(df.head())
print('diamonds where length>5,width>5 and depth>5')
filt = (df['x']>5)&(df['y']>5)&(df['z']>5)
print(df[filt].head())'''

#Write a Pandas program to find the diamonds that are either Premium or Ideal
'''import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/diamonds.csv')
#print(df.head())
print('diamonds that are either premium or ideal')
filt = (df['cut']=='Premium')|(df['cut']=='Ideal')
print(df[filt].head())'''

#Write a Pandas program to find the diamonds that are with a Fair or Good or Premium
'''import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/diamonds.csv')
#print(df.head())
print('diamonds that are with a Fair or Good or Premium')
filt = (df['cut']=='Fair')|(df['cut']=='Ideal')|(df['cut']=='Premium')
#print(df[filt].head())
rez = df[df['cut'].isin(['Ideal','Fair','Premium'])]
print(rez.head())'''

#Write a Pandas program to display all column labels of diamonds DataFrame
'''import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/diamonds.csv')
print(df.columns)'''

#Write a Pandas program to read only a subset of 3 rows from diamonds DataFrame
'''import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/diamonds.csv')
#print(df.head())
df2 = pd.read_csv('http://bit.ly/uforeports')
print(df2.iloc[:3])'''

#Write a Pandas program to iterate through diamonds DataFrame
'''import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/diamonds.csv')
#print(df.head())
for index,row in df.iterrows():
    print(index,row['carat'],row['cut'],row['color'],row['price'])'''

#Write a Pandas program to drop all non-numeric columns from diamonds DataFrame
'''import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/diamonds.csv')
#print(df.head())
rez = df.dtypes
print(rez)'''

#Write a Pandas program to include only numeric columns in the diamonds DataFrame
'''import pandas as pd
import numpy as np
df = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/diamonds.csv')
#print(df.head())
print('include only numeric columns of dataframe')
rez = df.select_dtypes(include=np.number)
print(rez.dtypes)'''

#Write a Pandas program to pass a list of data types to only describe certain types of diamonds DataFrame
'''import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/diamonds.csv')
#print(df.head())
print('list of data types to only describe certain types')
rez = df.describe(include=['object','float64'])
print(rez)'''

#Write a Pandas program to calculate the mean of each numeric column of diamonds DataFrame
'''import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/diamonds.csv')
#print(df.head())
rez = df.mean()
print(rez)'''

#Write a Pandas program to calculate the mean of each row of diamonds DataFrame
'''import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/diamonds.csv')
#print(df.head())
rez = df.mean(axis=1)
print(rez.head())'''

#Write a Pandas program to calculate the mean of price for each cut of diamonds DataFrame
'''import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/diamonds.csv')
#print(df.head())
print('calculate the mean of price for each cut')
rez = df.groupby(['cut'])['price'].mean()
print(rez)'''

#Write a Pandas program to calculate count, minimum, maximum price for each cut of diamonds DataFrame
'''import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/diamonds.csv')
#print(df.head())
rez = df.groupby('cut')['price'].agg(['count','min','max'])
print(rez)'''

#Write a Pandas program to create a side-by-side bar plot of the diamonds DataFrame.
'''import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/diamonds.csv')
#print(df.head())
plt.figure(figsize=(10,9))
rez = df.groupby('cut').mean().plot(kind='bar')
#plt.xlabel('cut',fontsize=8,color='black')
plt.legend()
plt.show()'''

#Write a Pandas program to count how many times each value in cut series of diamonds DataFrame occurs
'''import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/diamonds.csv')
#print(df.head())
print('number of occuring each value in cut column')
rez = df['cut'].value_counts()
print(rez)'''

#Write a Pandas program to display percentages of each value of cut series occurs in diamonds DataFrame
'''import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/diamonds.csv')
#print(df.head())
rez = df['cut'].value_counts(normalize=True)
print(rez)'''

#Write a Pandas program to display the unique values in cut series of diamonds DataFrame
'''import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/diamonds.csv')
#print(df.head())
rez = df['cut'].unique()
print('unique values in cut column of dataframe')
print(rez)'''

#Write a Pandas program to count the number of unique values in cut series of diamonds DataFrame
'''import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/diamonds.csv')
#print(df.head())
print('number of unique values in cut column of dataframe')
rez = df['cut'].unique().size
print(rez)
rez2 = df['cut'].nunique()
print(rez2)'''

#Write a Pandas program to compute a cross-tabulation of two Series in diamonds DataFrame
'''import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/diamonds.csv')
#print(df.head())
rez = pd.crosstab(df['cut'],df['price'])
print(rez)'''

#Write a Pandas program to calculate various summary statistics of cut series of diamonds DataFrame.
'''import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/diamonds.csv')
#print(df.head())
print('various summary statistic of diamonds dataframe')
rez = df['carat'].describe()
print(rez)'''

#Write a Pandas program to create a histogram of the 'carat' Series (distribution of a numerical variable) of diamonds DataFrame
'''import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/diamonds.csv')
#print(df.head())
plt.figure(figsize=(8,5))
rez = df['carat'].plot(kind='hist')
plt.show()'''

#Write a Pandas program to create a bar plot of the 'value_counts' for the 'cut' series of diamonds DataFrame
'''import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/diamonds.csv')
#print(df.head())
plt.figure(figsize=(10,5))
rez = df['cut'].value_counts().plot(kind='bar',color=['blue','orange','green','red','purple'])
plt.xlabel(rez,fontsize=12,color='black')
plt.show()'''

#Write a Pandas program to create a DataFrame of booleans (True if missing, False if not missing) from diamonds DataFrame.
'''import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/diamonds.csv')
#print(df.head())
print('dataframe of booleans')
rez = df.isnull()
print(rez.head(20)) '''

# Write a Pandas program to count the number of missing values in each Series of diamonds DataFrame
'''import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/diamonds.csv')
#print(df.head())
rez = df.isnull().sum()
print(rez)'''

#Write a Pandas program to check the number of rows and columns and drop those row if 'any' values are missing\
#in a row of diamonds DataFrame
'''import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/diamonds.csv')
#print(df.head())
print('number of rows and columns')
print(df.shape)
print('after droping those rows where values are missing')
rez = df.dropna(how='any')
print(rez.shape)'''

#Write a Pandas program to drop a row if any or all values in a row are missing of diamonds DataFrame on two specific columns.
'''import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/diamonds.csv')
#print(df.head())
print('After droping those rows where any value in a row is missing in carat and cut columns:')
rez1 = df.dropna(subset=['carat','cut'],how='any')
print(rez1.shape)
print('After droping those rows where all value in a row is missing in carat and cut columns:')
rez2 = df.dropna(subset=['carat','cut'],how='all')
print(rez2.shape)'''

#Write a Pandas program to set an existing column as the index of diamonds DataFrame
'''import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/diamonds.csv')
#print(df.head())
df.set_index(keys='color',inplace=True)
print(df.head())'''

#Write a Pandas program to set an existing column as the index of diamonds DataFrame and restore the index name,\
#and move the index back to a column.
'''import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/diamonds.csv')
#print(df.head())
rez = df.set_index(keys='color')
print(rez.head())
rez2 = rez.reset_index()
print(rez2.head())'''

#Write a Pandas program to access a specified Series index and the Series values of diamonds DataFrame
'''import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/diamonds.csv')
#print(df.head())
rez1 = df['carat'].value_counts().index
print('access the Series index')
print(rez1)
rez2 = df['carat'].value_counts().values
print('access the Series values')
print(rez2)'''

#Write a Pandas program to sort a Series by its values and index of diamonds DataFrame
'''import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/diamonds.csv')
#print(df.head())
print('Series sorted by its values')
rez = df['cut'].value_counts().sort_values(ascending=True)
print(rez)
print('Series sorted by its index')
rez2 = df['cut'].value_counts().sort_index(ascending=True)
print(rez2)'''

#Write a Pandas program to calculate the multiply of length, width and depth for each cut of diamonds DataFrame
'''import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/diamonds.csv')
#print(df.head())
print('multiply of length,width and depth for each cut')
rez = df['x']*df['y']*df['z']
print(rez.head())'''

#Write a Pandas program to concatenate the diamonds DataFrame with the 'color' Series
'''import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/diamonds.csv')
#print(df.head())
rez = pd.concat([df,df['color']],axis=1,join='inner')
print(rez.head())'''

#Write a Pandas program to read specified rows and all columns of diamonds DataFrame
'''import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/diamonds.csv')
#print(df.head(7))
print('all columns')
rez = df.loc[0,:]
print(rez)'''

#Write a Pandas program to read rows 0, 5, 7 and all columns of diamonds DataFrame.
'''import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/diamonds.csv')
#print(df.head())
print('rows 0,5,7 and all columns')
rez = df.loc[[0,5,7],:]
print(rez)'''

#Write a Pandas program to read rows 2 through 5 and all columns of diamonds DataFrame
'''import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/diamonds.csv')
#print(df.head())
print('rows 2 through 5 and all columns')
rez = df.loc[2:5,:]
print(rez)'''

#Write a Pandas program to read rows 0 through 2 (inclusive), columns 'color' and 'price' of diamonds DataFrame
'''import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/diamonds.csv')
#print(df.head())
rez = df.loc[0:2,['color','price']]
print(rez)'''

#Write a Pandas program to read rows 0 through 2 (inclusive), columns 'color' through 'price' (inclusive) of diamonds DataFrame
'''import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/diamonds.csv')
#print(df.head())
rez = df.loc[0:2,['color','clarity','depth','table','price']]
print(rez)
rez2 = df.iloc[0:2,2:7]
print(rez2)
rez3 = df.loc[0:2,'color':'price']
print(rez3)'''

#Write a Pandas program to read rows in which the 'cut' is 'Premium', column 'color' of diamonds DataFrame
'''import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/diamonds.csv')
#print(df.head())
filt = df['cut']=='Premium'
rez = df[filt]
#print(rez.loc[:,['color']])
print(rez.iloc[:,2])'''

#Write a Pandas program to read rows in positions 0 and 1, columns in positions 0 and 3 of diamonds DataFrame
'''import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/diamonds.csv')
#print(df.head())
rez = df.loc[0:1,['carat','clarity']]
print(rez)
rez2 = df.iloc[[0,1],[0,3]]
print(rez2)'''

#Write a Pandas program to read rows in positions 0 through 4, columns in positions 1 through 4 of diamonds DataFrame
'''import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/diamonds.csv')
#print(df.head())
rez = df.iloc[0:4,1:4]
print(rez)
rez2 = df.loc[0:4,'cut':'clarity']
print(rez2)'''

#Write a Pandas program to read rows in positions 0 through 4 (exclusive) and all columns of diamonds DataFrame
'''import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/diamonds.csv')
#print(df.head())
rez = df.iloc[0:5,:]
print(rez)'''

#Write a Pandas program to read rows 2 through 5 (inclusive), columns in positions 0 through 2 (exclusive)\
#of diamonds DataFrame
'''import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/diamonds.csv')
#print(df.head())
rez = df.iloc[2:5,0:2]
print(rez)'''

#Write a Pandas program to print a concise summary of diamonds DataFrame
'''import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/diamonds.csv')
#print(df.head())
print('concise summary of diamonds dataframe')
rez = df.info()
print(rez)'''

#Write a Pandas program to get the true memory usage by diamonds DataFrame.
'''import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/diamonds.csv')
#print(df.head())
rez = df.info(memory_usage='deep')
print(rez)'''

#Write a Pandas program to calculate the memory usage for each Series (in bytes) of diamonds DataFrame
'''import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/diamonds.csv')
#print(df.head())
print('memory usage for each series in bytes')
rez = df.memory_usage(deep=True)
print(rez)'''

#Write a Pandas program to get randomly sample rows from diamonds DataFrame
'''import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/diamonds.csv')
#print(df.head())
rez = df.sample(n=5)
print(rez) '''

#Write a Pandas program to get sample 75% of the diamonds DataFrame's rows without replacement and\
#store the remaining 25% of the rows in another DataFrame
'''import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/diamonds.csv')
#print(df.head())
print('sample 75% of diamonds dataframe')
rez = df.sample(frac=.75,random_state=99)
print(rez)
print('remaining 25% of the rows')
rez2 = df.loc[~df.index.isin(rez.index),:]
print(rez2)'''

#Write a Pandas program to read the diamonds DataFrame and detect duplicate color.
'''import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/diamonds.csv')
#print(df.head())
print('count the duplicate items')
rez = df['color'].duplicated().sum()
print(rez)'''

#Write a Pandas program to count the duplicate rows of diamonds DataFrame.
'''import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/diamonds.csv')
#print(df.head())
print('duplicate rows of diamonds dataframe')
rez = df.iloc[:].duplicated().sum()
print(rez)
rez2 = df.duplicated().sum()
print(rez2)'''

'https://raw.githubusercontent.com/mwaskom/seaborn-data/master/diamonds.csv'
'http://bit.ly/uforeports'