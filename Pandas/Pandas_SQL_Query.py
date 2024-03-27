#pandas sql query exercises at w3resource.com

#Write a Pandas program to display all the records of REGIONS file
'''import pandas as pd
df = pd.read_csv('REGIONS.csv')
print(df)'''

#Write a Pandas program to display all the location id from locations file.
'''import pandas as pd
df = pd.read_csv('LOCATIONS.csv')
#print(df.head())
print('\nall locations id from lacations file: ')
print(df[['location_id']])'''

#Write a Pandas program to extract first 7 records from employees file.
'''import pandas as pd
df = pd.read_csv('EMPLOYEES.csv')
print(df.head(7))
print(df.head(7).shape)'''

#Write a Pandas program to select distinct department id from employees file
'''import pandas as pd
df = pd.read_csv('EMPLOYEES.csv')
#print(df.head())
df = df['department_id'].unique()
print(df)'''

#Write a Pandas program to display the first and last name, and department number for all employees\
#whose last name is "McEwen".
'''import pandas as pd
df = pd.read_csv('EMPLOYEES.csv')
#print(df.head())
dept_df = pd.read_csv('DEPARTMENTS.csv')
#print(dept_df)
rez = df[['first_name','last_name','department_id']].query("last_name == 'McEwen'")
print(rez)  
#for index,row in rez.iterrows():
    #print(row['last_name'],'    ',row['first_name'],'    ',row['department_id'] )'''

#Write a Pandas program to display the first, last name, salary and department number for those employees\
#whose first name starts with the letter 'S'    
'''import pandas as pd
df = pd.read_csv('EMPLOYEES.csv')
#print(df.head())
print('first_name    last_name    salary     department_id')
result = df[df['first_name'].str[:1]=='S']
for index, row in result.iterrows():
    print(row['first_name'].ljust(15),row['last_name'].ljust(15),str(row['salary']).ljust(9),row['department_id'])'''

#Write a Pandas program to display the first, last name, salary and department number for those employees\
#whose first name does not contain the letter 'M'.    
'''import pandas as pd
df = pd.read_csv('EMPLOYEES.csv')
#print(df.head())
print('last_name    first_name    salary    department_id')
#rez = df[df['first_name'].str[:1]!='M']
rez = df[df['first_name'].str.find('M')==-1]
for index,row in rez.iterrows():
    print(row['last_name'].ljust(15),row['first_name'].ljust(15),str(row['salary']).ljust(9),row['department_id'])'''

#Write a Pandas program to display the first name, last name, salary and department number in ascending\
#order by department number
'''import pandas as pd
df = pd.read_csv('EMPLOYEES.csv')
#print(df.head())
print('first_name\tlast_name\tsalary\tdepartment_id')
rez = df.sort_values(by='department_id',ascending=True)
for index,row in rez.iterrows():
    print(row['first_name'].ljust(15),row['last_name'].ljust(15),str(row['salary']).ljust(9),row['department_id'])'''

#Write a Pandas program to display the first name, last name, salary and department number in descending order\
#by first name    
'''import pandas as pd
df = pd.read_csv('EMPLOYEES.csv')
#print(df.head())
print('first name\tlast name\tsalary\tdepartment id')
rez = df.sort_values(by='first_name',ascending=False)
for index,row in rez.iterrows():
    print(row['first_name'].ljust(15),row['last_name'].ljust(15),str(row['salary']).ljust(9),row['department_id'])'''

#Write a Pandas program to display the first name, last name, salary and manger id where manager ids are null.
'''import pandas as pd
df = pd.read_csv('EMPLOYEES.csv')
#print(df.head())    
print('first name\tlast name\tsalary\tmanager id')
rez = df[df['manager_id'].isnull()]
for index,row in rez.iterrows():
    print(row['first_name'].ljust(15),row['last_name'].ljust(15),str(row['salary']).ljust(9),row['manager_id'])'''

#Write a Pandas program to display the first name, last name, salary and manger id where manager ids are not null
'''import pandas as pd
df = pd.read_csv('EMPLOYEES.csv')
#print(df.head())
print('first_name\tlast_name\tsalary\tmanager_id')
rez = df[df['manager_id'].notnull()]
for index,row in rez.iterrows():
    print(row['first_name'].ljust(15),row['last_name'].ljust(15),str(row['salary']).ljust(9),row['manager_id'])'''

#Write a Pandas program to create and display a boolean series, where True for not null and False\
#for null values or missing values in state_province column of locations file
'''import pandas as pd
pd.set_option('display.max_rows',500)
pd.set_option('display.max_columns',500)
df = pd.read_csv('LOCATIONS.csv')
#print(df.head())
print('original data / state province')
#print(df['state_province'])
print('state province(Not null/ Null Series)')
rez = df['state_province'].notnull()
print(rez)  '''

#Write a Pandas program to create a boolean series selecting rows with one or more nulls from locations file.
'''import pandas as pd
df = pd.read_csv('LOCATIONS.csv')
#print(df.head())
rez = df.iloc[:,:].isnull()
print(rez)  
#rez2 = df.isnull()
#print(rez2) '''

#Write a Pandas program to count the NaN values of all the columns of locations file
'''import pandas as pd
pd.set_option('display.max_rows',500)
pd.set_option('display.max_columns',500)
df = pd.read_csv('LOCATIONS.csv')
#print(df.head())
print('\nNaN values of all the columns of loc file')
rez = df.iloc[:,:].isnull()
print(rez.sum())  '''

#Write a Pandas program to display the first name, last name, salary and department number for those employees\
#whose first name ends with the letter 'm'.
'''import pandas as pd
df = pd.read_csv('EMPLOYEES.csv')
#print(df.head())
print('first_name\tlast_name\tsalary\tdepartment_id')
rez = df[df['first_name'].str.endswith('m')]
for index,row in rez.iterrows():
    print(row['first_name'].ljust(15),row['last_name'].ljust(15),str(row['salary']).ljust(9),row['department_id'])'''

#Write a Pandas program to display the first name, last name, salary and department number for those employees\
#whose first name ends with the letter 'd' or 'n' or 's' and also arrange the result in descending order by department id    
'''import pandas as pd
df = pd.read_csv('EMPLOYEES.csv')
#print(df.head())
print('first_name\tlast_name\tsalary\tdepartment_id')
data = df[df['first_name'].str.endswith(('d','n','s'))]
#data = df[df['first_name'].str[-1].isin(['d','n','s'])]
rez = data.sort_values(by='department_id',ascending=True)
for index,row in rez.iterrows():
    print(row['first_name'].ljust(15),row['last_name'].ljust(15),str(row['salary']).ljust(9),row['department_id'])'''

# Write a Pandas program to display the first name, last name, salary and department number\
#for employees who works either in department 70 or 90    
'''import pandas  as pd
df = pd.read_csv('EMPLOYEES.csv')
#print(df.head())
print('first_name\tlast_name\tsalary\tdepartment_id')
rez = df[df['department_id'].isin([70,90])]
for index,row in rez.iterrows():
    print(row['first_name'].ljust(15),row['last_name'].ljust(15),str(row['salary']).ljust(9),row['department_id'])'''

#Write a Pandas program to display the first name, last name, salary and department number for those\
#employees whose managers are hold the ID 120, 103 or 145    
'''import pandas as pd
df = pd.read_csv('EMPLOYEES.csv')
#print(df.head())
print("first_name\tlast_name\tsalary\tmanager_id")
rez = df[df['manager_id'].isin([120,103,145])]
for index,row in rez.iterrows():
    print(row['first_name'].ljust(15),row['last_name'].ljust(15),str(row['salary']).ljust(9),row['manager_id'])'''

#Write a Pandas program to display the first, last name, salary and department number for those employees\
#who holds a letter n as a 3rd character in their first name.    
'''import pandas as pd
df = pd.read_csv('EMPLOYEES.csv')
#print(df.head())
print("first_name\tlast_name\tsalary\tdepartment_id")
rez = df[df['first_name'].str[2:3] == 'n']
for index,row in rez.iterrows():
    print(row['first_name'].ljust(15),row['last_name'].ljust(15),str(row['salary']).ljust(9),row['department_id'])'''

#Write a Pandas program to display the first name, job id, salary and department for those employees\
#not working in the departments 50,30 and 80.    
'''import pandas as pd
df = pd.read_csv('EMPLOYEES.csv')
#print(df.head())
print("first_name\tjob_id\tsalary\tdepartment_id")
rez = df[~df['department_id'].isin([50,30,80])]
for index,row in rez.iterrows():
    print(row['first_name'].ljust(15),row['job_id'].ljust(15),str(row['salary']).ljust(9),row['department_id'])'''

#Write a Pandas program to display the ID for those employees who did two or more jobs in the past
'''import pandas as pd
df = pd.read_csv('JOB_HISTORY.csv')
#print(df.head())    
rez = df.groupby(['employee_id'])
print(rez.filter(lambda x: len(x)>1).groupby('employee_id').size().sort_values(ascending=False))'''

#Write a Pandas program to calculate minimum, maximum and mean salary from employees file.
'''import pandas as pd
df = pd.read_csv('EMPLOYEES.csv')
#print(df.head())
rez = df.groupby(['employ_id'])
print(df.agg({'salary':['min','max','mean','median']}))'''

#Write a Pandas program to display the details of jobs in descending sequence on job title
'''import pandas as pd
df = pd.read_csv('JOBS.csv')
#print(df.head())
print('job_id\t\tJOB ID\t\t\t\tmin_salary max_salary')
rez = df.sort_values('job_title')
for index,row in rez.iterrows():
    print(row['job_id'].ljust(15),row['job_title'].ljust(35),str(row['min_salary']).ljust(9),row['max_salary'])'''

#Write a Pandas program to display the first and last name and date of joining of the employees\
#who is either Sales Representative or Sales Man    
'''import pandas as pd
df = pd.read_csv('EMPLOYEES.csv')
#print(df.head())
print('first name\tlast name\tjob id\thire date')
rez = df[df['job_id'].isin(['SA_REP','SA_MAN'])]
for index,row in rez.iterrows():
    print(row['first_name'].ljust(15),row['last_name'].ljust(15),str(row['job_id']).ljust(9),str(row['hire_date']).ljust(10))'''


