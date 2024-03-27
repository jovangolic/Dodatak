#Pandas Joining and merging DataFrame exercises at w3resource.com

#Write a Pandas program to join the two given dataframes along rows and assign all data
'''import pandas as pd
student_data1 = pd.DataFrame({
        'student_id': ['S1', 'S2', 'S3', 'S4', 'S5'],
         'name': ['Danniella Fenton', 'Ryder Storey', 'Bryce Jensen', 'Ed Bernal', 'Kwame Morin'], 
        'marks': [200, 210, 190, 222, 199]})
student_data2 = pd.DataFrame({
        'student_id': ['S4', 'S5', 'S6', 'S7', 'S8'],
        'name': ['Scarlette Fisher', 'Carla Williamson', 'Dante Morse', 'Kaiser William', 'Madeeha Preston'], 
        'marks': [201, 200, 198, 219, 201]})
#print(student_data1)
#print(student_data2)
s = pd.concat([student_data1,student_data2])
print(s)  '''

#Write a Pandas program to join the two given dataframes along columns and assign all data
'''import pandas as pd
student_data1 = pd.DataFrame({
        'student_id': ['S1', 'S2', 'S3', 'S4', 'S5'],
         'name': ['Danniella Fenton', 'Ryder Storey', 'Bryce Jensen', 'Ed Bernal', 'Kwame Morin'], 
        'marks': [200, 210, 190, 222, 199]})
student_data2 = pd.DataFrame({
        'student_id': ['S4', 'S5', 'S6', 'S7', 'S8'],
        'name': ['Scarlette Fisher', 'Carla Williamson', 'Dante Morse', 'Kaiser William', 'Madeeha Preston'], 
        'marks': [201, 200, 198, 219, 201]})
#print(student_data1)
#print(student_data2)        
print('\njoin two dataframes along columns: ')
#rez = student_data1.join(student_data2,lsuffix='_caller',rsuffix='_other')
#print(rez)  
rez2 = pd.concat([student_data1,student_data2],axis=1)
print(rez2) '''

#Write a Pandas program to append rows to an existing DataFrame and display the combined data
'''import pandas as pd
student_data1 = pd.DataFrame({
        'student_id': ['S1', 'S2', 'S3', 'S4', 'S5'],
         'name': ['Danniella Fenton', 'Ryder Storey', 'Bryce Jensen', 'Ed Bernal', 'Kwame Morin'], 
        'marks': [200, 210, 190, 222, 199]})
s2 = pd.Series(['S6', 'Scarlette Fisher', 205], index=['student_id', 'name', 'marks'])
#print(student_data1)
#print(s2)   
rez = student_data1.append(s2,ignore_index=True)
print(rez) '''

#Write a Pandas program to append a list of dictioneries or series to a existing DataFrame and display the combined data
'''import pandas as pd
student_data1  = pd.DataFrame({
        'student_id': ['S1', 'S2', 'S3', 'S4', 'S5'],
         'name': ['Danniella Fenton', 'Ryder Storey', 'Bryce Jensen', 'Ed Bernal', 'Kwame Morin'], 
        'marks': [200, 210, 190, 222, 199]})
dicts = [{'student_id': 'S6', 'name': 'Scarlette Fisher', 'marks': 203},
         {'student_id': 'S7', 'name': 'Bryce Jensen', 'marks': 207}]        
s6 = pd.Series(['S6', 'Scarlette Fisher', 205], index=['student_id', 'name', 'marks'])
#print(student_data1)
#print(s6)  
rez = student_data1.append(dicts,ignore_index=True)
print('\ncombined data: ')
print(rez)'''

#Write a Pandas program to join the two given dataframes along rows and merge with another dataframe along the common column id.
'''import pandas as pd
student_data1 = pd.DataFrame({
        'student_id': ['S1', 'S2', 'S3', 'S4', 'S5'],
         'name': ['Danniella Fenton', 'Ryder Storey', 'Bryce Jensen', 'Ed Bernal', 'Kwame Morin'], 
        'marks': [200, 210, 190, 222, 199]})
student_data2 = pd.DataFrame({
        'student_id': ['S4', 'S5', 'S6', 'S7', 'S8'],
        'name': ['Scarlette Fisher', 'Carla Williamson', 'Dante Morse', 'Kaiser William', 'Madeeha Preston'], 
        'marks': [201, 200, 198, 219, 201]})
exam_data = pd.DataFrame({
        'student_id': ['S1', 'S2', 'S3', 'S4', 'S5', 'S7', 'S8', 'S9', 'S10', 'S11', 'S12', 'S13'],
        'exam_id': [23, 45, 12, 67, 21, 55, 33, 14, 56, 83, 88, 12]})
#print(student_data1)        
#print(student_data2)
#print(exam_data)    
student = pd.concat([student_data1,student_data2],axis=0)
print('\njoin first two dataframes along rows: ')
#print(student)  
rez = pd.merge(student,exam_data,on='student_id')
print("join the said result_data and df_exam_data along student_id:")
print(rez)  '''

#Write a Pandas program to join the two dataframes using the common column of both dataframes
'''import pandas as pd
student_data1 = pd.DataFrame({
        'student_id': ['S1', 'S2', 'S3', 'S4', 'S5'],
         'name': ['Danniella Fenton', 'Ryder Storey', 'Bryce Jensen', 'Ed Bernal', 'Kwame Morin'], 
        'marks': [200, 210, 190, 222, 199]})

student_data2 = pd.DataFrame({
        'student_id': ['S4', 'S5', 'S6', 'S7', 'S8'],
        'name': ['Scarlette Fisher', 'Carla Williamson', 'Dante Morse', 'Kaiser William', 'Madeeha Preston'], 
        'marks': [201, 200, 198, 219, 201]})
#print(student_data1)
#print(student_data2)        
print('\nmerged data: ')
mrg = pd.merge(student_data1,student_data2,how='inner',suffixes=('_x','_y'),on='student_id')
print(mrg) '''

# Write a Pandas program to join the two dataframes with matching records from both sides where available
'''import pandas as pd
student_data1 = pd.DataFrame({
        'student_id': ['S1', 'S2', 'S3', 'S4', 'S5'],
         'name': ['Danniella Fenton', 'Ryder Storey', 'Bryce Jensen', 'Ed Bernal', 'Kwame Morin'], 
        'marks': [200, 210, 190, 222, 199]})

student_data2 = pd.DataFrame({
        'student_id': ['S4', 'S5', 'S6', 'S7', 'S8'],
        'name': ['Scarlette Fisher', 'Carla Williamson', 'Dante Morse', 'Kaiser William', 'Madeeha Preston'], 
        'marks': [201, 200, 198, 219, 201]})
#print(student_data1)        
#print(student_data2)
mrg = pd.merge(student_data1,student_data2,suffixes=('_x','_y'),on='student_id',how='outer')
print(mrg)'''

#Write a Pandas program to join (left join) the two dataframes using keys from left dataframe only
'''import pandas as pd
data1 = pd.DataFrame({'key1': ['K0', 'K0', 'K1', 'K2'],
                     'key2': ['K0', 'K1', 'K0', 'K1'],
                     'P': ['P0', 'P1', 'P2', 'P3'],
                     'Q': ['Q0', 'Q1', 'Q2', 'Q3']}) 
data2 = pd.DataFrame({'key1': ['K0', 'K1', 'K1', 'K2'],
                      'key2': ['K0', 'K0', 'K0', 'K0'],
                      'R': ['R0', 'R1', 'R2', 'R3'],
                      'S': ['S0', 'S1', 'S2', 'S3']})
#print(data1)
#print('---------------')
#print(data2)                          
mrg1 = pd.merge(data1,data2,how='left')
print('\nmerged data form data1: ')
print(mrg1) 
#print('\nmerged data form data2: ')
#mrg2 = pd.merge(data2,data1,how='left')
#print(mrg2) '''

#Write a Pandas program to join two dataframes using keys from right dataframe only
'''import pandas as pd
data1 = pd.DataFrame({'key1': ['K0', 'K0', 'K1', 'K2'],
                     'key2': ['K0', 'K1', 'K0', 'K1'],
                     'P': ['P0', 'P1', 'P2', 'P3'],
                     'Q': ['Q0', 'Q1', 'Q2', 'Q3']}) 
data2 = pd.DataFrame({'key1': ['K0', 'K1', 'K1', 'K2'],
                      'key2': ['K0', 'K0', 'K0', 'K0'],
                      'R': ['R0', 'R1', 'R2', 'R3'],
                      'S': ['S0', 'S1', 'S2', 'S3']})
#print(data1)
#print('-------') 
#print(data2)                             
mrg1 = pd.merge(data1,data2,how='right',on=['key1','key2'])
#print('\nmerged data keys from data2: ')
#print(mrg1) 
mrg2 = pd.merge(data2,data1,how='right',on=['key1','key2'])
print('\nmerged data keys from data1: ')
print(mrg2) '''

#Write a Pandas program to merge two given datasets using multiple join keys
'''import pandas as pd
data1 = pd.DataFrame({'key1': ['K0', 'K0', 'K1', 'K2'],
                     'key2': ['K0', 'K1', 'K0', 'K1'],
                     'P': ['P0', 'P1', 'P2', 'P3'],
                     'Q': ['Q0', 'Q1', 'Q2', 'Q3']}) 
data2 = pd.DataFrame({'key1': ['K0', 'K1', 'K1', 'K2'],
                      'key2': ['K0', 'K0', 'K0', 'K0'],
                      'R': ['R0', 'R1', 'R2', 'R3'],
                      'S': ['S0', 'S1', 'S2', 'S3']})
#print(data2)
#print(data1)
mrg = pd.merge(data1,data2,on=['key1','key2'])
print(mrg) '''

#Write a Pandas program to create a new DataFrame based on existing series,\
#using specified argument and override the existing columns names
'''import pandas as pd
s1 = pd.Series([0, 1, 2, 3], name='col1')
s2 = pd.Series([0, 1, 2, 3])
s3 = pd.Series([0, 1, 4, 5], name='col3')
#print(s1)
#print(s2)
#print(s3)   
df = pd.concat([s1,s2,s3],keys=['column1','column2','column3'],axis=1)
print(df) '''

# Write a Pandas program to create a combination from two dataframes where a column id combination appears more than once in both dataframes
'''import pandas as pd
data1 = pd.DataFrame({'key1': ['K0', 'K0', 'K1', 'K2'],
                     'key2': ['K0', 'K1', 'K0', 'K1'],
                     'P': ['P0', 'P1', 'P2', 'P3'],
                     'Q': ['Q0', 'Q1', 'Q2', 'Q3']}) 
data2 = pd.DataFrame({'key1': ['K0', 'K1', 'K1', 'K2'],
                      'key2': ['K0', 'K0', 'K0', 'K0'],
                      'R': ['R0', 'R1', 'R2', 'R3'],
                      'S': ['S0', 'S1', 'S2', 'S3']})
#print(data1)
#print('\n---------')
#print(data2)                          
mrg = pd.merge(data1,data2,suffixes=('_x','_y'),validate='many_to_many',on='key1')
print(mrg)  '''

#Write a Pandas program to combine the columns of two potentially differently-indexed DataFrames into a single result DataFrame
'''import pandas as pd
data1 = pd.DataFrame({'A': ['A0', 'A1', 'A2'],
                      'B': ['B0', 'B1', 'B2']},
                     index=['K0', 'K1', 'K2'])

data2 = pd.DataFrame({'C': ['C0', 'C2', 'C3'],
                      'D': ['D0', 'D2', 'D3']},
                     index=['K0', 'K2', 'K3'])
#print(data1)
#print(data2)                        
print('\nmerged data: ')
rez = data1.join(data2)
print(rez) '''

#Write a Pandas program to merge two given dataframes with different columns
'''import pandas as pd
data1 = pd.DataFrame({'key1': ['K0', 'K0', 'K1', 'K2'],
                     'key2': ['K0', 'K1', 'K0', 'K1'],
                     'P': ['P0', 'P1', 'P2', 'P3'],
                     'Q': ['Q0', 'Q1', 'Q2', 'Q3']}) 
data2 = pd.DataFrame({'key1': ['K0', 'K1', 'K1', 'K2'],
                      'key2': ['K0', 'K0', 'K0', 'K0'],
                      'R': ['R0', 'R1', 'R2', 'R3'],
                      'S': ['S0', 'S1', 'S2', 'S3']})
#print(data1)
#print(data2)                      
print('\nmerge 2 dataframes with different columns: ')
mrg = pd.concat([data1,data2],axis=0,join='outer',sort=True,ignore_index=True)
print(mrg)'''

#Write a Pandas program to Combine two DataFrame objects by filling null values in one DataFrame with non-null values from other DataFrame
'''import pandas as pd
df1 = pd.DataFrame({'A': [None, 0, None], 'B': [3, 4, 5]})
df2 = pd.DataFrame({'A': [1, 1, 3], 'B': [3, None, 3]})
df1.combine_first(df2) 
#print(df1)
#print(df2)
rez = df1.combine_first(df2)
print(rez)  '''

