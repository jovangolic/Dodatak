#Pandas DataFrame exercises at w3resource.com
#Write a Pandas program to get the powers of an array values element-wise.
'''import pandas as pd
df = pd.DataFrame({'X':[78,85,96,80,86],'Y':[84,94,89,83,86],'Z':[86,97,96,72,83]})
print(df)'''

#Write a Pandas program to create and display a DataFrame from a specified dictionary data which has the index labels.
'''import pandas as pd
import numpy as np
exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
df = pd.DataFrame(exam_data,index=labels)
print(df)'''

#Write a Pandas program to display a summary of the basic information about a specified DataFrame and its data.
'''import numpy as np
import pandas as pd
exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
df = pd.DataFrame(exam_data,labels)
print(df)
print(df.info())'''

#Write a Pandas program to get the first 3 rows of a given DataFrame
'''import numpy as np
import pandas as pd
exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
df = pd.DataFrame(exam_data,index=labels)
#print(df.head(3))
print(df.iloc[:3])'''

#Write a Pandas program to select the 'name' and 'score' columns from the following DataFrame
'''import numpy as np
import pandas as pd
exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
df = pd.DataFrame(exam_data,index=labels)
#print(df)
print(df[['name','score']])'''

#Write a Pandas program to select the specified columns and rows from a given data frame.
'''import pandas as pd
import numpy as np
exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
df = pd.DataFrame(exam_data,index=labels)
#print(df)
print(df.iloc[[1,3,5,6],[1,3]])'''

#Write a Pandas program to select the rows where the number of attempts in the examination is greater than 2.
'''import pandas as pd
import numpy as np
exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
df = pd.DataFrame(exam_data,index=labels)
#print(df)
filt = df['attempts'] > 2
print(df[filt])'''

#Write a Pandas program to count the number of rows and columns of a DataFrame
'''import pandas as pd
import numpy as np
exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
df = pd.DataFrame(exam_data,index=labels)
#print(df)
rows = len(df.axes[0])
columns = len(df.axes[1])
print('number of rows',rows)
print('number of columns: ',columns)'''

#Write a Pandas program to select the rows where the score is missing, i.e. is NaN.
'''import pandas as pd
import numpy as np
exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
df = pd.DataFrame(exam_data,index=labels)
#print(df)
filt = df['score'].isna()
#print(df[filt])
filt2 = df['score'].isnull()
print(df[filt2])'''

#Write a Pandas program to select the rows the score is between 15 and 20 (inclusive)
'''import pandas as pd
import numpy as np
exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
df = pd.DataFrame(exam_data,index=labels)
#print(df)
filt = (df['score'] >15) & (df['score']<=20)
print(df[filt])'''

#Write a Pandas program to select the rows where number of attempts in the examination is less than 2 and score greater than 15
'''import pandas as pd
import numpy as np
exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
df = pd.DataFrame(exam_data,index=labels)
#print(df)
filt = (df['attempts'] < 2) & (df['score']> 15)
print(df[filt])'''

#Write a Pandas program to change the score in row 'd' to 11.5.
'''import pandas as pd
import numpy as np
exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
df = pd.DataFrame(exam_data,index=labels)
#print(df.head(5))
df.loc['d','score'] = 11.5
print(df)'''

#Write a Pandas program to calculate the sum of the examination attempts by the students.
'''import numpy as np
import pandas as pd
exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
df = pd.DataFrame(exam_data,index=labels)
#print(df)
#print(df['attempts'].sum())
suma = (df['attempts'].sum())
print('sum of the examination attempts by the students: ')
print(suma)'''

#Write a Pandas program to calculate the mean score for each different student in DataFrame
'''import pandas as pd; import numpy as np
exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
df = pd.DataFrame(exam_data,index=labels)
#print(df)
score = df['score'].mean()
print(score)'''

#Write a Pandas program to append a new row 'k' to data frame with given values for each column.\
#  Now delete the new row and return the original DataFrame
'''import pandas as pd; import numpy as np
exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
df = pd.DataFrame(exam_data,index=labels)
#print(df.head())
df.loc['k'] = ['Suresh',15.5,1,'yes']
#print('new record added: ')
#print(df)
df = df.drop('k')
print('deleted new row and displayed the original rows: ')
print(df)'''

#Write a Pandas program to sort the DataFrame first by 'name' in descending order, then by 'score' in ascending order. 
'''import pandas as pd; import numpy as np
exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
df = pd.DataFrame(exam_data,index=labels)
#print(df)
df.sort_values(by=['name','score'],ascending=[False,True])
print(df)'''

#Write a Pandas program to replace the 'qualify' column contains the values 'yes' and 'no' with True and False
'''import pandas as pd; import numpy as np
exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
df = pd.DataFrame(exam_data,index=labels)
#print(df)
#df['qualify'] = df['qualify'].replace({'yes':True,'no':False})
df['qualify'] = df['qualify'].map({'yes':True,'no':False})
print(df)'''

#Write a Pandas program to change the name 'James' to 'Suresh' in name column of the DataFrame
'''import pandas as pd; import numpy as np
exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
df = pd.DataFrame(exam_data,index=labels)
#print(df)
df['name'] = df['name'].replace({'James':'Suresh'})
print(df)'''

#Write a Pandas program to delete the 'attempts' column from the DataFrame. 
'''import pandas as pd; import numpy as np
exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
df = pd.DataFrame(exam_data,index=labels)
print(df)
remv = df.drop(columns=['attempts'])
print('deleted column attempts from the data frame: ')
print(remv)'''

#Write a Pandas program to insert a new column in existing DataFrame.
'''import pandas as pd; import numpy as np
exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
df = pd.DataFrame(exam_data,index=labels)
#print(df)
color = ['Red','Blue','Orange','Red','White','White','Blue','Green','Green','Red']
df.insert(4,column='color',value=color)
#df['color'] = color
print('new column inserted into dataFrame: ')
print(df)'''

#Write a Pandas program to iterate over rows in a DataFrame
'''import pandas as pd
#import numpy as np
exam_data = [{'name':'Anastasia', 'score':12.5}, {'name':'Dima','score':9}, {'name':'Katherine','score':16.5}]
df = pd.DataFrame(exam_data)
#print(df)
for index,row in df.iterrows():
    print(row['name'],row['score'])'''

#Write a Pandas program to get list from DataFrame column headers.
'''import pandas as pd
import numpy as np
exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
df = pd.DataFrame(exam_data,index=labels) 
#print(df)
print(list(df.head(0)))
lst = list(df.columns.values)
print(lst)'''

#Write a Pandas program to rename columns of a given DataFrame
'''import pandas as pd
data = {'col1':[1,2,3],'col2':[4,5,6],'col3':[7,8,9]}
df = pd.DataFrame(data)
print(df)
new_names = df.rename(columns={'col1':'Column1','col2':'Column2','col3':'Column3'})
print(new_names)'''

#Write a Pandas program to select rows from a given DataFrame based on values in some columns
'''import pandas as pd
data = {'col1':[1,4,3,4,5],'col2':[4,5,6,7,8],'col3':[7,8,9,0,1]}
df = pd.DataFrame(data)
#print(df)
print('rows for column1 value == 4')
filt = df['col1'] == 4
print(df[filt])
#print(df.loc[df['col1'] == 4])'''

#Write a Pandas program to change the order of a DataFrame columns.
'''import pandas as pd
data = {'col1':[1,4,3,4,5],'col2':[4,5,6,7,8],'col3':[7,8,9,0,1]}
df = pd.DataFrame(data)
#print(df)
print('after altering col1 and col3: ')
print(df[['col3','col2','col1']])'''

#Write a Pandas program to add one row in an existing DataFrame.
'''import pandas as pd
data = {'col1':[1,4,3,4,5],'col2':[4,5,6,7,8],'col3':[7,8,9,0,1]}
df = pd.DataFrame(data)
#print(df)
d2 = {'col1':10,'col2':11,'col3':12}
new_row = df.append(d2,ignore_index=True)
print(new_row)'''

#Write a Pandas program to write a DataFrame to CSV file using tab separator.
'''import pandas as pd
d1 = {'col1':[1,4,3,4,5],'col2':[4,5,6,7,8],'col3':[7,8,9,0,1]}
df = pd.DataFrame(d1)
print(df)
data = df.to_csv('new_file.csv',sep='\t',index=False)
#print(data)
read_data = pd.read_csv('new_file.csv')
print(read_data)'''

#Write a Pandas program to count city wise number of people from a given of data set (city, name of the person).
'''import pandas as pd
df1 = pd.DataFrame({'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
'city': ['California', 'Los Angeles', 'California', 'California', 'California', 'Los Angeles', 'Los Angeles', 'Georgia', 'Georgia', 'Los Angeles']})
df = pd.DataFrame(df1)
print(df)
group = df.groupby(['city']).size().reset_index(name='num of people')
print(group)'''

#Write a Pandas program to delete DataFrame row(s) based on given column value
'''import pandas as pd
d1 = {'col1':[1,4,3,4,5],'col2':[4,5,6,7,8],'col3':[7,8,9,0,1]}
df = pd.DataFrame(d1)
#print(df)
df = df.drop([1])
print(df)'''

#Write a Pandas program to widen output display to see more columns.
'''import pandas as pd
d1 = {'col1':[1,4,3,4,5],'col2':[4,5,6,7,8],'col3':[7,8,9,0,1]}
df = pd.DataFrame(d1)
#print(df)
pd.set_option('display.max_rows',500)
pd.set_option('display.max_columns',500)
pd.set_option('display.width',1000)
print(df)'''

#Write a Pandas program to select a row of series/dataframe by given integer index
'''import pandas as pd
d1 = {'col1':[1,4,3,4,5],'col2':[4,5,6,7,8],'col3':[7,8,9,0,1]}
df = pd.DataFrame(d1)
#print(df)
idx = df.iloc[[2]]
print('index-2: Details')
print(idx)'''

#Write a Pandas program to replace all the NaN values with Zero's in a column of a dataframe
'''import pandas as pd
import numpy as np
exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
        'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
        'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
        'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
df = pd.DataFrame(exam_data)
#print(df)
df =df.fillna(0)
print(df)'''

#Write a Pandas program to convert index in a column of the given dataframe.
'''import pandas as pd
import numpy as np
exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
        'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
        'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
        'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
df = pd.DataFrame(exam_data)
#print(df)    
df.reset_index(level=0,inplace=True)   
print(df)   
print('\nhiding index: ')
print(df.to_string(index=False))'''

#Write a Pandas program to set a given value for particular cell in  DataFrame using index value.
'''import pandas as pd
import numpy as np
exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
        'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
        'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
        'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
df = pd.DataFrame(exam_data)
#print(df)           
df.loc[[8],['score']] = 10.2
print(df)'''

#Write a Pandas program to count the NaN values in one or more columns in DataFrame
'''import pandas as pd
import numpy as np
exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
        'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
        'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
        'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
df = pd.DataFrame(exam_data) 
#print(df)   
counts = df.isnull().values.sum()
print(counts)'''

#Write a Pandas program to drop a list of rows from a specified DataFrame
'''import pandas as pd
data = {'col':[1,4,3,4,5],'col2':[4,5,6,7,8],'col3':[7,8,9,0,1]}
df = pd.DataFrame(data)
print(df)   
rez = df.drop([2,4])
print(rez) '''

#Write a Pandas program to reset index in a given DataFrame
'''import pandas as pd
import numpy as np
exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
        'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
        'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
        'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
df = pd.DataFrame(exam_data)
#print(df)       
df = df.drop([0,1])
print('after removing first and second rows: ')
#print(df)       
print('reset the index: ')
df = df.reset_index()
print(df) '''

#Write a Pandas program to divide a DataFrame in a given ratio
'''import pandas as pd
import numpy as np
df = pd.DataFrame(np.random.randn(10, 2))
print("Original DataFrame:")
print(df)  
part_70 = df.sample(frac=0.7,random_state=10)
part_30 = df.drop(part_70.index)
print('\n70% of the said dataframe: ')
print(part_70)
print('\n30% of the said dataframe: ')     
print(part_30)  '''

#Write a Pandas program to combining two series into a DataFrame
'''import pandas as pd
d1 = ['100','200','python','300.12','400']
d2 = ['10','20','php','30.12','40']
s = pd.Series(d1)
s2 = pd.Series(d2)
#print(s)        
#print(s2)               
print('new dataFrame combinig by two series: ')
comb = pd.concat([s,s2],names=[0,1],axis=1)        
print(comb)'''

#Write a Pandas program to shuffle a given DataFrame rows.
'''import pandas as pd; import numpy as np
exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
        'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
        'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
        'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
df = pd.DataFrame(exam_data)    
#print(df)               
df = df.sample(frac=1)           
print('new dataFrame: ')
print(df)'''

#Write a Pandas program to convert DataFrame column type from string to datetime
'''import pandas as pd
s = pd.Series(['3/11/2000', '3/12/2000', '3/13/2000'])
print(s)        
df = pd.DataFrame(pd.to_datetime(s))    
print(df)  '''

#Write a Pandas program to rename a specific column name in a given DataFrame
'''import pandas as pd
d = {'col1':[1,2,3],'col2':[4,5,6],'col3':[7,8,9]}
df = pd.DataFrame(d)    
#print(df)       
print('renaming second column: ')
df = df.rename(columns={'col2':'Column2'})
print(df)  '''

#Write a Pandas program to get a list of a specified column of a DataFrame
'''import pandas as pd
d = {'col1':[1,2,3],'col2':[4,5,6],'col3':[7,8,9]}
df = pd.DataFrame(d)    
#print(df)       
print('col2 of the dataFrame to list: ')
df = df['col2'].tolist()
print(df) '''

#Write a Pandas program to create a DataFrame from a Numpy array and specify the index column and column headers.
'''import pandas as pd
import numpy as np
dtype = [('Column1','int32'), ('Column2','float32'), ('Column3','float32')]
vals = np.zeros(15,dtype=dtype)
idx = ['Index'+str(i) for i in range(1,len(vals)+1)]
df = pd.DataFrame(np.array(vals),index=idx) 
print(df)'''

#Write a Pandas program to find the row for where the value of a given column is maximum
'''import pandas as pd
d = {'col1':[1,2,3,4,7],'col2':[4,5,6,9,5],'col3':[7,8,12,1,11]}
df = pd.DataFrame(d)    
#print(df)          
print('row where col1 has max value: ')
x1 = df['col1'].argmax()      
print(x1)
print('row where col2 has max value: ')
x2 = df['col2'].argmax()
print(x2)
print('row where col3 has max value: ')
x3 = df['col3'].argmax()
print(x3)   '''

#Write a Pandas program to check whether a given column is present in a DataFrame or not
'''import pandas as pd
d = {'col1':[1,2,3,4,7],'col2':[4,5,6,9,5],'':[7,8,12,1,11]}
df = pd.DataFrame(d)    
#print(df)       
x = df.columns
if 'col4' in x:
        print('col4 is presented')
else:
        print('col4 is not presented')        
if 'col1' in x:
        print('col1 is presented')
else:
        print('col1 is not presented')  '''

#Write a Pandas program to get the specified row value of a given DataFrame
'''import pandas as pd
d = {'col1':[1,2,3,4,7],'col2':[4,5,6,9,5],'col3':[7,8,12,1,11]}
df = pd.DataFrame(d)
#print(df)                       
print('value of row1: ')
print(df.iloc[0])       
print('value of row4: ')
print(df.iloc[3]) '''

#Write a Pandas program to get the datatypes of columns of a DataFrame
'''import pandas as pd
import numpy as np
exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
        'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
        'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
        'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
df = pd.DataFrame(exam_data)    
#print(df)              
print(df.dtypes)'''

# Write a Pandas program to append data to an empty DataFrame.
'''import pandas as pd
df = pd.DataFrame()
print(df)       
data = pd.DataFrame({'col1':[0,1,2],'col2':[0,1,2]})
df = df.append(data)
print(df)  '''

#Write a Pandas program to sort a given DataFrame by two or more columns
'''import pandas as pd
import numpy as np
exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
        'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
        'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
        'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
df = pd.DataFrame(exam_data)
#print(df)               
df = df.sort_values(by=['attempts','name'],ascending=[True,True])
print(df)  '''

#Write a Pandas program to convert the datatype of a given column (floats to ints).
'''import pandas as pd
import numpy as np
exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
        'score': [12.5, 9.1, 16.5, 12.77, 9.21, 20.22, 14.5, 11.34, 8.8, 19.13],
        'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
        'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
df = pd.DataFrame(exam_data)    
#print(df.dtypes)               
df['score'] = df['score'].astype(int)
#df.score = df.score.astype(int)
print(df.dtypes)  '''

#Write a Pandas program to remove infinite values from a given DataFrame.
'''import pandas as pd
import numpy as np
df = pd.DataFrame([1000, 2000, 3000, -4000, np.inf, -np.inf])
#print(df)       
df = df.replace([np.inf,-np.inf],np.NaN) 
print(df)  '''

#Write a Pandas program to insert a given column at a specific column index in a DataFrame
'''import pandas as pd
d = {'col2':[4,5,6,9,5],'col3':[7,8,12,1,11]}
df = pd.DataFrame(d)    
#print(df)       
d1 = [1,2,3,4,7]
idx = 0
df.insert(loc=idx,column='col1',value=d1)
print(df)  '''

#Write a Pandas program to convert a given list of lists into a Dataframe.
'''import pandas as pd
lst = [['col1', 'col2'], [2, 4], [1, 3]]
headers = lst.pop(0)
#print(headers)              
df = pd.DataFrame(lst,columns=headers)
print(df) '''

#Write a Pandas program to group by the first column and get second column as lists in rows
'''import pandas as pd
df = pd.DataFrame( {'col1':['C1','C1','C2','C2','C2','C3','C2'], 'col2':[1,2,3,3,4,6,5]})
#print(df)       
print('group on the col1: ')
df = df.groupby('col1')['col2'].apply(list)
print(df) '''

#Write a Pandas program to get column index from column name of a given DataFrame
'''import pandas as pd
d = {'col1':[1,2,3,4,7],'col2':[4,5,6,9,5],'col3':[7,8,12,1,11]}
df = pd.DataFrame(d)
#print(df)       
print('index of col2 :')
df = df.columns.get_loc('col2') 
print(df) '''

#Write a Pandas program to count number of columns of a DataFrame
'''import pandas as pd
d = {'col1':[1,2,3,4,7],'col2':[4,5,6,9,5],'col3':[7,8,12,1,11]}
df = pd.DataFrame(d)    
#print(df)               
print('number of columns: ')
df = df.columns
print(len(df))   '''

#Write a Pandas program to select all columns, except one given column in a DataFrame.
'''import pandas as pd
d = {'col1':[1,2,3,4,7],'col2':[4,5,6,9,5],'col3':[7,8,12,1,11]}
df = pd.DataFrame(d)
#print(df)  
print('all columns except col3: ')     
#df = df[['col1','col2']] 
df = df.loc[:,df.columns != 'col3']
print(df)   '''

#Write a Pandas program to get first n records of a DataFrame
'''import pandas as pd
d = {'col1':[1,2,3,4,11],'col2':[4,5,6,9,0],'col3':[7,5,12,1,11]}
df = pd.DataFrame(d)
#print(df) 
#df = df.loc[:2]
df = df.head(3)
print('first 3 row of the DataFrame: ')
print(df) '''

#Write a Pandas program to get last n records of a DataFrame
'''import pandas as pd
d = {'col1':[1,2,3,4,7,11],'col2':[4,5,6,9,5,0],'col3':[7,5,8,12,1,11]}
df = pd.DataFrame(d)    
#print(df)       
df = df.tail(3)
print('last 3 rows of the DataFrame: ')
print(df)'''

#Write a Pandas program to get topmost n records within each group of a DataFrame
'''import pandas as pd
d = {'col1':[1,2,3,4,7,11],'col2':[4,5,6,9,5,0],'col3':[7,5,8,12,1,11]}
df = pd.DataFrame(d)    
#print(df)       
df1 = df.nlargest(3,['col1'])
print(df1)       
df2 = df.nlargest(3,['col2'])
print(df2)      
df3 = df.nlargest(3,['col3'])
print(df3)  '''

#Write a Pandas program to remove first n rows of a given DataFrame
'''import pandas as pd
import numpy as np
d = {'col1':[1,2,3,4,7,11],'col2':[4,5,6,9,5,0],'col3':[7,5,8,12,1,11]}
df = pd.DataFrame(d)  
#print(df) 
df = df.drop(np.arange(3))
#df = df.iloc[3:]
print('after removing first 3 rows from dataFrame: ') 
print(df) '''

#Write a Pandas program to remove last n rows of a given DataFrame
'''import pandas as pd
d = {'col1':[1,2,3,4,7,11],'col2':[4,5,6,9,5,0],'col3':[7,5,8,12,1,11]}
df = pd.DataFrame(d) 
#print(df)       
df = df.iloc[:3]
print('after removing last 3 rows from dataframe: ')
print(df) '''

#Write a Pandas program to add a prefix or suffix to all columns of a given DataFrame
'''import pandas as pd
df = pd.DataFrame({'W':[68,75,86,80,66],'X':[78,85,96,80,86], 'Y':[84,94,89,83,86],'Z':[86,97,96,72,83]})
#print(df)       
df_prefix = df.add_prefix('A_')
print('add prefix: ')
print(df_prefix)
df_sufix = df.add_suffix('_1')
print('add suffix:')
print(df_sufix)'''

#Write a Pandas program to reverse order (rows, columns) of a given DataFrame
'''import pandas as pd
d = {'W':[68,75,86,80,66],'X':[78,85,96,80,86], 'Y':[84,94,89,83,86],'Z':[86,97,96,72,83]}
df = pd.DataFrame(d)    
#print(df)       
print('reverse column order: ')
df1 = df.iloc[:,::-1]
print(df1)   
print('reverse row order: ')
df2 = df.iloc[::-1]
print(df2) 
print('reverse row order and reset index: ')
df3 = df.iloc[::-1].reset_index(drop=True)
print(df3) '''

#Write a Pandas program to select columns by data type of a given DataFrame.
'''import pandas as pd
df = pd.DataFrame({
    'name': ['Alberto Franco','Gino Mcneill','Ryan Parkes', 'Eesha Hinton', 'Syed Wharton'],
    'date_of_birth': ['17/05/2002','16/02/1999','25/09/1998','11/05/2002','15/09/1997'],
    'age': [18.5, 21.2, 22.5, 22, 23]
})
#print(df)       
df1 = df.select_dtypes(include='float64')           
print('select numerical columns ')
print(df1)      
df2 = df.select_dtypes(include='object')
print('select string columns')
print(df2)'''

#Write a Pandas program to split a given DataFrame into two random subsets.
'''import pandas as pd
df = pd.DataFrame({
    'name': ['Alberto Franco','Gino Mcneill','Ryan Parkes', 'Eesha Hinton', 'Syed Wharton'],
    'date_of_birth': ['17/05/2002','16/02/1999','25/09/1998','11/05/2002','15/09/1997'],
    'age': ['18', '21', '22', '22', '23']
})
#print(df)       
#print(df.shape)
print('subset-1 and shape:')
df1 = df.sample(frac=0.6)
df2 = df.drop(df1.index)
print(df1)
print(df1.shape)
print('subset-2 and shape:')
print(df2)
print(df2.shape)'''

#Write a Pandas program to rename all columns with the same pattern of a given DataFrame
'''import pandas as pd
df = pd.DataFrame({
    'Name': ['Alberto Franco','Gino Mcneill','Ryan Parkes', 'Eesha Hinton', 'Syed Wharton'],
    'Date_Of_Birth ': ['17/05/2002','16/02/1999','25/09/1998','11/05/2002','15/09/1997'],
    'Age': [18.5, 21.2, 22.5, 22, 23]
})
#print(df)       
df = df.rename(str.lower,axis='columns')
print(df)  
#df.columns = df.columns.str.lower().str.rstrip()     
#print(df.head())'''

#Write a Pandas program to merge datasets and check uniqueness
'''import pandas as pd
df = pd.DataFrame({
    'Name': ['Alberto Franco','Gino Mcneill','Ryan Parkes', 'Eesha Hinton', 'Syed Wharton'],
    'Date_Of_Birth ': ['17/05/2002','16/02/1999','25/09/1998','11/05/2002','15/09/1997'],
    'Age': [18.5, 21.2, 22.5, 22, 23]
})
#print(df)       
df1 = df.iloc[2:]
print(df1) 
df2 = df.drop([2])
print(df2)      
#df1 = df.copy(deep=True)
#df = df1.drop([0,1])
#df1 = df.drop([2])
#print(df)
#print(df1)             
print("\none_to_one”: check if merge keys are unique in both left and right datasets:")
d_merge1 = pd.merge(df1,df2,validate='one_to_one')
print(d_merge1)         
print('\none_to_many” or “1:m”: check if merge keys are unique in left dataset: ')
d_merge2 = pd.merge(df1,df2,validate='one_to_many')
print(d_merge2)
print('\nmany_to_one” or “m:1”: check if merge keys are unique in right dataset:')
d_merge3 = pd.merge(df1,df2,validate="many_to_one")
print(d_merge3) '''

#Write a Pandas program to convert continuous values of a column in a given DataFrame to categorical
'''import pandas as pd
df = pd.DataFrame({
    'name': ['Alberto Franco','Gino Mcneill','Ryan Parkes', 'Eesha Hinton', 'Syed Wharton', 'Kierra Gentry'],
      'age': [18, 22, 85, 50, 80, 5]
})
#print(df)       
df['age_group'] = pd.cut(df['age'],bins=[0,18,65,99],labels=['kids','adult','elderly'])     
print(df['age_group']) '''

#Write a Pandas program to display memory usage of a given DataFrame and every column of the DataFrame
'''import pandas as pd
df = pd.DataFrame({
    'Name': ['Alberto Franco','Gino Mcneill','Ryan Parkes', 'Eesha Hinton', 'Syed Wharton'],
    'Date_Of_Birth ': ['17/05/2002','16/02/1999','25/09/1998','11/05/2002','15/09/1997'],
    'Age': [18.5, 21.2, 22.5, 22, 23]
})
#print(df) 
print('global usage of memory of the dataframe: ')
print(df.info(memory_usage='deep'))      
print('the usage of memoery of every column: ')
df = df.memory_usage(deep=True)         
print(df)  '''

#Write a Pandas program to combine many given series to create a DataFrame
'''import pandas as pd
s1 = pd.Series(['php', 'python', 'java', 'c#', 'c++'])
s2 = pd.Series([1, 2, 3, 4, 5])
#print(s1)
#print(s2)      
print('combine above series to a dataFrame: ') 
df = pd.DataFrame(s1,s2).reset_index()
#print(df)       
print('\nusing pandas concat: ')
df1 = pd.concat([s1,s2],axis=1)
print(df1)    
print('\nusing pandas DF with dict, gives a specific name to the columns: ')  
df2 = pd.DataFrame({'col1':s1,'col2':s2})
print(df2) '''

#Write a Pandas program to create DataFrames that contains random values, contains missing values,\
#  contains datetime values and contains mixed values
'''import pandas as pd
df1 = pd.util.testing.makeDataFrame() # contains random values
print("\ncontains random values")
print(df1)      
df2 = pd.util.testing.makeMissingDataframe() #contains missing values
print("\ncontains missing values")
print(df2)      
df3 = pd.util.testing.makeTimeDataFrame() # containts datetime values
print("\ncontaints datetime values")
print(df3)      
df4 = pd.util.testing.makeMixedDataFrame() #containts mixed values
print("\ncontaints mixed values")
print(df4) '''

#Write a Pandas program to fill missing values in time series data
'''import pandas as pd
import numpy as np
sdata = {"c1":[120, 130 ,140, 150, np.nan, 170], "c2":[7, np.nan, 10, np.nan, 5.5, 16.5]}
df = pd.DataFrame(sdata)    
df.index = pd.util.testing.makeDateIndex()[0:6]   
#print(df)  
print('dataframe after interpolate: ')
df = df.interpolate()
print(df)  '''

#Write a Pandas program to use a local variable within a query.
'''import pandas as pd
df = pd.DataFrame({'W':[68,75,86,80,66],'X':[78,85,96,80,86], 'Y':[84,94,89,83,86],'Z':[86,97,96,72,83]})
#print(df)       
print('values which are less than maximum value of W column: ')
maxi = df['W'].max()
print(df.query("W < @maxi"))  '''

#Write a Pandas program to clean object column with mixed data of a given DataFrame using regular expression
'''import pandas as pd
d = {"agent": ["a001", "a002", "a003", "a003", "a004"], "purchase":[4500.00, 7500.00, "$3000.25", "$1250.35", "9000.00"]}
df = pd.DataFrame(d)
#print(df)       
print(df['purchase'].apply(type))
#print('data types: ')          
print('new data types: ')
df['purchase'] = df['purchase'].replace("[$,]","",regex=True).astype('float')      
print(df['purchase'].apply(type))'''

#Write a Pandas program to get the numeric representation of an array\
#  by identifying distinct values of a given column of a dataframe.
'''import pandas as pd
df = pd.DataFrame({
    'Name': ['Alberto Franco','Gino Mcneill','Ryan Parkes', 'Eesha Hinton', 'Gino Mcneill'],
    'Date_Of_Birth ': ['17/05/2002','16/02/1999','25/09/1998','11/05/2002','15/09/1997'],
    'Age': [18.5, 21.2, 22.5, 22, 23]
})
#print(df)                      
lab1,uni1 = pd.factorize(df['Name'])
print(lab1)
print(uni1) '''

#Write a Pandas program to replace the current value in a dataframe column based on last largest value. \
# If the current value is less than last largest value replaces the value with 0
'''import pandas as pd
df1=pd.DataFrame({'rnum':[23, 21, 27, 22, 34, 33, 34, 31, 25, 22, 34, 19, 31, 32, 19]})
print(df1)      
df1['rnum'] = df1.rnum.where(df1.rnum.eq(df1.rnum.cummax()),0)
print(df1) '''

#Write a Pandas program to check for inequality of two given DataFrames.
'''import pandas as pd
df1 = pd.DataFrame({'W':[68,75,86,80,None],'X':[78,85,None,80,86], 'Y':[84,94,89,83,86],'Z':[86,97,96,72,83]})
df2 = pd.DataFrame({'W':[78,75,86,80,None],'X':[78,85,96,80,76], 'Y':[84,84,89,83,86],'Z':[86,97,96,72,83]})
#print(df1)
#print(df2)      
df = df1.ne(df2)
print(df) '''

#Write a Pandas program to get lowest n records within each group of a given DataFrame.
'''import pandas as pd
d = {'col1': [1, 2, 3, 4, 7, 11], 'col2': [4, 5, 6, 9, 5, 0], 'col3': [7, 5, 8, 12, 1,11]}
df = pd.DataFrame(data=d)
#print(df)       
df1 = df.nsmallest(3,'col1')
print(df1)
df2 = df.nsmallest(3,'col2') 
print(df2)      
df3 = df.nsmallest(3,'col3') 
print(df3) '''
           