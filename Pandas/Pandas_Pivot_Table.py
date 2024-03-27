#pandas pivot table exercises at w3resource.com

#Write a Pandas program to create a Pivot table with multiple indexes from a given excel sheet (Salesdata.xlsx)
'''import pandas as pd
import jinja2
df = pd.read_excel('SaleData.xlsx')
#print(df.head())
print(pd.pivot_table(df,index=['Region','SalesMan']))'''

#Write a Pandas program to create a Pivot table and find the total sale amount region wise, manager wise
'''import pandas as pd
import numpy as np
df = pd.read_excel('SaleData.xlsx')
#print(df.head())   
rez = pd.pivot_table(df,index=['Region','Manager'],values=['Sale_amt'],aggfunc=np.sum)
print(rez)  '''

#Write a Pandas program to create a Pivot table and find the total sale amount region wise, manager wise, sales man wise.
'''import pandas as pd
import numpy as np
df = pd.read_excel('SaleData.xlsx')
#print(df.head())
rez = pd.pivot_table(df,index=['Region','Manager','SalesMan'],values=['Sale_amt'],aggfunc=np.sum)
print(rez)  '''

#Write a Pandas program to create a Pivot table and find the item wise unit sold.
'''import pandas as pd
import numpy as np
df = pd.read_excel('SaleData.xlsx')
#print(df.head())
rez = pd.pivot_table(df,index='Item',values='Units',aggfunc=np.sum)
print(rez) '''

#Write a Pandas program to create a Pivot table and find the region wise total sale.
'''import pandas as pd
import numpy as np
df = pd.read_excel('SaleData.xlsx')
#print(df.head())
rez = pd.pivot_table(df,index='Region',values='Sale_amt',aggfunc=np.sum)
print(rez)  '''

#Write a Pandas program to create a Pivot table and find the region wise, item wise unit sold
'''import pandas as pd
import numpy as np
df = pd.read_excel('SaleData.xlsx')
#print(df.head())
rez = pd.pivot_table(df,index=['Region','Item'],values='Units',aggfunc=np.sum)
print(rez)  '''

#Write a Pandas program to create a Pivot table and count the manager wise sale and mean value of sale amount
'''import pandas as pd
import numpy as np
df = pd.read_excel('SaleData.xlsx')
#print(df.head())
rez = pd.pivot_table(df,index='Manager',values=['Sale_amt'],aggfunc=[np.mean,len])
print(rez) '''

#Write a Pandas program to create a Pivot table and find manager wise, salesman wise total sale\
#and also display the sum of all sale amount at the bottom
'''import pandas as pd
import numpy as np
df = pd.read_excel('SaleData.xlsx')
#print(df.head())
rez = pd.pivot_table(df,index=['Manager','SalesMan'],values=['Sale_amt','Units'],aggfunc=np.sum,\
        fill_value=0,margins=True)
print(rez)'''

#Write a Pandas program to create a Pivot table and find the total sale amount region wise,\
#manager wise, sales man wise where Manager = "Douglas".
'''import pandas as pd
import numpy as np
df = pd.read_excel('SaleData.xlsx')
table = pd.pivot_table(df,index=["Region","Manager","SalesMan"], values="Sale_amt")
print(table.query('Manager == ["Douglas"]'))'''

#Write a Pandas program to create a Pivot table and find the region wise Television and Home Theater sold.
'''import pandas as pd
import numpy as np
df = pd.read_excel('SaleData.xlsx')
#print(df.head())
rez = pd.pivot_table(df,index=['Region','Item'],values='Units')
print(rez.query("Item == ['Home Theater','Television']"))'''

#Write a Pandas program to create a Pivot table and find the maximum sale value of the items
'''import pandas as pd
import numpy as np
df = pd.read_excel('SaleData.xlsx')
#print(df.head())
rez = pd.pivot_table(df,index=['Item'],values='Sale_amt',aggfunc=np.max)
print(rez)  '''

#Write a Pandas program to create a Pivot table and find the minimum sale value of the items.
'''import pandas as pd
import numpy as np
df = pd.read_excel('SaleData.xlsx')
#print(df.head())
rez = pd.pivot_table(df,index=['Item'],values='Sale_amt',aggfunc=np.min)
print(rez)  '''

#Write a Pandas program to create a Pivot table and find the maximum and minimum sale value of the items
'''import pandas as pd
import numpy as np
df = pd.read_excel('SaleData.xlsx')
#print(df.head())
rez = pd.pivot_table(df,index=['Item'],values='Sale_amt',aggfunc=[np.max,np.min])
print(rez) '''

#Write a Pandas program to print a concise summary of the dataset (titanic.csv).
'''import pandas as pd
df = pd.read_csv('titanic.txt')
#print(df)   
rez = df.info()
print(rez) '''

#Write a Pandas program to extract the column labels, shape and data types of the dataset (titanic.csv)
'''import pandas  as pd
df = pd.read_csv('titanic1.csv') 
#print(df.head())
rez = df.columns
print('\nlist of columns: ')
print(rez)      
#print('\nshape of the dataset:')
print(df.shape)
print(df.dtypes)'''

#Write a Pandas program to create a Pivot table with multiple indexes from the data set of titanic.csv.
'''import pandas as pd
import numpy as np
df = pd.read_csv('titanic.csv')
#print(df.head())
rez = df.pivot_table(df,index=['sex','age'],aggfunc=np.sum)
print(rez)'''

#Write a Pandas program to create a Pivot table and find survival rate by gender on various classes
'''import pandas as pd
import numpy as np
df = pd.read_csv('titanic.csv')
#print(df.head())
rez = df.pivot_table('survived',index='sex',columns='class')
print(rez) '''

#Write a Pandas program to create a Pivot table and find survival rate by gender.
'''import pandas as pd
import numpy as np
df = pd.read_csv('titanic.csv')
#print(df.head())
rez = df.pivot_table('survived',index='sex')
print(rez)  
rez2 = df.groupby(by='sex').agg({'survived':'mean'})
print(rez2)'''

#Write a Pandas program to create a Pivot table and find survival rate by gender, age wise of various classes
'''import pandas as pd
import numpy as np
df = pd.read_csv('titanic.csv')
#print(df.head())
rez = df.pivot_table('survived',index=['sex','age'],columns='class')
print(rez) '''

#Write a Pandas program to partition each of the passengers into four categories based on their age
#Note: Age categories (0, 10), (10, 30), (30, 60), (60, 80)
'''import pandas as pd
import numpy as np
df = pd.read_csv('titanic.csv')
#print(df.head())
rez = pd.cut(df['age'],[0,10,30,60,80])
print(rez) '''

# Write a Pandas program to create a Pivot table and count survival by gender, categories wise age of various classes
#Note: Age categories (0, 10), (10, 30), (30, 60), (60, 80)
'''import pandas as pd
import numpy as np
df = pd.read_csv('titanic.csv')
#print(df.head())
age = pd.cut(df['age'],[0,10,30,60,80])
#print(cat)
rez = df.pivot_table('survived',index=['sex',age],columns='pclass',aggfunc='count')
print(rez) '''

#Write a Pandas program to create a Pivot table and find survival rate by gender, age of the different categories of various classes
#age categories 0, 20,55
'''import pandas as pd
df = pd.read_csv('titanic.csv')
#print(df.head())
age = pd.cut(df['age'],[0,20,55])
#print(age)
rez = df.pivot_table('survived',index=['sex',age],columns='class')
print(rez) '''

#Write a Pandas program to create a Pivot table and find survival rate by gender,\
#age of the different categories of various classes. Add the fare as a dimension of columns\
#and partition fare column into 2 categories based on the values present in fare columns
'''import pandas as pd
import numpy as np
df = pd.read_csv('titanic.csv')
#print(df.head())
fare = pd.qcut(df['fare'],2)
age = pd.cut(df['age'],[0,10,30,60,80])
rez = df.pivot_table('survived',index=['sex',age],columns=[fare,'pclass'])
print(rez)  '''

# Write a Pandas program to create a Pivot table and calculate number of women and men were in a particular cabin class
'''import pandas as pd
import numpy as np
df = pd.read_csv('titanic.csv')
#print(df.head())
rez = df.pivot_table(index=['sex'],columns='pclass',aggfunc='count')
print(rez) '''

#Write a Pandas program to create a Pivot table and find survival of both gender and class affected
'''import pandas as pd
df = pd.read_csv('titanic.csv')
#print(df.head())
rez = df.pivot_table('survived',index=['sex'],columns='class')
print(rez) 
rez2 = df.groupby(['sex','class'])['survived'].aggregate('mean').unstack()
print(rez2) '''

#Write a Pandas program to create a Pivot table and compute survival totals of all classes along each group. 
'''import pandas as pd
import numpy as np
df = pd.read_csv('titanic.csv')
#print(df.head())
rez = df.pivot_table('survived',index=['sex'],columns='class',margins=True)
print(rez) '''

#Write a Pandas program to create a Pivot table and calculate how many women and men were in a particular cabin class
'''import pandas as pd
import numpy as np
df = pd.read_csv('titanic.csv')
#print(df.head())
rez = df.pivot_table('who',index='sex',columns='pclass',aggfunc='count')
#print(rez)      
rez2 = df.pivot_table(index='sex',values='who',columns='pclass',aggfunc='count')
print(rez2)'''

#Write a Pandas program to create a Pivot table and find number of survivors and average rate grouped by gender and class
'''import pandas as pd
import numpy as np
df = pd.read_csv('titanic.csv')
#print(df.head())
rez = df.pivot_table(['fare','survived'],index='sex',columns='class',aggfunc=np.sum)
print(rez)      
rez2 = df.pivot_table(index='sex',columns='class',aggfunc=({'fare':'mean','survived':'sum'}))
print(rez2)
rez3 = df.groupby(['sex','class']).agg({'fare':'mean','survived':'sum'})
#print(rez3)'''

#Write a Pandas program to create a Pivot table and find number of adult male, adult female and children.
'''import pandas as pd
df = pd.read_csv('titanic.csv')
#print(df.head())
rez = df.groupby('who').agg({'sex':'count'})
#print(rez)           
rez2 = pd.pivot_table(df,index='who',values='sex',aggfunc='count')
#print(rez2)
rez3 = df.pivot_table('sex','who',aggfunc='count')
print(rez3)'''

#Write a Pandas program to create a Pivot table and check missing values of children.
'''import pandas as pd
import numpy as np
df = pd.read_csv('titanic.csv')
#print(df.head())
rez = df.loc[df["who"]=='child'].isna().sum()
print(rez)  '''

#Write a Pandas program to create a Pivot table and separate the gender according to whether they\
#traveled alone or not to get the probability of survival.
'''import pandas as pd
df = pd.read_csv('titanic.csv')
#print(df.head())
rez = df.pivot_table('survived',index=['sex','alone'],columns='class')
print(rez) '''

#Write a Pandas program to create a Pivot table and find the probability of survival by class,\
#gender, solo boarding and port of embarkation.
'''import pandas as pd
df = pd.read_csv('titanic.csv')
#print(df.head())
rez = df.pivot_table('survived',index=['sex','alone'],columns=['embark_town','class'])
print(rez)  '''

