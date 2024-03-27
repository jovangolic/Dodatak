#pandas filter exercises atw3resource.com

#Write a Pandas program to display the dimensions or shape of the World alcohol consumption dataset. Also extract the column names from the dataset.
'''import pandas as pd
file = pd.read_csv('world_alcohol.csv')
print('\nworld alcohol consumption sample data: ')
print(file.head())
print('\nshape of the dataframe: ') 
print(file.shape)
print("\nnumber of rows: ")
print(file.shape[0])
print('\nnumber of columns: ')
print(file.shape[1])
print('\nextract column names:')
print(file.columns)'''

#Write a Pandas program to select first 2 rows, 2 columns and specific two columns from World alcohol consumption datase
'''import pandas as pd
data = pd.read_csv('world_alcohol.csv')
#print(data.head())
print('\nselect first 2 rows: ')
print(data.iloc[:2])
print('\nselect first 2 columns')
d = data[['Year','WHO region']]
print(d.head(5))
print('\nselect 2 specific columns: ')
d1 = data[['Display Value','Year']]
print(d1) '''

#Write a Pandas program to select random number of rows, fraction of random rows from World alcohol consumption dataset
'''import pandas as pd
data = pd.read_csv('world_alcohol.csv')
print('\nselect random number of rows: ')
d1 = data.sample(5) #random number of rows
print(d1)   
print('\nselect fraction of random rows: ')
d2 = data.sample(frac=0.02) #fraction of random rows
print(d2) '''

#Write a Pandas program to find and drop the missing values from World alcohol consumption dataset
'''import pandas as pd
data = pd.read_csv('world_alcohol.csv')
print(data.head())
print('\nmissing values: ')
d = data.isnull() #finding missing values
print(d)
d1 = data.dropna()
print("\nmissing values: ")
print(d1) '''

#Write a Pandas program to remove the duplicates from 'WHO region' column of World alcohol consumption datase
'''import pandas as pd
data = pd.read_csv('world_alcohol.csv')
#print(data.head())
d = data.drop_duplicates(subset=['WHO region'])
print(d)  '''

#Write a Pandas program to find out the alcohol consumption of a given year from the world alcohol consumption dataset
'''import pandas as pd
data = pd.read_csv('world_alcohol.csv')
#print(data.head())
print('\nalcohol consumption for year 1985: ')
d1 = data['Year']==1985
print(data[d1])  
print('\nalcohol consumption for year 1989: ')
d2 = data['Year'] == 1989
print(data[d2])'''

#Write a Pandas program to find out the alcohol consumption details in the year\n
#'1987' or '1989' from the world alcohol consumption dataset.
'''import pandas as pd
data = pd.read_csv('world_alcohol.csv')
#print(data.head())
print('\nThe world alcohol consumption details where year is 1987 or 1989:')
filt = (data['Year']==1987)|(data['Year']==1989)
print(data[filt]) '''

#Write a Pandas program to find out the alcohol consumption details by the 'Americas' in the year '1989' from the world alcohol consumption dataset
'''import pandas as pd
data = pd.read_csv('world_alcohol.csv')
#print(data.head())
print('\nThe world alcohol consumption details by the Americas in the 1989:')
filt = (data['WHO region'] == 'Americas') & (data['Year'] == 1989)
print(data[filt])  '''

#Write a Pandas program to find out the alcohol consumption details in the year '1986' where WHO region is 'Western Pacific' and\n
#country is 'VietNam' from the world alcohol consumption dataset
'''import pandas as pd
data = pd.read_csv('world_alcohol.csv')
#print(data.head())
filt = (data['Year']==1986)&(data['WHO region']=='Western Pacific')&(data['Country']=='Viet Nam')
print(data[filt]) '''

#Write a Pandas program to find out the alcohol consumption details in the year '1986' or '1989'\n
#where WHO region is 'Americas' from the world alcohol consumption dataset
'''import pandas as pd
data = pd.read_csv('world_alcohol.csv')
#print(data.head())  
filt = ((data['Year']==1986)|(data['Year']==1989))&(data['WHO region'] =='Americas')
print(data[filt])  '''

#Write a Pandas program to find out the alcohol consumption details in the year '1986' or '1989' where WHO region is\n
#'Americas' or 'Europe' from the world alcohol consumption datase
'''import pandas as pd
data = pd.read_csv('world_alcohol.csv')
#print(data.head())
filt = ((data['Year']==1986) |(data['Year']==1989))&((data['WHO region']=='Americas')|(data['WHO region']=='Europe'))
print(data[filt])   '''

#Write a Pandas program to find out the 'WHO region, 'Country', 'Beverage Types' in the year '1986' or '1989' \n
#where WHO region is 'Americas' or 'Europe' from the world alcohol consumption dataset.
'''import pandas as pd
data = pd.read_csv('world_alcohol.csv')
#print(data.head())
filt = ((data['WHO region']=='Americas')|\
    (data['WHO region']=='Europe'))&((data['Year']==1986)|(data['Year']==1989))
print(data[filt][['WHO region','Country','Beverage Types']])  '''

#Write a Pandas program to find out the records where consumption of beverages per person average >=5 \n
#and Beverage Types is Beer from world alcohol consumption dataset
'''import pandas as pd
data = pd.read_csv('world_alcohol.csv')
#print(data.head())  
filt = (data['Beverage Types']=='Beer')&(data['Display Value']>=float(5))
print(data[filt]) '''

#Write a Pandas program to find out the records where consumption of beverages per person average >=4 and \n
#Beverage Types is Beer, Wine, Spirits from world alcohol consumption dataset.
'''import pandas as pd
data = pd.read_csv('world_alcohol.csv')
#print(data.head())
filt = ((data['Beverage Types']=='Beer')|(data['Beverage Types']=='Wine')|(data['Beverage Types']=='Spirits'))&\
    (data['Display Value']>=float(4))
print(data[filt])   '''

#Write a Pandas program to filter the specified columns and records by range from world alcohol consumption dataset.
'''import pandas as pd
data = pd.read_csv('world_alcohol.csv')
#print(data.head())
print(data.loc[:4,['WHO region','Beverage Types']])'''

#Write a Pandas program to filter those records where WHO region contains "Ea" substring from world alcohol consumption dataset
'''import pandas as pd
data = pd.read_csv('world_alcohol.csv')
#print(data.head())  
filt = data['WHO region'].str.contains('Ea')
print(data[filt]) '''

#Write a Pandas program to filter those records where WHO region matches with multiple values\n
#(Africa, Eastern Mediterranean, Europe) from world alcohol consumption dataset
'''import pandas as pd
data = pd.read_csv('world_alcohol.csv')
#print(data.head())
print('\nFilter by matching multiple values in a given dataframe:')
filt = (data['WHO region'].isin(['Africa','Eastern Mediterranean','Europe']))
print(data[filt]) '''

#Write a Pandas program to filter those records which not appears in a given list from world alcohol consumption dataset
'''import pandas as pd
data = pd.read_csv('world_alcohol.csv')
#print(data.head())  
print('\nselect all rows which not appears in a given list: ')
region = ["Africa", "Eastern Mediterranean", "Europe"]
filt = ~data['WHO region'].isin(region)
print(data[filt])  '''

#Write a Pandas program to filter all records where the average consumption of beverages per person from .5 to 2.50 in world alcohol consumption dataset
'''import pandas as pd
data = pd.read_csv('world_alcohol.csv')
#print(data.head())
print('\naverage consumption of beverages per person: ')
filt = (data['Display Value']>float(0.5))&(data['Display Value']<=float(2.50))
print(data[filt])   '''

#Write a Pandas program to find average consumption of wine per person greater than 2 in world alcohol consumption dataset
'''import pandas as pd
data = pd.read_csv("world_alcohol.csv")
#print(data.head())
print('\nAverage consumption of wine per person greater than 2:')
filt = (data['Beverage Types']=='Wine')&(data['Display Value']>.2)
print(data[filt].count()) '''

#Write a Pandas program to filter rows based on row numbers ended with 0, like 0, 10, 20, 30 from world alcohol consumption dataset
'''import pandas as pd
data = pd.read_csv('world_alcohol.csv')
#print(data.head())
print('\nfilter rows based on row numbers ended with 0 like 0,10,20,30: ')
print(data.filter(regex='0$',axis=0))'''

#Write a Pandas program to select consecutive columns and also select rows with Index label 0 to 9 with some columns from world alcohol consumption dataset
'''import pandas as pd
data = pd.read_csv('world_alcohol.csv')
#print(data.head())
print('\nselect consecutive columns: ')
print(data.loc[:,['Country','Beverage Types','Display Value']].head())
print('\nalternate command or different way: ')
print(data.iloc[:,2:5].head())
print('\nselect rows with index label 0-9 with specific columns: ')
print(data.loc[0:9,['Year','Country','Display Value']])'''

#Write a Pandas program to rename all and only some of the column names from world alcohol consumption dataset
'''import pandas as pd
data = pd.read_csv('world_alcohol.csv')
#print(data.head())
print('\nrename all the column names: ')
df = data.rename(columns={'Year':'year','WHO region':'who_region','Beverage Types':'beerage_types','Display Value':'display_values'})
print(df.head())   
print('\nrenaming only some of the column names')
df2 = data.rename(columns={'WHO region':'WHO_region','Display Value':'Display_Value'})
print(df2.head()) '''

#Write a Pandas program to find which years have all non-zero values and which years have any non-zero\n
#values from world alcohol consumption dataset
'''import pandas as pd
data = pd.read_csv('world_alcohol.csv')
#print(data.head())
print('\nfind which years have all non-zero values: ')
print(data.loc[:,data.all()])
print('\nfind which years have any non-zero values: ')
print(data.loc[:,data.any()])'''

#Write a Pandas program to filter all columns where all entries present, check which rows and columns has a NaN and\
#finally drop rows with any NaNs from world alcohol consumption dataset.
'''import pandas as pd
data = pd.read_csv('world_alcohol.csv')
#print(data.head())
print('\nfind all columns which all entries present: ')
#print(data.loc[:,data.all()])
print('\nrows and columns has a nan:')
#print(data.loc[:,data.isnull().any()])
print('\ndrop rows with any NaNs: ')
d1 = data.dropna(how='any')
print(d1)'''

#Write a Pandas program to filter all records starting from the 'Year' column, access every other column from world alcohol consumption dataset.
'''import pandas as pd
data = pd.read_csv('world_alcohol.csv')
#print(data.head())
print("\n from 'year' column,access every other column")
print(data.loc[:,'Year'::2])
print('\ndifferent way: ')
print(data.iloc[:,::2])'''

#Write a Pandas program to filter all records starting from the 2nd row, access every 5th row from world alcohol consumption dataset.
'''import pandas as pd
data = pd.read_csv("world_alcohol.csv")
#print(data.head())
print('\nstarting from the 2nd row,access every 5th row: ')
print(data.iloc[1::5])'''

