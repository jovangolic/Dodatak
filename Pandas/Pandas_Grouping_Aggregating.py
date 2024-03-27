#Pandas Grouping and Aggregating at w3resource.com

#Write a Pandas program to split the following dataframe into groups based on school code. \n
#Also check the type of GroupBy object
'''import pandas as pd
pd.set_option('display.max_rows', None)
#pd.set_option('display.max_columns', None)
student_data = pd.DataFrame({
    'school_code': ['s001','s002','s003','s001','s002','s004'],
    'class': ['V', 'V', 'VI', 'VI', 'V', 'VI'],
    'name': ['Alberto Franco','Gino Mcneill','Ryan Parkes', 'Eesha Hinton', 'Gino Mcneill', 'David Parkes'],
    'date_Of_Birth ': ['15/05/2002','17/05/2002','16/02/1999','25/09/1998','11/05/2002','15/09/1997'],
    'age': [12, 12, 13, 13, 14, 12],
    'height': [173, 192, 186, 167, 151, 159],
    'weight': [35, 32, 33, 30, 31, 32],
    'address': ['street1', 'street2', 'street3', 'street1', 'street2', 'street4']},
    index=['S1', 'S2', 'S3', 'S4', 'S5', 'S6'])
#print(student_data) 
print('\nsplit the said data on school_code:')
rez = student_data.groupby(['school_code'])
for name,group in rez:
    print('\nGroup: ')
    print(name)
    print(group)
print(type(rez)) '''

#Write a Pandas program to split the following dataframe by school code and get mean, min, and max value of age for each school
'''import pandas as pd
pd.set_option('display.max_rows', None)
#pd.set_option('display.max_columns', None)
student_data = pd.DataFrame({
    'school_code': ['s001','s002','s003','s001','s002','s004'],
    'class': ['V', 'V', 'VI', 'VI', 'V', 'VI'],
    'name': ['Alberto Franco','Gino Mcneill','Ryan Parkes', 'Eesha Hinton', 'Gino Mcneill', 'David Parkes'],
    'date_Of_Birth ': ['15/05/2002','17/05/2002','16/02/1999','25/09/1998','11/05/2002','15/09/1997'],
    'age': [12, 12, 13, 13, 14, 12],
    'height': [173, 192, 186, 167, 151, 159],
    'weight': [35, 32, 33, 30, 31, 32],
    'address': ['street1', 'street2', 'street3', 'street1', 'street2', 'street4']},
    index=['S1', 'S2', 'S3', 'S4', 'S5', 'S6'])
#print(student_data)
rez = student_data.groupby(by='school_code').agg({'age':['mean','min','max']})
print(rez) '''

#Write a Pandas program to split the following given dataframe into groups based on school code and class
'''import pandas as pd
pd.set_option('display.max_rows', None)
#pd.set_option('display.max_columns', None)
student_data = pd.DataFrame({
    'school_code': ['s001','s002','s003','s001','s002','s004'],
    'class': ['V', 'V', 'VI', 'VI', 'V', 'VI'],
    'name': ['Alberto Franco','Gino Mcneill','Ryan Parkes', 'Eesha Hinton', 'Gino Mcneill', 'David Parkes'],
    'date_Of_Birth ': ['15/05/2002','17/05/2002','16/02/1999','25/09/1998','11/05/2002','15/09/1997'],
    'age': [12, 12, 13, 13, 14, 12],
    'height': [173, 192, 186, 167, 151, 159],
    'weight': [35, 32, 33, 30, 31, 32],
    'address': ['street1', 'street2', 'street3', 'street1', 'street2', 'street4']},
    index=['S1', 'S2', 'S3', 'S4', 'S5', 'S6'])
#print(student_data) 
print('\nsplit the data on school_code,class wise: ')
rez = student_data.groupby(by=['school_code','class'])
for name,group in rez:
    print('\nGroup: ')
    print(name)
    print(group)'''

#Write a Pandas program to split the following given dataframe into groups based on school code and cast grouping as a list.
'''import pandas as pd
pd.set_option('display.max_rows', None)
#pd.set_option('display.max_columns', None)
student_data = pd.DataFrame({
    'school_code': ['s001','s002','s003','s001','s002','s004'],
    'class': ['V', 'V', 'VI', 'VI', 'V', 'VI'],
    'name': ['Alberto Franco','Gino Mcneill','Ryan Parkes', 'Eesha Hinton', 'Gino Mcneill', 'David Parkes'],
    'date_Of_Birth ': ['15/05/2002','17/05/2002','16/02/1999','25/09/1998','11/05/2002','15/09/1997'],
    'age': [12, 12, 13, 13, 14, 12],
    'height': [173, 192, 186, 167, 151, 159],
    'weight': [35, 32, 33, 30, 31, 32],
    'address': ['street1', 'street2', 'street3', 'street1', 'street2', 'street4']},
    index=['S1', 'S2', 'S3', 'S4', 'S5', 'S6'])
#print(student_data) 
rez = student_data.groupby(by='school_code')
print(list(rez))  '''

#Write a Pandas program to split the following given dataframe into groups based on single column and multiple columns.\
#Find the size of the grouped data
'''import pandas as pd
pd.set_option('display.max_rows',None)
#pd.set_option('display.max_columns',None)
data = pd.DataFrame({
    'school_code': ['s001','s002','s003','s001','s002','s004'],
    'class': ['V', 'V', 'VI', 'VI', 'V', 'VI'],
    'name': ['Alberto Franco','Gino Mcneill','Ryan Parkes', 'Eesha Hinton', 'Gino Mcneill', 'David Parkes'],
    'date_Of_Birth ': ['15/05/2002','17/05/2002','16/02/1999','25/09/1998','11/05/2002','15/09/1997'],
    'age': [12, 12, 13, 13, 14, 12],
    'height': [173, 192, 186, 167, 151, 159],
    'weight': [35, 32, 33, 30, 31, 32],
    'address': ['street1', 'street2', 'street3', 'street1', 'street2', 'street4']},
    index=['S1', 'S2', 'S3', 'S4', 'S5', 'S6'])
#print(data)
print('\nsplit the data on school_code wise and group data: ')
rez = data.groupby(by='school_code')
print(rez.size())
print('\nsplit the data on school_code,class and grouped multiple columns: ')
rez2 = data.groupby(by=['school_code','class']).size()
print(rez2)
#rez2 = data.groupby(by=['school_code','class'])
#print(rez2.size()) '''

#Write a Pandas program to split the following given dataframe into groups based on school code and call a specific group with the name of the group
'''import pandas as pd
pd.set_option('display.max_rows', None)
#pd.set_option('display.max_columns', None)
student_data = pd.DataFrame({
    'school_code': ['s001','s002','s003','s001','s002','s004'],
    'class': ['V', 'V', 'VI', 'VI', 'V', 'VI'],
    'name': ['Alberto Franco','Gino Mcneill','Ryan Parkes', 'Eesha Hinton', 'Gino Mcneill', 'David Parkes'],
    'date_Of_Birth ': ['15/05/2002','17/05/2002','16/02/1999','25/09/1998','11/05/2002','15/09/1997'],
    'age': [12, 12, 13, 13, 14, 12],
    'height': [173, 192, 186, 167, 151, 159],
    'weight': [35, 32, 33, 30, 31, 32],
    'address': ['street1', 'street2', 'street3', 'street1', 'street2', 'street4']},
    index=['S1', 'S2', 'S3', 'S4', 'S5', 'S6'])
#print(student_data)  
print('\nsplit the data on school_code: ') 
print('\ncall school_code -s001:')
rez = student_data.groupby(by='school_code')
print(rez.get_group('s001'))
print('\ncall school_code s004: ')
print(rez.get_group('s004'))'''

#Write a Pandas program to split a dataset, group by one column and get mean, min, and max values by group.\n
#Using the following dataset find the mean, min, and max values of purchase amount\
#(purch_amt) group by customer id (customer_id)
'''import pandas as pd
pd.set_option('display.max_rows',None)
pd.set_option('display.max_columns',None)
data = pd.DataFrame({
'ord_no':[70001,70009,70002,70004,70007,70005,70008,70010,70003,70012,70011,70013],
'purch_amt':[150.5,270.65,65.26,110.5,948.5,2400.6,5760,1983.43,2480.4,250.45, 75.29,3045.6],
'ord_date': ['2012-10-05','2012-09-10','2012-10-05','2012-08-17','2012-09-10','2012-07-27','2012-09-10','2012-10-10','2012-10-10','2012-06-27','2012-08-17','2012-04-25'],
'customer_id':[3005,3001,3002,3009,3005,3007,3002,3004,3009,3008,3003,3002],
'salesman_id': [5002,5005,5001,5003,5002,5001,5001,5006,5003,5002,5007,5001]})
#print(data)
print('\nMean, min, and max values of purchase amount (purch_amt) group by customer id  (customer_id)')
rez = data.groupby(by='customer_id').agg({'purch_amt':['mean','min','max']})
print(rez)  '''

#Write a Pandas program to split a dataset to group by two columns and count by each row
'''import pandas as pd
pd.set_option('display.max_rows',None)
pd.set_option('display.max_columns',None)
data = pd.DataFrame({
'ord_no':[70001,70009,70002,70004,70007,70005,70008,70010,70003,70012,70011,70013],
'purch_amt':[150.5,270.65,65.26,110.5,948.5,2400.6,5760,1983.43,2480.4,250.45, 75.29,3045.6],
'ord_date': ['2012-10-05','2012-09-10','2012-10-05','2012-08-17','2012-09-10','2012-07-27','2012-09-10','2012-10-10','2012-10-10','2012-06-27','2012-08-17','2012-04-25'],
'customer_id':[3005,3001,3002,3009,3005,3007,3002,3004,3009,3008,3003,3002],
'salesman_id': [5002,5005,5001,5003,5002,5001,5001,5006,5003,5002,5007,5001]})
#print(data)
print('\ngroup by two columns and count by each row:')
rez = data.groupby(by=['salesman_id','customer_id']).size().reset_index().groupby(['salesman_id','customer_id'])[[0]].max()
print(rez)'''

#Write a Pandas program to split a dataset to group by two columns and then sort the aggregated results within the groups.
#In the following dataset group on 'customer_id','salesman_id' and then sort sum of purch_amt within the groups.
'''import pandas as pd
pd.set_option('display.max_rows',None)
pd.set_option('display.max_columns',None)
data = pd.DataFrame({
'ord_no':[70001,70009,70002,70004,70007,70005,70008,70010,70003,70012,70011,70013],
'purch_amt':[150.5,270.65,65.26,110.5,948.5,2400.6,5760,1983.43,2480.4,250.45, 75.29,3045.6],
'ord_date': ['2012-10-05','2012-09-10','2012-10-05','2012-08-17','2012-09-10','2012-07-27','2012-09-10','2012-10-10','2012-10-10','2012-06-27','2012-08-17','2012-04-25'],
'customer_id':[3001,3001,3005,3001,3005,3001,3005,3001,3005,3001,3005,3005],
'salesman_id': [5002,5005,5001,5003,5002,5001,5001,5006,5003,5002,5007,5001]})
#print(data)
print("\nGroup on 'customer_id', 'salesman_id' and then sort sum of purch_amt within the groups:")
x = data.groupby(by=['customer_id','salesman_id']).agg({'purch_amt':'sum'})
rez = x['purch_amt'].groupby(level=0,group_keys=False)
print(rez.nlargest())  '''

#Write a Pandas program to split the following dataframe into groups based on customer id and create a list of order date for each group.
'''import pandas as pd
pd.set_option("display.max_rows",None)
pd.set_option("display.max_columns",None)
data = pd.DataFrame({
'ord_no':[70001,70009,70002,70004,70007,70005,70008,70010,70003,70012,70011,70013],
'purch_amt':[150.5,270.65,65.26,110.5,948.5,2400.6,5760,1983.43,2480.4,250.45, 75.29,3045.6],
'ord_date': ['2012-10-05','2012-09-10','2012-10-05','2012-08-17','2012-09-10','2012-07-27','2012-09-10','2012-10-10','2012-10-10','2012-06-27','2012-08-17','2012-04-25'],
'customer_id':[3001,3001,3005,3001,3005,3001,3005,3001,3005,3001,3005,3005],
'salesman_id': [5002,5005,5001,5003,5002,5001,5001,5006,5003,5002,5007,5001]})
#print(data)
print("\nGroup on 'customer_id' and display the list of order dates in group wise:")
rez = data.groupby(by='customer_id')['ord_date'].apply(list)
print(rez)'''

#Write a Pandas program to split the following dataframe into groups and calculate monthly purchase amount
'''import pandas as pd
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
df = pd.DataFrame({
'ord_no':[70001,70009,70002,70004,70007,70005,70008,70010,70003,70012,70011,70013],
'purch_amt':[150.5,270.65,65.26,110.5,948.5,2400.6,5760,1983.43,2480.4,250.45, 75.29,3045.6],
'ord_date': ['05-10-2012','09-10-2012','05-10-2012','08-17-2012','10-09-2012','07-27-2012','10-09-2012','10-10-2012','10-10-2012','06-17-2012','07-08-2012','04-25-2012'],
'customer_id':[3001,3001,3005,3001,3005,3001,3005,3001,3005,3001,3005,3005],
'salesman_id': [5002,5005,5001,5003,5002,5001,5001,5006,5003,5002,5007,5001]})
#print(df)
print('\nmonth wise purchase amount: ')  
df['ord_date'] = pd.to_datetime(df['ord_date']) 
rez = df.set_index('ord_date').groupby(pd.Grouper(freq='M')).agg({'purch_amt':'sum'})
print(rez)'''

#Write a Pandas program to split the following dataframe into groups,\
#group by month and year based on order date and find the total purchase amount year wise, month wise
'''import pandas as pd
pd.set_option('display.max_rows',None)
pd.set_option('display.max_columns',None)
df = pd.DataFrame({
'ord_no':[70001,70009,70002,70004,70007,70005,70008,70010,70003,70012,70011,70013],
'purch_amt':[150.5,270.65,65.26,110.5,948.5,2400.6,5760,1983.43,2480.4,250.45, 75.29,3045.6],
'ord_date': ['05-10-2012','09-10-2012','05-10-2013','08-17-2013','10-09-2013','07-27-2014','10-09-2012','10-10-2012','10-10-2012','06-17-2014','07-08-2012','04-25-2012'],
'customer_id':[3001,3001,3005,3001,3005,3001,3005,3001,3005,3001,3005,3005],
'salesman_id': [5002,5005,5001,5003,5002,5001,5001,5006,5003,5002,5007,5001]})
#print(df)
print('\nyear wise,month wise purchase amount: ')
df['ord_date'] = pd.to_datetime(df['ord_date'])
rez = df.groupby([df['ord_date'].dt.year,df['ord_date'].dt.month]).agg({'purch_amt':'sum'})
print(rez)'''

#Write a Pandas program to split the following dataframe into groups\
#based on first column and set other column values into a list of values. 
'''import pandas as pd
df = pd.DataFrame({'X':[10,10,10,20,30,30,10],'Y':[10,15,11,20,21,12,14],'Z':[22,20,18,20,13,10,0]})
#print(df)   
rez = df.groupby('X').agg(lambda x: x.unique().tolist())
print(rez) '''

#Write a Pandas program to split the following dataframe into groups based on all columns\
#and calculate Groupby value counts on the dataframe
'''import pandas as pd
df = pd.DataFrame({'id':[1,2,1,1,2,1,2],'type':[10,15,11,20,21,12,14],\
        'book':['Math','English','Physics','Math','English','Physics','English']})
#print(df)
print('\nresult: ')
rez = df.groupby(by=['id','type','book']).size().unstack(fill_value=0)
print(rez)'''

#Write a Pandas program to split the following dataframe into groups and count unique values of 'value' column
'''import pandas as pd
df = pd.DataFrame({'id':[1,1,2,3,3,4,4,4],'value':['a','a','b',None,'a','a',None,'b']})
#print(df)   
print('\ncount uniqu values: ')
rez2 = df.groupby('value')['id'].nunique()
print(rez2)  '''

#Write a Pandas program to split a given dataframe into groups and list all the keys from the GroupBy object
'''import pandas as pd
pd.set_option('display.max_rows', None)
#pd.set_option('display.max_columns', None)
df = pd.DataFrame({
    'school_code': ['s001','s002','s003','s001','s002','s004'],
    'class': ['V', 'V', 'VI', 'VI', 'V', 'VI'],
    'name': ['Alberto Franco','Gino Mcneill','Ryan Parkes', 'Eesha Hinton', 'Gino Mcneill', 'David Parkes'],
    'date_Of_Birth ': ['15/05/2002','17/05/2002','16/02/1999','25/09/1998','11/05/2002','15/09/1997'],
    'age': [12, 12, 13, 13, 14, 12],
    'height': [173, 192, 186, 167, 151, 159],
    'weight': [35, 32, 33, 30, 31, 32],
    'address': ['street1', 'street2', 'street3', 'street1', 'street2', 'street4']},
    index=['S1', 'S2', 'S3', 'S4', 'S5', 'S6'])
#print(df)   
print('\nlist of all the keys: ')
rez = df.groupby('school_code')
print(rez.groups.keys())  '''

#Write a Pandas program to split a given dataframe into groups and create a new column with count from GroupBy.
'''import pandas as pd
pd.set_option('display.max_rows', None)
df = pd.DataFrame({
'book_name':['Book1','Book2','Book3','Book4','Book1','Book2','Book3','Book5'],
'book_type':['Math','Physics','Computer','Science','Math','Physics','Computer','English'],
'book_id':[1,2,3,4,1,2,3,5]})
#print(df)   
print('\nnew column with count from groupby: ')
rez = df.groupby(['book_name','book_type'])['book_type'].count().reset_index(name='count')
print(rez)'''

#Write a Pandas program to split a given dataframe into groups with bin counts
'''import pandas as pd
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
df = pd.DataFrame({
'ord_no':[70001,70009,70002,70004,70007,70005,70008,70010,70003,70012,70011,70013],
'purch_amt':[150.5,270.65,65.26,110.5,948.5,2400.6,5760,1983.43,2480.4,250.45, 75.29,3045.6],
'customer_id':[3005,3001,3002,3009,3005,3007,3002,3004,3009,3008,3003,3002],
'sales_id':[5002,5003,5004,5003,5002,5001,5005,5007,5008,5004,5005,5001]})
#print(df)   
x = df.groupby(['customer_id',pd.cut(df.sales_id,3)])
rez = x.size().unstack()
print(rez)  '''

#Write a Pandas program to split a given dataframe into groups with multiple aggregations.\
#Split the following given dataframe by school code, class and get mean, min,\
#and max value of height and age for each value of the school.
'''import pandas as pd
pd.set_option('display.max_rows', None)
#pd.set_option('display.max_columns', None)
df = pd.DataFrame({
    'school_code': ['s001','s002','s003','s001','s002','s001'],
    'class': ['V', 'V', 'VI', 'VI', 'V', 'VI'],
    'name': ['Alberto Franco','Gino Mcneill','Ryan Parkes', 'Eesha Hinton', 'Gino Mcneill', 'David Parkes'],
    'date_Of_Birth ': ['15/05/2002','17/05/2002','16/02/1999','25/09/1998','11/05/2002','15/09/1997'],
    'age': [12, 12, 13, 13, 14, 12],
    'height': [173, 192, 186, 167, 151, 159],
    'weight': [35, 32, 33, 30, 31, 32],
    'address': ['street1', 'street2', 'street3', 'street1', 'street2', 'street4']},
    index=['S1', 'S2', 'S3', 'S4', 'S5', 'S6'])
#print(df)     
print('\ngroup by with multiple aggregations: ')
rez = df.groupby(['school_code','class']).agg({'height':['max','mean'],'weight':['sum','min','count']})
print(rez)  '''

#Write a Pandas program to split a given dataframe into groups and display target column as a list of unique values
'''import pandas as pd
df = pd.DataFrame({'id':['A','A','A','A','A','A','B','B','B','B','B'],\
        'type':[1,1,1,1,2,2,1,1,1,2,2],'book':['Math','Math','English','Physics','Math','English','Physics','English','Physics','English','English']})

#print(df)   
print('\nlist all unique values in a group')
rez = df[['id','type','book']].drop_duplicates().groupby(['id','type'])['book'].apply(list).reset_index()
#print(rez)
rez['book'] = rez.apply(lambda x: (','.join([str(i) for i in x['book']])),axis=1)
print(rez)'''

#Write a Pandas program to split the following dataframe into groups and calculate quarterly purchase amount
'''import pandas as pd
pd.set_option('display.max_rows', None)
#pd.set_option('display.max_columns', None)
df = pd.DataFrame({
'ord_no':[70001,70009,70002,70004,70007,70005,70008,70010,70003,70012,70011,70013],
'purch_amt':[150.5,270.65,65.26,110.5,948.5,2400.6,5760,1983.43,2480.4,250.45, 75.29,3045.6],
'ord_date': ['05-10-2012','09-10-2012','05-10-2012','08-17-2012','10-09-2012','07-27-2012','10-09-2012','10-10-2012','10-10-2012','06-17-2012','07-08-2012','04-25-2012'],
'customer_id':[3001,3001,3005,3001,3005,3001,3005,3001,3005,3001,3005,3005],
'salesman_id': [5002,5005,5001,5003,5002,5001,5001,5006,5003,5002,5007,5001]})
#print(df)
print('\nquartly purchase amount: ')   
df['ord_date'] = pd.to_datetime(df['ord_date'])
rez = df.set_index('ord_date').groupby(pd.Grouper(freq='Q')).agg({'purch_amt':'sum'})
print(rez)'''

#Write a Pandas program to split the following dataframe into groups by school code and\
#get mean, min, and max value of age with customized column name for each school.
'''import pandas as pd
pd.set_option('display.max_rows',None)
pd.set_option('display.max_columns',None)
df = pd.DataFrame({
    'school_code': ['s001','s002','s003','s001','s002','s004'],
    'class': ['V', 'V', 'VI', 'VI', 'V', 'VI'],
    'name': ['Alberto Franco','Gino Mcneill','Ryan Parkes', 'Eesha Hinton', 'Gino Mcneill', 'David Parkes'],
    'date_Of_Birth ': ['15/05/2002','17/05/2002','16/02/1999','25/09/1998','11/05/2002','15/09/1997'],
    'age': [12, 12, 13, 13, 14, 12],
    ' height ': [173, 192, 186, 167, 151, 159],
    'weight': [35, 32, 33, 30, 31, 32],
    'address': ['street1', 'street2', 'street3', 'street1', 'street2', 'street4']},
    index=['S1', 'S2', 'S3', 'S4', 'S5', 'S6'])
#print(df)   
rez = df.groupby('school_code').agg(Age_Mean=('age','mean'),Age_Max=('age','max'),Age_Min=('age','min'))
print(rez)  '''

#Write a Pandas program to split the following datasets into groups on customer id and calculate\
#the number of customers starting with 'C', the list of all products \
#and the difference of maximum purchase amount and minimum purchase amount
'''import pandas as pd
pd.set_option('display.max_rows', None)
#pd.set_option('display.max_columns', None)
df = pd.DataFrame({
'ord_no':[70001,70009,70002,70004,70007,70005,70008,70010,70003,70012,70011,70013],
'purch_amt':[150.5, 270.65, 65.26, 110.5, 948.5, 2400.6, 5760, 1983.43, 2480.4, 250.45, 75.29, 3045.6],
'ord_date': ['05-10-2012','09-10-2012','05-10-2012','08-17-2012','10-09-2012','07-27-2012','10-09-2012','10-10-2012','10-10-2012','06-17-2012','07-08-2012','04-25-2012'],
'customer_id':['C3001','C3001','D3005','D3001','C3005','D3001','C3005','D3001','D3005','C3001','D3005','D3005'],
'salesman_id': [5002,5005,5001,5003,5002,5001,5001,5006,5003,5002,5007,5001]})
print("Original Orders DataFrame:")
#print(df)   
def cust_id_with_c(x):
    return (x.str[0]=='C').sum()
rez = df.groupby('salesman_id').agg(cust_with_c=('customer_id',cust_id_with_c),\
        cust_id_list=('customer_id',lambda x: ', '.join(x)),\
        purch_amt_gap=('purch_amt',lambda x: x.max()-x.min()))
#print(rez)  '''

#Write a Pandas program to split the following datasets into groups on customer_id \
#to summarize purch_amt and calculate percentage of purch_amt in each group
'''import pandas as pd
pd.set_option('display.max_rows', None)
#pd.set_option('display.max_columns', None)
df = pd.DataFrame({
'ord_no':[70001,70009,70002,70004,70007,70005,70008,70010,70003,70012,70011,70013],
'purch_amt':[150.5,270.65,65.26,110.5,948.5,2400.6,5760,1983.43,2480.4,250.45, 75.29,3045.6],
'ord_date': ['05-10-2012','09-10-2012','05-10-2012','08-17-2012','10-09-2012','07-27-2012','10-09-2012','10-10-2012','10-10-2012','06-17-2012','07-08-2012','04-25-2012'],
'customer_id':[3001,3001,3005,3001,3005,3001,3005,3001,3005,3001,3005,3005],
'salesman_id': [5002,5005,5001,5003,5002,5001,5001,5006,5003,5002,5007,5001]})
#print(df)   
print('\npercentage of purch_amt in each group of customer_id: ')
rez = df.groupby(by=['customer_id','salesman_id']).agg({'purch_amt':'sum'})
rez['%(Purch Amt.)'] = rez.apply(lambda x: 100*x/x.sum())
print(rez)  '''

#Write a Pandas program to split a dataset, group by one column and get mean, min, and max values by group,\
#also change the column name of the aggregated metric. Using the following dataset find the mean, min,\
#and max values of purchase amount (purch_amt) group by customer id (customer_id)
'''import pandas as pd
pd.set_option('display.max_rows',None)
pd.set_option('display.max_columns',None)
df = pd.DataFrame({
    'school_code': ['s001','s002','s003','s001','s002','s004'],
    'class': ['V', 'V', 'VI', 'VI', 'V', 'VI'],
    'name': ['Alberto Franco','Gino Mcneill','Ryan Parkes', 'Eesha Hinton', 'Gino Mcneill', 'David Parkes'],
    'date_Of_Birth ': ['15/05/2002','17/05/2002','16/02/1999','25/09/1998','11/05/2002','15/09/1997'],
    'age': [12, 12, 13, 13, 14, 12],
    'height': [173, 192, 186, 167, 151, 159],
    'weight': [35, 32, 33, 30, 31, 32],
    'address': ['street1', 'street2', 'street3', 'street1', 'street2', 'street4']},
    index=['S1', 'S2', 'S3', 'S4', 'S5', 'S6'])
#print(df)   
rez = df.groupby('school_code').agg({'age':[('mean_age','mean'),('min_age','min'),('max_age','max')]})
print(rez)  '''

#Write a Pandas program to split a given dataset, group by two columns and convert other columns of the dataframe\
#into a dictionary with column header as key.
'''import pandas as pd
pd.set_option('display.max_rows',None)
pd.set_option('display.max_columns',None)
df = pd.DataFrame({
    'school_code': ['s001','s002','s003','s001','s002','s004'],
    'class': ['V', 'V', 'VI', 'VI', 'V', 'VI'],
    'name': ['Alberto Franco','Gino Mcneill','Ryan Parkes', 'Eesha Hinton', 'Gino Mcneill', 'David Parkes'],
    'date_Of_Birth ': ['15/05/2002','17/05/2002','16/02/1999','25/09/1998','11/05/2002','15/09/1997'],
    'age': [12, 12, 13, 13, 14, 12],
    'height': [173, 192, 186, 167, 151, 159],
    'weight': [35, 32, 33, 30, 31, 32],
    'address': ['street1', 'street2', 'street3', 'street1', 'street2', 'street4']},
    index=['S1', 'S2', 'S3', 'S4', 'S5', 'S6'])
#print(df)   
dict_data_list = list()
for col,row in df.groupby(['school_code','class']):
    group = dict(zip(['school_code','class'],col))
    col_list = list()
    for _,data in row.iterrows():
        data = data.drop(labels=['school_code','class'])
        col_list.append(data.to_dict())
    group['other_columns'] = col_list
    dict_data_list.append(group)
print(dict_data_list)   '''

#Write a Pandas program to split a given dataset, group by one column and apply an aggregate function\
#to few columns and another aggregate function to the rest of the columns of the dataframe.
'''import pandas as pd
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
df = pd.DataFrame({
'salesman_id': [5002,5005,5001,5003,5002,5001,5001,5006,5003,5002,5007,5001],
'sale_jan':[150.5, 270.65, 65.26, 110.5, 948.5, 2400.6, 1760, 2983.43, 480.4,  1250.45, 75.29,1045.6],
'sale_feb':[250.5, 170.65, 15.26, 110.5, 598.5, 1400.6, 2760, 1983.43, 2480.4, 250.45, 75.29, 3045.6],
'sale_mar':[150.5, 270.65, 65.26, 110.5, 948.5, 2400.6, 5760, 1983.43, 2480.4, 250.45, 75.29, 3045.6],
'sale_apr':[150.5, 270.65, 95.26, 210.5, 948.5, 2400.6, 760, 1983.43, 2480.4, 250.45, 75.29, 3045.6],
'sale_may':[130.5, 270.65, 65.26, 310.5, 948.5, 2400.6, 760, 1983.43, 2480.4, 250.45, 75.29, 3045.6],
'sale_jun':[150.5, 270.65, 45.26, 110.5, 948.5, 3400.6, 5760, 983.43, 2480.4, 250.45, 75.29, 3045.6],
'sale_jul':[950.5, 270.65, 65.26, 210.5, 948.5, 2400.6, 5760, 983.43, 2480.4, 250.45, 75.29, 3045.6],
'sale_aug':[150.5, 70.65,  65.26, 110.5, 948.5, 400.6, 5760, 1983.43, 2480.4, 250.45, 75.29, 3045.6],
'sale_sep':[150.5, 270.65, 65.26, 110.5, 948.5, 200.6, 5760, 1983.43, 2480.4, 250.45, 75.29, 3045.6],
'sale_oct':[150.5, 270.65, 65.26, 110.5, 948.5, 2400.6, 5760, 1983.43, 2480.4, 250.45, 75.29, 3045.6],
'sale_nov':[150.5, 270.65, 95.26, 110.5, 948.5, 2400.6, 5760, 1983.43, 2480.4, 250.45, 75.29, 3045.6], 
'sale_dec':[150.5, 70.65, 65.26, 110.5, 948.5, 2400.6, 5760, 1983.43, 2480.4, 250.45, 75.29, 3045.6]
})
print(df)   
rez = df.groupby(by='salesman_id').agg(lambda x: x.sum() if x.name in['sale_jan','sale_feb','sale_mar'] else x.mean())
print(rez)  '''

#Write a Pandas program to split a given dataset, group by one column and remove those groups\
#if all the values of a specific columns are not available
'''import pandas as pd
pd.set_option('display.max_rows',None)
pd.set_option('display.max_columns',None)
df = pd.DataFrame({
    'school_code': ['s001','s002','s003','s001','s002','s004'],
    'class': ['V', 'V', 'VI', 'VI', 'V', 'VI'],
    'name': ['Alberto Franco','Gino Mcneill','Ryan Parkes', 'Eesha Hinton', 'Gino Mcneill', 'David Parkes'],
    'date_Of_Birth ': ['15/05/2002','17/05/2002','16/02/1999','25/09/1998','11/05/2002','15/09/1997'],
    'age': [12, 12, 13, 13, 14, 12],
    'weight': [173, 192, 186, 167, 151, 159],
    'height': [35, None, 33, 30, None, 32]},
    index=['S1', 'S2', 'S3', 'S4', 'S5', 'S6'])
#print(df)   
print('\nGroup by one column and remove those groups if all the values of a specific columns are not available:')
rez = df[(~df['height'].isna()).groupby(df['school_code']).transform('any')]
print(rez)'''

#Write a Pandas program to split a given dataset using group by on specified column into two labels and ranges
'''import pandas as pd
import numpy as np
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
df = pd.DataFrame({
'salesman_id': [5001,5002,5003,5004,5005,5006,5007,5008,5009,5010,5011,5012],
'sale_jan':[150.5, 270.65, 65.26, 110.5, 948.5, 2400.6, 1760, 2983.43, 480.4,  1250.45, 75.29,1045.6]})
#print(df)   
rez = df.groupby(pd.cut(df['salesman_id'],bins=(0,5006,np.inf),labels=['S1','S2']))['sale_jan'].sum().reset_index()
print(rez) '''

#Write a Pandas program to split the following dataset using group by on first column\
#and aggregate over multiple lists on second column.
'''import pandas as pd
import numpy as np
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
df = pd.DataFrame({
    'student_id': ['S001','S001','S002','S002','S003','S003'],
    'marks': [[88,89,90],[78,81,60],[84,83,91],[84,88,91],[90,89,92],[88,59,90]]})
#print(df)   
rez = df.set_index('student_id')['marks'].groupby('student_id').apply(list).apply(lambda x: np.mean(x,0))
print(rez)  '''

#Write a Pandas program to split the following dataset using group by on 'salesman_id' and find the first order date for each group
'''import pandas as pd
pd.set_option('display.max_rows', None)
#pd.set_option('display.max_columns', None)
df = pd.DataFrame({
'ord_no':[70001,70009,70002,70004,70007,70005,70008,70010,70003,70012,70011,70013],
'purch_amt':[150.5,270.65,65.26,110.5,948.5,2400.6,5760,1983.43,2480.4,250.45, 75.29,3045.6],
'ord_date': ['2012-10-05','2012-09-10','2012-10-05','2012-08-17','2012-09-10','2012-07-27','2012-09-10','2012-10-10','2012-10-10','2012-06-27','2012-08-17','2012-04-25'],
'customer_id':[3005,3001,3002,3009,3005,3007,3002,3004,3009,3008,3003,3002],
'salesman_id': [5002,5005,5001,5003,5002,5001,5001,5004,5003,5002,5004,5001]})
#print(df)   
r = df.groupby('salesman_id')['ord_date'].min()
print(r)'''

#Write a Pandas program to split a given dataset using group by on multiple columns and drop last n rows of from each group.
'''import pandas as pd
pd.set_option('display.max_rows',None)
pd.set_option('display.max_columns',None)
df = pd.DataFrame({
'ord_no':[70001,70009,70002,70004,70007,70005,70008,70010,70003,70012,70011,70013],
'purch_amt':[150.5,270.65,65.26,110.5,948.5,2400.6,5760,1983.43,2480.4,250.45, 75.29,3045.6],
'ord_date': ['2012-10-05','2012-09-10','2012-10-05','2012-08-17','2012-09-10','2012-07-27','2012-09-10','2012-10-10','2012-10-10','2012-06-27','2012-08-17','2012-04-25'],
'customer_id':[3002,3001,3001,3003,3002,3002,3001,3004,3003,3002,3003,3001],
'salesman_id':[5002,5003,5001,5003,5002,5001,5001,5003,5003,5002,5003,5001]})
#print(df)  
print('\nsplit the data on salesman_id,customer_id wise:') 
rez = df.groupby(['salesman_id','customer_id'])
for name,group in rez:
    print('\ngroup: ')
    print(name)
    print(group)
print('\ndroping last two records: ')
n = 2
last_two = df.drop(df.groupby(['salesman_id','customer_id']).tail(n).index,axis=0)
print(last_two)'''

