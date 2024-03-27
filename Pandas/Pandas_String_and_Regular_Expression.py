#Pandas String and Regular Expression at w3resource

#Write a Pandas program to convert all the string values to upper, lower cases in a given pandas series.\
# Also find the length of the string value
'''import pandas as pd
import numpy as np
s = pd.Series(['X', 'Y', 'Z', 'Aaba', 'Baca', np.nan, 'CABA', None, 'bird', 'horse', 'dog'])
#print(s)
print('\n all values to upper case: ')
print(s.str.upper())
print('\all values to lower case:')
print(s.str.lower()) 
print('\str length')
print(s.str.len())  '''

#Write a Pandas program to remove whitespaces, left sided whitespaces\
#  and right sided whitespaces of the string values of a given pandas series
'''import pandas as pd
color1 = pd.Index([' Green', 'Black ', ' Red ', 'White', ' Pink '])
print(color1)   
print('\nremoved whitespace ')
print(color1.str.strip())
print('\nremoved right sided whitespace: ')
print(color1.str.rstrip())
print('\nremoved left sided whitespace')
print(color1.str.lstrip())'''

#Write a Pandas program to add leading zeros to the integer column in a pandas series\
#  and makes the length of the field to 8 digit.
'''import pandas as pd
nums = {'amount': [10, 250, 3000, 40000, 500000]}
df = pd.DataFrame(nums)
#print(df)    
#df['amount'] = df['amount'].apply(lambda x: '{0:0>8}'.format(x))
#print(df)
df['amount'] = df['amount'].apply(lambda x: 0 if x<8 else '{0:0>8}'.format(x))
print(df)  '''

#Write a Pandas program to add leading zeros to the character column in a pandas series\
#and makes the length of the field to 8 digit
'''import pandas as pd
nums = {'amount': ['10', '250', '3000', '40000', '500000']}
df = pd.DataFrame(nums) 
#print(df)   
df['amount'] = list(map(lambda x: x.zfill(8),df['amount']))
print('\add leading zeros: ')
print(df) '''

#Write a Pandas program to capitalize all the string values of specified columns of a given DataFrame
'''import pandas as pd
df = pd.DataFrame({
    'name': ['alberto','gino','ryan', 'Eesha', 'syed'],
    'date_of_birth ': ['17/05/2002','16/02/1999','25/09/1998','11/05/2002','15/09/1997'],
    'age': [18.5, 21.2, 22.5, 22, 23]})
#print(df)
df['name'] = df['name'].apply(lambda x: str.capitalize(x))
#df['name'] = list(map(lambda x: x.capitalize(),df['name']))
print(df) '''

#Write a Pandas program to count of occurrence of a specified substring in a DataFrame column.
'''import pandas as pd
df = pd.DataFrame({
    'name_code': ['c001','c002','c022', 'c2002', 'c2222'],
    'date_of_birth ': ['12/05/2002','16/02/1999','25/09/1998','12/02/2022','15/09/1997'],
    'age': [18.5, 21.2, 22.5, 22, 23]})
#print(df)       
df['count'] = df['name_code'].apply(lambda x: x.count(str(2)))
print(df)  '''

#Write a Pandas program to find the index of a given substring of a DataFrame column
'''import pandas as pd
df = pd.DataFrame({
    'name_code': ['c001','c002','c022', 'c2002', 'c2222'],
    'date_of_birth ': ['12/05/2002','16/02/1999','25/09/1998','12/02/2022','15/09/1997'],
    'age': [18.5, 21.2, 22.5, 22, 23]})
#print(df)       
df['Index'] = df['name_code'].apply(lambda x: x.find(str(22)))
print(df) '''

#Write a Pandas program to find the index of a substring of DataFrame with beginning and end position.
'''import pandas as pd
df = pd.DataFrame({
    'name_code': ['c0001','1000c','b00c2', 'b2c02', 'c2222'],
    'date_of_birth ': ['12/05/2002','16/02/1999','25/09/1998','12/02/2022','15/09/1997'],
    'age': [18.5, 21.2, 22.5, 22, 23]})
#print(df)       
df['Index'] = df['name_code'].apply(lambda x: x.find('c',0,5))
print(df)'''

#Write a Pandas program to check whether alpha numeric values present in a given column of a DataFrame. 
'''import pandas as pd
df = pd.DataFrame({
    'name_code': ['Company','Company a001','Company 123', '1234', 'Company 12'],
    'date_of_birth ': ['12/05/2002','16/02/1999','25/09/1998','12/02/2022','15/09/1997'],
    'age': [18.5, 21.2, 22.5, 22, 23]})
#print(df)       
print('\nwether all chars in the string are alphanumeric: ')
df['name_code_is_alphanum'] = df['name_code'].apply(lambda x: x.isalnum())
print(df)  '''

#Write a Pandas program to check whether alphabetic values present in a given column of a DataFrame
'''import pandas as pd
df = pd.DataFrame({
    'company_code': ['Company','Company a001','Company 123', 'abcd', 'Company 12'],
    'date_of_sale ': ['12/05/2002','16/02/1999','25/09/1998','12/02/2022','15/09/1997'],
    'sale_amount': [12348.5, 233331.2, 22.5, 2566552.0, 23.0]})
#print(df)       
print('\nwhether alphabetic values in company_code col:')
#df['company_code_is_alpha'] = df['company_code'].apply(lambda x: x.isalpha())
df['company_code_is_alpha'] = list(map(lambda x: x.isalpha(),df['company_code']))
print(df) '''

#Write a Pandas program to check whether only numeric values present in a given column of a DataFrame
'''import pandas as pd
df = pd.DataFrame({
    'company_code': ['Company','Company a001', '2055', 'abcd', '123345'],
    'date_of_sale ': ['12/05/2002','16/02/1999','25/09/1998','12/02/2022','15/09/1997'],
    'sale_amount': [12348.5, 233331.2, 22.5, 2566552.0, 23.0]})
#print(df)      
df['company_code_is_digit'] = df['company_code'].apply(lambda x: x.isdigit())
print('\nnum values present in company_code column: ')
print(df) '''

#Write a Pandas program to check whether only lower case or upper case is present in a given column of a DataFrame
'''import pandas as pd
df = pd.DataFrame({
    'company_code': ['ABCD','EFGF', 'hhhh', 'abcd', 'EAWQaaa'],
    'date_of_sale ': ['12/05/2002','16/02/1999','25/09/1998','12/02/2022','15/09/1997'],
    'sale_amount': [12348.5, 233331.2, 22.5, 2566552.0, 23.0]})
#print(df)       
df['company_code_ul_cases'] = df['company_code'].apply(lambda x: x.isupper())
print('\n is upper? ')
print(df)   
df['company_code_ul_cases'] = df['company_code'].apply(lambda x: x.islower())
print('\n is lower? ')
print(df) '''

#Write a Pandas program to check whether only proper case or title case is present in a given column of a DataFrame
'''import pandas as pd
df = pd.DataFrame({
    'company_code': ['Abcd','EFGF', 'Hhhh', 'abcd', 'EAWQaaa'],
    'date_of_sale ': ['12/05/2002','16/02/1999','25/09/1998','12/02/2022','15/09/1997'],
    'sale_amount': [12348.5, 233331.2, 22.5, 2566552.0, 23.0]})
#print(df)       
df['company_code_is_title'] = df['company_code'].apply(lambda x: x.istitle())
print('\nis propper case or title case?')
print(df) '''

#Write a Pandas program to check whether only space is present in a given column of a DataFrame.
'''import pandas as pd
df = pd.DataFrame({
    'company_code': ['Abcd','EFGF ', '  ', 'abcd', ' '],
    'date_of_sale ': ['12/05/2002','16/02/1999','25/09/1998','12/02/2022','15/09/1997'],
    'sale_amount': [12348.5, 233331.2, 22.5, 2566552.0, 23.0]})
#print(df)       
df['company_code_is_space'] = df['company_code'].apply(lambda x: x.isspace())
print(df)   '''

#Write a Pandas program to get the length of the string present of a given column in a DataFrame
'''import pandas as pd
df = pd.DataFrame({
    'company_code': ['Abcd','EFGF', 'skfsalf', 'sdfslew', 'safsdf'],
    'date_of_sale ': ['12/05/2002','16/02/1999','25/09/1998','12/02/2022','15/09/1997'],
    'sale_amount': [12348.5, 233331.2, 22.5, 2566552.0, 23.0]})
#print(df)       
print('\nlength of the string in a column: ')
df['company_code_length'] = df['company_code'].apply(lambda x: len(x))
print(df)  '''

#Write a Pandas program to get the length of the integer of a given column in a DataFrame.
'''import pandas as pd
df = pd.DataFrame({
    'company_code': ['Abcd','EFGF', 'skfsalf', 'sdfslew', 'safsdf'],
    'date_of_sale': ['12/05/2002','16/02/1999','25/09/1998','12/02/2022','15/09/1997'],
    'sale_amount': [12348.5, 233331.2, 22.5, 2566552.0, 23.0]})
#print(df)       
print('\nlength of sale_amount column: ')
df['sale_amt_length'] = df['sale_amount'].apply(lambda x: len(str(x)))
#df['sale_amt_length'] = df['sale_amount'].map(str).apply(len)
print(df)'''

#Write a Pandas program to check if a specified column starts with a specified string in a DataFrame
'''import pandas as pd
df = pd.DataFrame({
    'company_code': ['Abcd','EFGF', 'zefsalf', 'sdfslew', 'zekfsdf'],
    'date_of_sale': ['12/05/2002','16/02/1999','25/09/1998','12/02/2022','15/09/1997'],
    'sale_amount': [12348.5, 233331.2, 22.5, 2566552.0, 23.0]})
#print(df)       
print('\nif a specified column starts with a specified str: ')
df['company_code_starts_with'] = df['company_code'].apply(lambda x: x.startswith('ze')) #starts with ze
print(df)  '''

#Write a Pandas program to swap the cases of a specified character column in a given DataFrame
'''import pandas as pd
df = pd.DataFrame({
    'company_code': ['Abcd','EFGF', 'zefsalf', 'sdfslew', 'zekfsdf'],
    'date_of_sale': ['12/05/2002','16/02/1999','25/09/1998','12/02/2022','15/09/1997'],
    'sale_amount': [12348.5, 233331.2, 22.5, 2566552.0, 23.0]})
#print(df)       
print('\nswap cases in company_code: ')
df['swapped_comp_code'] = df['company_code'].apply(lambda x: x.swapcase())
print(df)  '''

#Write a Pandas program to convert a specified character column in upper/lower cases in a given DataFrame
'''import pandas as pd
df = pd.DataFrame({
    'company_code': ['Abcd','EFGF', 'zefsalf', 'sdfslew', 'zekfsdf'],
    'date_of_sale': ['12/05/2002','16/02/1999','25/09/1998','12/02/2022','15/09/1997'],
    'sale_amount': [12348.5, 233331.2, 22.5, 2566552.0, 23.0]
})

df1 = pd.DataFrame({
    'company_code': ['Abcd','EFGF', 'zefsalf', 'sdfslew', 'zekfsdf'],
    'date_of_sale': ['12/05/2002','16/02/1999','25/09/1998','12/02/2022','15/09/1997'],
    'sale_amount': [12348.5, 233331.2, 22.5, 2566552.0, 23.0]
})
#print(df)
#print(df1)
#df['upper_comp_code'] = df['company_code'].apply(lambda x: x.upper())
#print(df)   
df1['lower_comp_code'] = df['company_code'].apply(lambda x: x.lower())
print(df1)  '''

#Write a Pandas program to convert a specified character column in title case in a given DataFrame
'''import pandas as pd
df = pd.DataFrame({
    'company_code': ['Abcd','EFGF', 'zefsalf', 'sdfslew', 'zekfsdf'],
    'date_of_sale': ['12/05/2002','16/02/1999','25/09/1998','12/02/2022','15/09/1997'],
    'sale_amount': [12348.5, 233331.2, 22.5, 2566552.0, 23.0]
})
#print(df) 
print('\ntitle cases: ')
df['title_cases'] = df['company_code'].apply(lambda x: x.title())
print(df) '''

# Write a Pandas program to replace arbitrary values with other values in a given DataFrame
'''import pandas as pd
df = pd.DataFrame({
    'company_code': ['A','B', 'C', 'D', 'A'],
    'date_of_sale': ['12/05/2002','16/02/1999','25/09/1998','12/02/2022','15/09/1997'],
    'sale_amount': [12348.5, 233331.2, 22.5, 2566552.0, 23.0]})
#print(df)       
rez = df.replace('A','C')
print('\nreplace A with C: ')
print(rez)  '''

#Write a Pandas program to replace more than one value with other values in a given DataFrame
'''import pandas as pd
df = pd.DataFrame({
    'company_code': ['A','B', 'C', 'D', 'A'],
    'date_of_sale': ['12/05/2002','16/02/1999','25/09/1998','12/02/2022','15/09/1997'],
    'sale_amount': [12348.5, 233331.2, 22.5, 2566552.0, 23.0]})
#print(df)       
rez = df.replace({'A':'X','D':'Y'})
print(rez) '''

#Write a Pandas program to split a string of a column of a given DataFrame into multiple columns.
'''import pandas as pd
df = pd.DataFrame({
    'name': ['Alberto  Franco','Gino Ann Mcneill','Ryan  Parkes', 'Eesha Artur Hinton', 'Syed  Wharton'],
    'date_of_birth ': ['17/05/2002','16/02/1999','25/09/1998','11/05/2002','15/09/1997'],
    'age': [18.5, 21.2, 22.5, 22, 23]})
#print(df)       
df[['first','middle','last']] = df['name'].str.split(' ',expand=True)
print(df)'''

#Write a Pandas program to extract email from a specified column of string type of a given DataFrame
'''import pandas as pd
import re as re
pd.set_option('display.max_columns', 10)
df = pd.DataFrame({
    'name_email': ['Alberto Franco af@gmail.com','Gino Mcneill gm@yahoo.com','Ryan Parkes rp@abc.io', 'Eesha Hinton', 'Gino Mcneill gm@github.com']
    })
#print(df)       
def new_email(text):
    email = re.findall(r"[\w\.-]+@[\w\.-]+",str(text))
    return ''.join(email)
df['email'] = df['name_email'].apply(lambda x: new_email(x))
print(df)  '''

#Write a Pandas program to extract hash attached word from twitter text from the specified column of a given DataFrame.
'''import re as re
import pandas as pd
pd.set_option('display.max_columns', 10)
df = pd.DataFrame({
    'tweets': ['#Obama says goodbye','Retweets for #cash','A political endorsement in #Indonesia', '1 dog = many #retweets', 'Just a simple #egg']
    })
#print(df)       
def find_hash(text):
    tweets = re.findall(r"(?<=#)\w+",text)
    return ''.join(tweets)
df['hash_word'] = df['tweets'].apply(lambda x: find_hash(x))
print(df) '''

#Write a Pandas program to extract word mention someone in tweets using @ from the specified column of a given DataFrame
'''import pandas as pd
import re as re
pd.set_option('display.max_columns', 10)
df = pd.DataFrame({
    'tweets': ['@Obama says goodbye','Retweets for @cash','A political endorsement in @Indonesia', '1 dog = many #retweets', 'Just a simple #egg']
    })
#print(df)       
def find_char(text):
    tweets = re.findall(r"(?<=@)\w+",text)
    return ''.join(tweets)
df['at_word'] = df['tweets'].apply(lambda x: find_char(x))
print(df)'''

#Write a Pandas program to extract only number from the specified column of a given DataFrame
'''import pandas as pd
import re as re
pd.set_option("display.max_columns",10)
df = pd.DataFrame({
    'company_code': ['c0001','c0002','c0003', 'c0003', 'c0004'],
    'address': ['7277 Surrey Ave.','920 N. Bishop Ave.','9910 Golden Star St.', '25 Dunbar St.', '17 West Livingston Court']
    })
#print(df)       
def find_nums(text):
    nums = re.findall(r"[0-9]+",text)
    return ''.join(nums)
df['number'] = df['address'].apply(lambda x: find_nums(x))
print(df)  '''

#Write a Pandas program to extract only phone number from the specified column of a given DataFrame
'''import pandas as pd
import re as re
pd.set_option("display.max_columns",10)
df = pd.DataFrame({
    'company_code': ['c0001','c0002','c0003', 'c0003', 'c0004'],
    'company_phone_no': ['Company1-Phone no. 4695168357','Company2-Phone no. 8088729013','Company3-Phone no. 6204658086', 'Company4-Phone no. 5159530096', 'Company5-Phone no. 9037952371']
    })
#print(df)       
def find_phone_num(text):
    nums = re.findall(r"\b\d{10}\b",text)
    return ''.join(nums)
df['number'] = df['company_phone_no'].apply(lambda x: find_phone_num(x))
print(df)  '''

#Write a Pandas program to extract year between 1800 to 2200 from the specified column of a given DataFrame
'''import pandas as pd
import re as re
pd.set_option("display.max_columns",10)
df = pd.DataFrame({
    'company_code': ['c0001','c0002','c0003', 'c0003', 'c0004'],
    'year': ['year 1800','year 1700','year 2300', 'year 1900', 'year 2200']
    })
#print(df)       
def year_range(text):
    nums = re.findall(r"\b(18[0-9]{2}|19[0-8][0-9]|199[0-9]|2[01][0-9]{2}|2200)\b",text)
    return nums
df['year_range'] = df['year'].apply(lambda x: year_range(x))
print(df) '''

#Write a Pandas program to extract only non alphanumeric characters from the specified column of a given DataFrame
'''import pandas as pd
import re as re
pd.set_option("display.max_columns",10)
df = pd.DataFrame({
    'company_code': ['c0001#','c00@0^2','$c0003', 'c0003', '&c0004'],
    'year': ['year 1800','year 1700','year 2300', 'year 1900', 'year 2200']
    })
#print(df)       
def char_extract(text):
    rez = re.findall(r"[^A-Za-z0-9 ]",text)
    return rez
df['nonalpha'] = df['company_code'].apply(lambda x: char_extract(x))
print(df) '''

#Write a Pandas program to extract only punctuations from the specified column of a given DataFrame
'''import pandas as pd
import re as re
pd.set_option("display.max_columns",10)
df = pd.DataFrame({
    'company_code': ['c0001.','c000,2','c0003', 'c0003#', 'c0004,'],
    'year': ['year 1800','year 1700','year 2300', 'year 1900', 'year 2200']
    })
#print(df)       
def extract_punc(text):
    rez = re.findall(r"\W",text)
    return rez  
df['nonalpha'] = df['company_code'].apply(lambda x: extract_punc(x))
print(df)'''

#Write a Pandas program to remove repetitive characters from the specified column of a given DataFrame
'''import pandas as pd #i've had help for this task
import re as re
pd.set_option("display.max_columns",10)
df = pd.DataFrame({
    'text_code': ['t0001.','t0002','t0003', 't0004'],
    'text_lang': ['She livedd a long life.', 'How oold is your father?', 'What is tthe problem?','TThhis desk is used by Tom.']
    })
#print(df)
def rep_char(text):
    x = text.group(0)
    if len(x)>1:
        return x[0:1]
def unique_char(rep,text):
    c = re.sub(r"(\w)\1+",rep,text)
    return c
df['normal_text'] = df['text_lang'].apply(lambda x: unique_char(rep_char,x))
print(df)'''

#Write a Pandas program to extract numbers greater than 940 from the specified column of a given DataFrame
'''import pandas as pd
import re as re
pd.set_option("display.max_columns",10)
df = pd.DataFrame({
    'company_code': ['c0001','c0002','c0003', 'c0003', 'c0004'],
    'address': ['7277 Surrey Ave.1111','920 N. Bishop Ave.','9910 Golden Star St.', '1025 Dunbar St.', '1700 West Livingston Court']
    })
#print(df)       
def greater_than(num):
    n = re.findall(r"95[5-9]|9[6-9]\d|[1-9]\d{3,}",num)
    return ' '.join(n)
df['num_great'] = df['address'].apply(lambda x: greater_than(x))
print(df)'''

#Write a Pandas program to extract numbers less than 100 from the specified column of a given DataFrame
'''import pandas as pd
import re as re
pd.set_option('display.max_columns',10)
df = pd.DataFrame({
    'company_code': ['c0001','c0002','c0003', 'c0003', 'c0004'],
    'address': ['72 Surrey Ave.11','92 N. Bishop Ave.','9910 Golden Star St.', '102 Dunbar St.', '17 West Livingston Court']
    })
#print(df)       
def less_than(n):
    nums = []
    for i in n.split():
        rez = re.findall(r"\b(0*(?:[1-9][0-9]?|100))\b",i)
        nums.append(rez)
        total = [','.join(x) for x in nums if x != []]
    return ' '.join(total)   
df['num_less'] = df['address'].apply(lambda x: less_than(x))    
print(df) '''

#Write a Pandas program to check whether two given words present in a specified column of a given DataFrame
'''import pandas as pd
import re as re
pd.set_option('display.max_columns',10)
df = pd.DataFrame({
    'company_code': ['c0001','c0002','c0003', 'c0003', 'c0004'],
    'address': ['9910 Surrey Ave.','92 N. Bishop Ave.','9910 Golden Star Ave.', '102 Dunbar St.', '17 West Livingston Court']
    })
#print(df)          
def test(text):
    words = re.findall(r"(?=.*Ave)(?=.*9910).*",text)
    return ''.join(words)
df['check_2_words'] = df['address'].apply(lambda x: test(x))
print(df) '''

#Write a Pandas program to extract date (format: mm-dd-yyyy) from a given column of a given DataFrame
'''import pandas as pd
import re as re
df = pd.DataFrame({
    'company_code': ['Abcd','EFGF', 'zefsalf', 'sdfslew', 'zekfsdf'],
    'date_of_sale': ['12/05/2002','16/02/1999','05/09/1998','12/02/2022','15/09/1997'],
    'sale_amount': [12348.5, 233331.2, 22.5, 2566552.0, 23.0]
})
#print(df)   
def find_dateTime(text):
    date = re.findall(r"\b(1[0-2]|0[1-9])/(3[01]|[12][0-9]|0[1-9])/([0-9]{4})\b",text)
    return date
df['valid_dates'] = df['date_of_sale'].apply(lambda x: find_dateTime(x))
print(df)'''

#Write a Pandas program to extract only words from a given column of a given DataFrame
'''import pandas as pd
import re as re
df = pd.DataFrame({
    'company_code': ['Abcd','EFGF', 'zefsalf', 'sdfslew', 'zekfsdf'],
    'date_of_sale': ['12/05/2002','16/02/1999','05/09/1998','12/02/2022','15/09/1997'],
    'address': ['9910 Surrey Ave.','92 N. Bishop Ave.','9910 Golden Star Ave.', '102 Dunbar St.', '17 West Livingston Court']
})
#print(df)   
def extract_words(text):
    s1 = re.findall(r"\b([A-Za-z]+)\b",text)
    return ' '.join(s1)   
df['only_words'] = df['address'].apply(lambda x: extract_words(x))
print(df) '''

#Write a Pandas program to extract the sentences where a specific word is present in a given column of a given DataFrame
'''import pandas as pd
import re as re
df = pd.DataFrame({
    'company_code': ['Abcd','EFGF', 'zefsalf', 'sdfslew', 'zekfsdf'],
    'date_of_sale': ['12/05/2002','16/02/1999','05/09/1998','12/02/2022','15/09/1997'],
    'address': ['9910 Surrey Avenue','92 N. Bishop Avenue','9910 Golden Star Avenue', '102 Dunbar St.', '17 West Livingston Court']
})
#print(df)   
def word(s,text):
    s1 = re.findall(r"([^.]*"+text+"[^.]*)",s)
    return s1
df['filter_sentence'] = df['address'].apply(lambda x: word(x,'Avenue'))
print(df) '''

#Write a Pandas program to extract words starting with capital words from a given column of a given DataFrame. 
'''import pandas as pd
import re as re
df = pd.DataFrame({
    'company_code': ['Abcd','EFGF', 'zefsalf', 'sdfslew', 'zekfsdf'],
    'date_of_sale': ['12/05/2002','16/02/1999','05/09/1998','12/02/2022','15/09/1997'],
    'address': ['9910 Surrey Avenue','92 N. Bishop Avenue','9910 Golden Star Avenue', '102 Dunbar St.', '17 West Livingston Court']
})
#print(df)   
def capital_words(words):
    s = re.findall(r"\b([A-Z]\w+)",words)
    return s
df['capital_words'] = df['address'].apply(lambda x: capital_words(x))
print(df) '''

#Write a Pandas program to remove the html tags within the specified column of a given DataFrame
'''import pandas as pd
import re as re
df = pd.DataFrame({
    'company_code': ['Abcd','EFGF', 'zefsalf', 'sdfslew', 'zekfsdf'],
    'date_of_sale': ['12/05/2002','16/02/1999','05/09/1998','12/02/2022','15/09/1997'],
    'address': ['9910 Surrey <b>Avenue</b>','92 N. Bishop Avenue','9910 <br>Golden Star Avenue', '102 Dunbar <i></i>St.', '17 West Livingston Court']
})
#print(df)   
def remove_tags(tags):
    s = re.sub(r"<.*?>","",tags)
    return ''.join(s)
df['without_tags'] = df['address'].apply(lambda x: remove_tags(x))
print(df)  '''

