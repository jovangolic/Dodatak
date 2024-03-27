#Pandas Indexing exercises at w3resource.com
#Write a Pandas program to display the default index and set a column as an Index in a given dataframe.
'''import pandas as pd
df = pd.DataFrame({
    'school_code': ['s001','s002','s003','s001','s002','s004'],
    'class': ['V', 'V', 'VI', 'VI', 'V', 'VI'],
    'name': ['Alberto Franco','Gino Mcneill','Ryan Parkes', 'Eesha Hinton', 'Gino Mcneill', 'David Parkes'],
    'date_Of_Birth': ['15/05/2002','17/05/2002','16/02/1999','25/09/1998','11/05/2002','15/09/1997'],
    'weight': [35, 32, 33, 30, 31, 32],
    'address': ['street1', 'street2', 'street3', 'street1', 'street2', 'street4'],
    't_id':['t1', 't2', 't3', 't4', 't5', 't6']})
print(df)       
#df = df.set_index('school_code')
#print("\n school_code as new index: ")
#print(df)   
df2 = df['t_id']
df2 = df.set_index('t_id')
print(df2) '''

#Write a Pandas program to create a multi Index frame using two columns and using an Index and a column
'''import pandas as pd
df = pd.DataFrame({
    'school_code': ['s001','s002','s003','s001','s002','s004'],
    'class': ['V', 'V', 'VI', 'VI', 'V', 'VI'],
    'name': ['Alberto Franco','Gino Mcneill','Ryan Parkes', 'Eesha Hinton', 'Gino Mcneill', 'David Parkes'],
    'date_Of_Birth': ['15/05/2002','17/05/2002','16/02/1999','25/09/1998','11/05/2002','15/09/1997'],
    'weight': [35, 32, 33, 30, 31, 32],
    'address': ['street1', 'street2', 'street3', 'street1', 'street2', 'street4'],
    't_id':['t1', 't2', 't3', 't4', 't5', 't6']})
#print(df)   
#df = df.set_index(['t_id','school_code'])
#print(df)  
print('multiIndex using an Index and a column: ')
df1 = df.set_index([pd.Index([0,1,2,3,4,5]),'t_id'])   
print(df1)  '''

#Write a Pandas program to display the default index and set a column as an Index in a given dataframe and then reset the index
'''import pandas as pd
df = pd.DataFrame({
    'school_code': ['s001','s002','s003','s001','s002','s004'],
    'class': ['V', 'V', 'VI', 'VI', 'V', 'VI'],
    'name': ['Alberto Franco','Gino Mcneill','Ryan Parkes', 'Eesha Hinton', 'Gino Mcneill', 'David Parkes'],
    'date_Of_Birth': ['15/05/2002','17/05/2002','16/02/1999','25/09/1998','11/05/2002','15/09/1997'],
    'weight': [35, 32, 33, 30, 31, 32],
    'address': ['street1', 'street2', 'street3', 'street1', 'street2', 'street4'],
    't_id':['t1', 't2', 't3', 't4', 't5', 't6']})
#print(df)           
#print('\nt_id as new index: ')
df1 = df.set_index('t_id')
#print(df1) 
print('\n reset the index: ')     
df2 = df1.reset_index(inplace=False)
print(df2) '''

#Write a Pandas program to create an index labels by using 64-bit integers, using floating-point numbers in a given dataframe.
'''import pandas as pd
df_i64 = pd.DataFrame({
    'school_code': ['s001','s002','s003','s001','s002','s004'],
    'class': ['V', 'V', 'VI', 'VI', 'V', 'VI'],
    'name': ['Alberto Franco','Gino Mcneill','Ryan Parkes', 'Eesha Hinton', 'Gino Mcneill', 'David Parkes'],
    'date_Of_Birth': ['15/05/2002','17/05/2002','16/02/1999','25/09/1998','11/05/2002','15/09/1997'],
    'weight': [35, 32, 33, 30, 31, 32],
    'address': ['street1', 'street2', 'street3', 'street1', 'street2', 'street4']},
    index=[1, 2, 3, 4, 5, 6])
#print(df_i64)
#print(df_i64.index)        
df = pd.DataFrame({
    'school_code': ['s001','s002','s003','s001','s002','s004'],
    'class': ['V', 'V', 'VI', 'VI', 'V', 'VI'],
    'name': ['Alberto Franco','Gino Mcneill','Ryan Parkes', 'Eesha Hinton', 'Gino Mcneill', 'David Parkes'],
    'date_Of_Birth': ['15/05/2002','17/05/2002','16/02/1999','25/09/1998','11/05/2002','15/09/1997'],
    'weight': [35, 32, 33, 30, 31, 32],
    'address': ['street1', 'street2', 'street3', 'street1', 'street2', 'street4']},
    index=[.1, .2, .3, .4, .5, .6])
print('\n floating-point labels using float64index: ')
print(df)
print(df.index)   '''

#Write a Pandas program to create a DataFrame using intervals as an index
'''import pandas as pd
df_interval = pd.DataFrame({"X":[1,2,3,4,5,6,7]},
    index=pd.IntervalIndex.from_breaks([0,0.5,1.0,1.5,2.0,2.5,3,3.5]))
#print("Create an Interval Index using IntervalIndex.from_breaks:")
#print(df_interval)  
#print(df_interval.index)    
#print("Create an Interval Index using IntervalIndex.from_tuples:")
df_interval_tuple = pd.DataFrame({'X':[1,2,3,4,5,6,7]},
    index = pd.IntervalIndex.from_tuples([(0,0.5),(0.5,1),(1,1.5),(1.5,2),(2,2.5),(2.5,3),(3,3.5)]))
#print(df_interval_tuple)    
#print(df_interval_tuple.index)
df_interval_arrays = pd.DataFrame({'X':[1,2,3,4,5,6,7]},
    index = pd.IntervalIndex.from_arrays([0,.5,1,1.5,2,2.5,3],[.5,1,1.5,2,2.5,3,3.5]))
print("Create an Interval Index using IntervalIndex.from_arrays:")   
print(df_interval_arrays)
print(df_interval_arrays.index) '''

#Write a Pandas program to create a dataframe indexing by date and time.
'''import pandas as pd
dt_range = pd.date_range(start ='2020-05-12 07:10:10', freq ='S', periods = 10) 
df_dt = pd.DataFrame({"Sale_amt":[100, 110, 117, 150, 112, 99, 129, 135, 140, 150]},
                            index = dt_range)
print(df_dt)'''

#Write a Pandas program to create a dataframe and set a title or name of the index column
'''import pandas as pd
df = pd.DataFrame({
    'school_code': ['s001','s002','s003','s001','s002','s004'],
    'class': ['V', 'V', 'VI', 'VI', 'V', 'VI'],
    'name': ['Alberto Franco','Gino Mcneill','Ryan Parkes', 'Eesha Hinton', 'Gino Mcneill', 'David Parkes'],
    'date_Of_Birth': ['15/05/2002','17/05/2002','16/02/1999','25/09/1998','11/05/2002','15/09/1997'],
    'weight': [35, 32, 33, 30, 31, 32],
    'address': ['street1', 'street2', 'street3', 'street1', 'street2', 'street4']},
                                index = ['t1', 't2', 't3', 't4', 't5', 't6'])
#print(df)                                   
df.index.name = 'Index_name'
print(df)   '''

#Write a Pandas program to set value in a specific cell in a given dataframe using index.
'''import pandas as pd
df = pd.DataFrame({
    'school_code': ['s001','s002','s003','s001','s002','s004'],
    'class': ['V', 'V', 'VI', 'VI', 'V', 'VI'],
    'name': ['Alberto Franco','Gino Mcneill','Ryan Parkes', 'Eesha Hinton', 'Gino Mcneill', 'David Parkes'],
    'date_of_birth': ['15/05/2002','17/05/2002','16/02/1999','25/09/1998','11/05/2002','15/09/1997'],
    'weight': [35, 32, 33, 30, 31, 32]},
     index = ['t1', 't2', 't3', 't4', 't5', 't6'])
#print(df)  
df.at['t6','school_code'] = 's005'
#print('set school code s004 to s005: ')
#print(df)         
df.at['t1','date_of_birth'] = '16/05/2002'
#print('set date_of_birth of Alberto Franco to 16/05/2002: ')
print(df) '''

#Write a Pandas program to convert index of a given dataframe into a column.
'''import pandas as pd
df = pd.DataFrame({
    'school_code': ['s001','s002','s003','s001','s002','s004'],
    'class': ['V', 'V', 'VI', 'VI', 'V', 'VI'],
    'name': ['Alberto Franco','Gino Mcneill','Ryan Parkes', 'Eesha Hinton', 'Gino Mcneill', 'David Parkes'],
    'date_of_birth': ['15/05/2002','17/05/2002','16/02/1999','25/09/1998','11/05/2002','15/09/1997'],
    'weight': [35, 32, 33, 30, 31, 32]},
     index = ['t1', 't2', 't3', 't4', 't5', 't6'])
#print(df)
print('convert indext of DataFrame into a column: ')    
df.reset_index(level=0,inplace=True) 
print(df)'''

#Write a Pandas program to convert 1st and 3rd levels in the index into columns\
#  from a multiple level of index frame of a given dataframe.
'''import pandas as pd
df = pd.DataFrame({
    'school_code': ['s001','s002','s003','s001','s002','s004'],
    'class': ['V', 'V', 'VI', 'VI', 'V', 'VI'],
    'name': ['Alberto Franco','Gino Mcneill','Ryan Parkes', 'Eesha Hinton', 'Gino Mcneill', 'David Parkes'],
    'date_of_birth': ['15/05/2002','17/05/2002','16/02/1999','25/09/1998','11/05/2002','15/09/1997'],
    'weight': [35, 32, 33, 30, 31, 32],
    't_id': ['t1', 't2', 't3', 't4', 't5', 't6']})
#print(df)       
print('multiIndex using columns t_id,school_code,and class: ')
df1 = df.set_index(['t_id','school_code','class'])
print(df1) 
print('convert 1st and 3rd levels in the indexframe into columns: ') 
df2 = df1.reset_index(level=['t_id','school_code'])
print(df2) '''

#Write a Pandas program to check if a specified value exists in single and multiple column index dataframe.
'''import pandas as pd
df = pd.DataFrame({
    'school_code': ['s001','s002','s003','s001','s002','s004'],
    'class': ['V', 'V', 'VI', 'VI', 'V', 'VI'],
    'name': ['Alberto Franco','Gino Mcneill','Ryan Parkes', 'Eesha Hinton', 'Gino Mcneill', 'David Parkes'],
    'date_of_birth': ['15/05/2002','17/05/2002','16/02/1999','25/09/1998','11/05/2002','15/09/1997'],
    'weight': [35, 32, 33, 30, 31, 32]},
     index =  ['t1', 't2', 't3', 't4', 't5', 't6'])
#print(df)        
#print('\ncheck if value exists in single column index dataframe')
#print('t2' in df.index)
#print('t7' in df.index)
df1 = pd.DataFrame({
    'school_code': ['s001','s002','s003','s001','s002','s004'],
    'class': ['V', 'V', 'VI', 'VI', 'V', 'VI'],
    'name': ['Alberto Franco','Gino Mcneill','Ryan Parkes', 'Eesha Hinton', 'Gino Mcneill', 'David Parkes'],
    'date_of_birth': ['15/05/2002','17/05/2002','16/02/1999','25/09/1998','11/05/2002','15/09/1997'],
    'weight': [35, 32, 33, 30, 31, 32],
    't_id': ['t1', 't2', 't3', 't4', 't5', 't6']}) 
#print(df1)     
df2 = df1.set_index(['t_id','school_code','class'])
print(df2)  
print('\ncheck if value exists in multiple columns index dataframe: ')
print('t4' in df2.index.levels[0])
print('t4' in df2.index.levels[1])
print('t4' in df2.index.levels[2])  '''

#Write a Pandas program to construct a series using the MultiIndex levels as the column and index
'''import pandas as pd 
import numpy as np
sales_arrays = [['sale1', 'sale1', 'sale2', 'sale2', 'sale3', 'sale3', 'sale4', 'sale4'],
          ['city1', 'city2', 'city1', 'city2', 'city1', 'city2', 'city1', 'city2']]
sales = list(zip(*sales_arrays))
print('create multiIndex: ') 
sales_index = pd.MultiIndex.from_tuples(sales,names=['sale','city'])
print(sales) 
print('\n construct a series using multiIndex level: ')
s = pd.Series(np.random.randn(8),index=sales_index)
print(s) '''

#Write a Pandas program to construct a DataFrame using the MultiIndex levels as the column and index.
'''import pandas as pd
import numpy as np
sales_arrays = [['sale1', 'sale1', 'sale2', 'sale2', 'sale3', 'sale3', 'sale4', 'sale4'],
          ['city1', 'city2', 'city1', 'city2', 'city1', 'city2', 'city1', 'city2']]
sales_tuples = list(zip(*sales_arrays))
print('\ncreate a multiIndex: ')
m_index = pd.MultiIndex.from_tuples(sales_tuples,name=['sale','city']) 
#print(m_index)           
print("\nconstruct a dataframe using MultiIndex levels: ")
df = pd.DataFrame(np.random.randn(8,5),index=m_index)
print(df) '''

#Write a Pandas program to extract a single row, rows and a specific value from a MultiIndex levels DataFrame.
'''import pandas as pd
import numpy as np
sales_arrays = [['sale1', 'sale1', 'sale2', 'sale2', 'sale3', 'sale3', 'sale4', 'sale4'],
          ['city1', 'city2', 'city1', 'city2', 'city1', 'city2', 'city1', 'city2']]
sales_tuples = list(zip(*sales_arrays))
m_index = pd.MultiIndex.from_tuples(sales_tuples,names=['sale','city'])
#print(sales_tuples)
print("\nconsturct a DataFrame using multiIndex levels: ")
df = pd.DataFrame(np.random.randn(8,5),index=m_index)
#print(df)  
#print("\n extract a single row from dataframe: ") 
#print(df.loc['sale1','city1'])
#print(df.loc['sale2','city2'])  
#print("\nextract number of rows from dataframe: ")
#print(df.loc['sale2'])
#print(df.loc['sale4'])
print('\nextract a single value from dataframe: ')
#print(df.iat[1,2])
#print(df.iat[6,4])
print(df.loc[('sale1','city2'),1])
print(df.loc[('sale4','city1'),4])'''

#Write a Pandas program to rename names of columns and specific labels of the Main Index of the MultiIndex dataframe
'''import pandas as pd 
import numpy as np
sales_arrays = [['sale1', 'sale1', 'sale2', 'sale2', 'sale3', 'sale3', 'sale4', 'sale4'],
          ['city1', 'city2', 'city1', 'city2', 'city1', 'city2', 'city1', 'city2']]
s_tuple = list(zip(*sales_arrays))
#print(s_tuple)           
m_index = pd.MultiIndex.from_tuples(s_tuple,names=['sale','city'])
#print(m_index)  
df = pd.DataFrame(np.random.randn(8,5),index=m_index)
#print(df)   
#print('\nrename the columns name: ')
df1 = df.rename(columns={0:'col1',1:'col2',2:'col3',3:'col4',4:'col5'})
print(df1)  
print('\nrename specific labels of the main index: ')
df2 = df1.rename({'sale2':'S2','city2':'C2'},axis=0)
print(df2)'''

#Write a Pandas program to sort a MultiIndex of a DataFrame. Also sort on various levels of index
'''import pandas as pd 
import numpy as np
sales_arrays = [['sale1', 'sale1', 'sale3', 'sale3', 'sale2', 'sale2', 'sale4', 'sale4'],
          ['city1', 'city2', 'city1', 'city2', 'city1', 'city2', 'city1', 'city2']]
s_tuple = list(zip(*sales_arrays))
#print(s_tuple)            
m_index = pd.MultiIndex.from_tuples(s_tuple,names=['sale','city'])
#print(m_index)  
df = pd.DataFrame(np.random.randn(8,5),index=m_index)   
#print(df)  
print('\nsort on multiIndex dataframe: ') 
print(df.sort_index())
print("\nsort on index level=0 of the dataframe: ")
df1 = df.sort_index(level=0)
print(df1)  
df2 = df.sort_index(level=1) 
print("\nsort on index level=1 of the dataframe: ")
print(df2)  
print('\pass a level name to sort the dataframe')
df3 = df.sort_index(level='city')
print(df3)  '''

#Write a Pandas program to extract elements in the given positional indices along an axis of a dataframe.
'''import pandas as pd 
import numpy as np
sales_arrays = [['sale1', 'sale1', 'sale3', 'sale3', 'sale2', 'sale2', 'sale4', 'sale4'],
          ['city1', 'city2', 'city1', 'city2', 'city1', 'city2', 'city1', 'city2']]
s_tuple = list(zip(*sales_arrays))
#print(s_tuple)            
m_index = pd.MultiIndex.from_tuples(s_tuple,names=['sale','city'])
#print(m_index)  
df = pd.DataFrame(np.random.randn(8,5),index=m_index)
#print(df)   
print('\nselect 1st,2nd,3rd row of the dataframe: ')
pos = [1,2,5]
df1 = df.take(pos)
print(df1)  
print('\ntake elements at indices 1,2 along the axis 1:')
df2 = df.take([1,2],axis=1)
print(df2)  
#print(df.take([1,2],axis=1))   
print('\Take elements at indices 4 and 3 using negative integers along the axis 1 (column selection):')
df3 = df.take([-1,-2],axis=1)
print(df3)'''

#Write a Pandas program to get the index of an element of a given Series
'''import pandas as pd
s = pd.Series([1,3,5,7,9,11,13,15], index=[0,1,2,3,4,5,7,8])
#print(s)    
print('\nIndex of 11 in the series: ')
idx_s = s[s==11].index[0]
print(idx_s)'''

#Write a Pandas program to get the index of an element of a given Series.
'''import pandas as pd
ds = pd.Series([1,3,5,7,9,11,13,15], index=[0,1,2,3,4,5,7,8])
#print(ds)   
print('\nthrid row: ')
x = ds.iloc[[2]]
print(x)   
print('\nfifth row: ')
y = ds.iloc[[4]] 
print(y)
df = pd.DataFrame({
    'school_code': ['s001','s002','s003','s001','s002','s004'],
    'class': ['V', 'V', 'VI', 'VI', 'V', 'VI'],
    'name': ['Alberto Franco','Gino Mcneill','Ryan Parkes', 'Eesha Hinton', 'Gino Mcneill', 'David Parkes'],
    'date_of_birth': ['15/05/2002','17/05/2002','16/02/1999','25/09/1998','11/05/2002','15/09/1997'],
    'weight': [35, 32, 33, 30, 31, 32]})
#print(df)    
print('\nthird row: ')   
a = df.iloc[[2]]
print(a)    
print('\nfifth row')
b = df.iloc[[4]]
print(b)  '''

#Write a Pandas program to find the indexes of rows of a specified value of a given column in a DataFrame.
'''import pandas as pd
df = pd.DataFrame({
    'school_code': ['s001','s002','s003','s001','s002','s004'],
    'class': ['V', 'V', 'VI', 'VI', 'V', 'VI'],
    'name': ['Alberto Franco','Gino Mcneill','Ryan Parkes', 'Eesha Hinton', 'Gino Mcneill', 'David Parkes'],
    'date_of_birth': ['15/05/2002','17/05/2002','16/02/1999','25/09/1998','11/05/2002','15/09/1997'],
    'weight': [35, 32, 33, 30, 31, 32]},
     index =  [1, 2, 3, 4, 5, 6])
#print(df)        
print(df.index[df['school_code'] == 's001'].tolist())'''

#Write a Pandas program to drop a index level from a multi-level column index of a dataframe
'''import pandas as pd
cols = pd.MultiIndex.from_tuples([("a", "x"), ("a", "y"), ("a", "z")])
print("\nConstruct a Dataframe using the said MultiIndex levels: ")
df = pd.DataFrame([[1,2,3], [3,4,5], [5,6,7]], columns=cols)
print(df)   
#df.columns = df.columns.droplevel(0)
#print('\remove the top level index: ')
#print(df)
print('\nremove the index next to top level: ')
df.columns = df.columns.droplevel(1)
print(df)  '''

##Write a Pandas program to insert a column at a specific index in a given DataFrame.
'''import pandas as pd
df = pd.DataFrame({
    'school_code': ['s001','s002','s003','s001','s002','s004'],
    'class': ['V', 'V', 'VI', 'VI', 'V', 'VI'],
    'name': ['Alberto Franco','Gino Mcneill','Ryan Parkes', 'Eesha Hinton', 'Gino Mcneill', 'David Parkes'],
    'weight': [35, 32, 33, 30, 31, 32]},
     index =  [1, 2, 3, 4, 5, 6])
#print(df)        
val = ['15/05/2002','17/05/2002','16/02/1999','25/09/1998','11/05/2002','15/09/1997']
col = 'date_of_birth'
df.insert(3,column=col,value=val)
print(df) '''

#Write a Pandas program to print a DataFrame without index
'''import pandas as pd
df = pd.DataFrame({
    'school_code': ['s001','s002','s003','s001','s002','s004'],
    'class': ['V', 'V', 'VI', 'VI', 'V', 'VI'],
    'name': ['Alberto Franco','Gino Mcneill','Ryan Parkes', 'Eesha Hinton', 'Gino Mcneill', 'David Parkes'],
    'date_of_birth': ['15/05/2002','17/05/2002','16/02/1999','25/09/1998','11/05/2002','15/09/1997'],
    'weight': [35, 32, 33, 30, 31, 32]},
     index =  [1, 2, 3, 4, 5, 6])
#print(df)        
print('\ndataframe without index: ')
print(df.to_string(index=False))'''

#Write a Pandas program to find integer index of rows with missing data in a given dataframe
'''import numpy as np
import pandas as pd
df = pd.DataFrame({
    'school_code': ['s001','s002','s003','s001','s002','s004'],
    'class': ['V', 'V', 'VI', 'VI', 'V', 'VI'],
    'name': ['Alberto Franco','Gino Mcneill','Ryan Parkes', 'Eesha Hinton', 'Gino Mcneill', 'David Parkes'],
    'date_of_birth': ['15/05/2002','17/05/2002','16/02/1999','25/09/1998','11/05/2002','15/09/1997'],
    'weight': [35, None, 33, 30, 31, None]},
     index = ['t1', 't2', 't3', 't4', 't5', 't6'])
#print(df) 
idx = df['weight'].index[df['weight'].apply(np.isnan)]
df1 = df.index.tolist()
print([df1.index(i) for i in idx])'''

#Write a Pandas program to start index with different value rather than 0 in a given DataFrame
'''import pandas as pd
df = pd.DataFrame({
    'school_code': ['s001','s002','s003','s001','s002','s004'],
    'class': ['V', 'V', 'VI', 'VI', 'V', 'VI'],
    'name': ['Alberto Franco','Gino Mcneill','Ryan Parkes', 'Eesha Hinton', 'Gino Mcneill', 'David Parkes'],
    'date_of_birth': ['15/05/2002','17/05/2002','16/02/1999','25/09/1998','11/05/2002','15/09/1997'],
    'weight': [35, 37, 33, 30, 31, 32]})
#print(df)   
print('\ndefault index range: ')    
print(df.index)
df.index+=10
print(df.index)
print(df) '''

#Write a Pandas program to select rows by filtering on one or more column(s) in a multi-index dataframe
'''import pandas as pd
df = pd.DataFrame({
    'school_code': ['s001','s002','s003','s001','s002','s004'],
    'class': ['V', 'V', 'VI', 'VI', 'V', 'VI'],
    'name': ['Alberto Franco','Gino Mcneill','Ryan Parkes', 'Eesha Hinton', 'Gino Mcneill', 'David Parkes'],
    'date_of_birth': ['15/05/2002','17/05/2002','16/02/1999','25/09/1998','11/05/2002','15/09/1997'],
    'weight': [35, 37, 33, 30, 31, 32],
    'tcode': ['t1', 't2', 't3', 't4', 't5', 't6']})
#print(df)       
df = df.set_index(['tcode','school_code'])
#print('\nmultiIndex')
#print(df)
#print('\nselect row(s) from tcode column: ')
#print(df.query("tcode == 't2'"))
#print('\nselect row(s) from school_code column: ')
#print(df.query("school_code == 's001'"))
print('\nselect row(s) fro tcode and school_code columns: ')
print(df.query("tcode == 's001'")&(df.query("school_code == 's001'")))'''

