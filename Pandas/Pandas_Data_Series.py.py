#Pandas Data Series exercises at w3resource.com
#Write a Pandas program to add, subtract, multiple and divide two Pandas Series.
'''import pandas as pd
s1 = pd.Series([2,4,6,8,10])
s2 = pd.Series([1,3,5,7,9])
print('add')
a = s1 + s2
print(a)
print('subtract')
b = s1 - s2
print(b)
print('multiple')
c = s1 * s2
print(c)
print('divide')
d = s1 / s2
print(d)'''

#Write a Pandas program to compare the elements of the two Pandas Series.
'''import pandas as pd
s1 = pd.Series([2,4,6,8,10])
s2 = pd.Series([1,3,5,7,10])
print('equals')
a = s1 == s2
print(a)
print('greater than')
b = s1 > s2
print(b)
print('less than')
c = s1 < s2
print(c)'''

#Write a Pandas program to convert a dictionary to a Pandas series
'''import pandas as pd
dct = {'a':100,'b':200,'c':300,'d':400,'e':800}
s = pd.Series(dct)
print(s)'''

#Write a Pandas program to convert a NumPy array to a Pandas series.
'''import pandas as pd
import numpy as np
d1 = np.array([10,20,30,40,50])
print(d1)
print('converted pandas series: ')
s = pd.Series(d1)
print(s)'''

#Write a Pandas program to change the data type of given a column or a Series
'''import pandas as pd
s1 = pd.Series(['100','200','python','300.12','400'])
print(s1)
x = pd.to_numeric(s1,errors='coerce')
print('change the data type to numeric: ')
print(x)'''

#Write a Pandas program to convert the first column of a DataFrame as a Series
'''import pandas as pd
df = pd.DataFrame({'col1':[1,2,3,4,7,11],'col2':[4,5,6,9,5,0],'col3':[7,5,8,12,1,11]})
print(df)
x = pd.Series(df['col1'])
#x = df.iloc[:,0]
print('1st column as a series:')
print(x)
print(type(x))'''

#Write a Pandas program to convert a given Series to an array
'''import pandas as pd
import numpy as np
s = pd.Series(['100','200','python','300.12','400'])
print(s)
x = np.array(s.tolist())
print('series to an array:')
print(x)'''

#Write a Pandas program to convert Series of lists to one Series
'''import pandas as pd
s = pd.Series([['red','green','white'],['red','black'],['yellow']])
print(s)
x = s.apply(pd.Series).stack().reset_index(drop=True)
print(x)'''

#Write a Pandas program to sort a given Series.
'''import pandas as pd
s = pd.Series(data=['100','200','python','300.12','400'])
print(s)
x = s.sort_values()
print(x)'''

#Write a Pandas program to add some data to an existing Series.
'''import pandas as pd
s = pd.Series(['100','200','300.12','python','400'])
print(s)
x = s.append(pd.Series(['500','php']))
#x = s.append(pd.Series([500,'php'])).reset_index(drop=True)
print(x)'''

#Write a Pandas program to create a subset of a given series based on value and condition.
'''import pandas as pd
s = pd.Series(data=[0,1,2,3,4,5,6,7,8,9,10])
print(s)
i = 6
x = s[s<i]
print(x)'''

# Write a Pandas program to change the order of index of a given series.
'''import pandas as pd
s = pd.Series(data=[1,2,3,4,5],index=['A','B','C','D','E'])
print(s)
print('data series after changing the order of index: ')
x = s.reindex(index=['B','A','C','D','E'])
print(x)'''

#Write a Pandas program to create the mean and standard deviation of the data of a given Series
'''import pandas as pd
s = pd.Series(data=[1,2,3,4,5,6,7,8,9,5,3])
print(s)
print('mean of the said data series: ')
x = s.mean()
print(x)
print('standard deviation of the said data series: ')
c = s.std()
print(c)'''

#Write a Pandas program to get the items of a given series not present in another given series.
'''import pandas as pd
s1 = pd.Series([1,2,3,4,5])
s2 = pd.Series([2,4,6,8,10])
x = s1[~s1.isin(s2)]
print('items of s1 not presented in s2:')
print(x)
print('items of s2 not presented in s1:')
y = s2[~s2.isin(s1)]
print(y)'''

# Write a Pandas program to get the items which are not common of two given series.
'''import pandas as pd
import numpy as np
s1 = pd.Series(data=[1,2,3,4,5])
s2 = pd.Series(data=[2,4,6,8,10])
print('items of a given series not presented in another given series: ')
x = pd.Series(np.union1d(s1,s2))
y = pd.Series(np.intersect1d(s1,s2))
rez = x[~x.isin(y)]
print(rez)'''

#Write a Pandas program to compute the minimum, 25th percentile, median, 75th, and maximum of a given series.
'''import pandas as pd
import numpy as np
nums = np.random.RandomState(100)
nums_state = pd.Series(nums.normal(10,4,20))
print(nums_state)
rez = np.percentile(nums_state,[0,25,50,75,100])
print('\nMin,25th percentile,median,75th, and max of a given series: ')
print(rez)'''

#Write a Pandas program to calculate the frequency counts of each unique value of a given series
'''import pandas as pd
import numpy as np
nums = pd.Series(np.take(list('0123456789'),np.random.randint(10,size=40)))
print(nums)
unique_vals = nums.value_counts()
print('frequency of each unique value of the said series:')
print(unique_vals)'''

#Write a Pandas program to display most frequent value in a given series and replace everything else as 'Other' in the series.
'''import pandas as pd
import numpy as np
np.random.RandomState(100)
nums = pd.Series(np.random.randint(1,5,15))
print(nums)
freq_val = nums.value_counts()
print(freq_val)
repl_elem = nums[~nums.isin(nums.value_counts().index[:1])]='other'
print(nums)'''

#Write a Pandas program to find the positions of numbers that are multiples of 5 of a given series.
'''import pandas as pd
import numpy as np
nums = pd.Series(np.random.randint(1,10,9))
print(nums)
rez = np.where(nums %5 == 0)
print(rez)'''

#Write a Pandas program to extract items at given positions of a given series.
'''import pandas as pd
nums = pd.Series(list('2390238923902390239023'))
element_pos = [0,2,6,11,21]
print(nums)
rez = nums.loc[element_pos]
print(rez)'''

#Write a Pandas program to get the positions of items of a given series in another given series
'''import pandas as pd
s1 = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
s2 = pd.Series([1, 3, 5, 7, 10])
rez = [pd.Index(s1).get_loc(i) for i in s2]
print('positions of items of s2 in s1')
print(rez)'''

#Write a Pandas program convert the first and last character of each word to upper case in each word of a given series
'''import pandas as pd
s = pd.Series(['php','python','java','c#'])
print(s)
rez = s.map(lambda x: x[0].upper()+x[1:-1]+x[-1].upper())
print(rez)'''

#Write a Pandas program to calculate the number of characters in each word in a given series. 
'''import pandas as pd
s = pd.Series(['php','python','java','c#'])
print(s)
print('numbers of chararters in each word:')
x = s.apply(len)
print(x)
y = s.map(lambda x: len(x))
#print(y)'''

#Write a Pandas program to compute difference of differences between consecutive numbers of a given series.
'''import pandas as pd
s = pd.Series([1,3,5,8,10,11,15])
print(s)
print('difference of difference between consecutive nums:')
x = s.diff().tolist()
print(x)
y = s.diff().diff().tolist()
print(y)'''

#Write a Pandas program to convert a series of date strings to a timeseries.
'''import pandas as pd
s = pd.Series(['01 Jan 2015', '10-02-2016', '20180307', '2014/05/06', '2016-04-12', '2019-04-06T11:20'])
print(s)
rez = pd.to_datetime(s)
print(rez)'''

# Write a Pandas program to get the day of month, day of year, week number and day of week from a given series of date strings
'''import pandas as pd
from dateutil.parser import parse
s = pd.Series(['01 Jan 2015', '10-02-2016', '20180307', '2014/05/06', '2016-04-12', '2019-04-06T11:20'])
s = s.map(lambda x: parse(x))
print(s)
print('day of month:')
print(s.dt.day.tolist())
print('day of year:')
print(s.dt.day_of_year.tolist())
print('week number: ')
print(s.dt.isocalendar().week.tolist())
print('day of week: ')
print(s.dt.day_name().tolist())'''

#Write a Pandas program to convert year-month string to dates adding a specified day of the month.
'''import pandas as pd
from dateutil.parser import parse
s = pd.Series(['Jan 2015','Feb 2016','Mar 2017','Apr 2018','May 2019'])
print(s)
rez = s.map(lambda x: parse('11' + x))
print(rez)'''

#Write a Pandas program to filter words from a given series that contain atleast two vowels.
'''import pandas as pd
from collections import Counter
s = pd.Series(['Red','Green','Orange','Pink','Yellow','White'])
filt = s.map(lambda x: sum([Counter(x.lower()).get(i,0) for i in list('aeiou')])>=2)
print(s[filt])'''

#Write a Pandas program to compute the Euclidean distance between two given series.
'''import pandas as pd
import numpy as np
x = pd.Series([1,2,3,4,5,6,7,8,9,10])
y = pd.Series([11, 8, 7, 5, 6, 5, 3, 4, 7, 1])
print(x)
print(y)
rez = np.linalg.norm(x-y)
print(rez)'''

#Write a Pandas program to find the positions of the values neighboured by smaller values on both sides in a given series
'''import pandas as pd
import numpy as np
s = pd.Series([1,8,7,5,6,5,3,4,7,1])
print(s)
pos = np.diff(np.sign(np.diff(s)))
rez = np.where(pos == -2)[0]+1
print(rez)'''

#Write a Pandas program to replace missing white spaces in a given string with the least frequent character
'''import pandas as pd
string = "abc def abcdef icd"
s = pd.Series(list(string))
#print(s)
freq_char = s.value_counts()
#print(list(freq_char))
least_freq = freq_char.dropna().index[-1]
#print(least_freq)
rez = "".join(s.replace(" ",least_freq))
print(rez)'''

#Write a Pandas program to compute the autocorrelations of a given numeric series
'''import pandas as pd
import numpy as np
nums = pd.Series(np.arange(15) + np.random.normal(1,10,15))
print(nums)
autocor = [nums.autocorr(i).round(2) for i in range(11)]
print(autocor[1:])'''

#Write a Pandas program to create a TimeSeries to display all the Sundays of given year
'''import pandas as pd
s = pd.Series(pd.date_range(start='2022-01-01',periods=52,freq='W-SUN'))
print('all sundays of 2022: ')
print(s)'''

#Write a Pandas program to convert given series into a dataframe with its index as another column on the dataframe
'''import pandas as pd
import numpy as np
elem = list('ABCDEFGHIJKLMNOP')
x = np.arange(16)
nums = dict(zip(elem,x))
#print(nums)
s = pd.Series(nums)
#print(s)
df = s.to_frame().reset_index()
print(df)'''

#Write a Pandas program to stack two given series vertically and horizontally.
'''import pandas as pd
s1 = pd.Series(range(10))
s2 = pd.Series(list('pqrstuvwxy'))
#print(s1)
#print(s2)
s = pd.concat([s1,s2],axis=1)
print(s)'''

#Write a Pandas program to check the equality of two given series.
'''import pandas as pd
s1 = pd.Series([1, 8, 7, 5, 6, 5, 3, 4, 7, 1])
s2 = pd.Series([1, 8, 7, 5, 6, 5, 3, 4, 7, 1])
rez = s1 == s2
print(rez)
x = s1.equals(s2)
#print(x)'''

#Write a Pandas program to find the index of the first occurrence of the smallest and largest value of a given series.
'''import pandas as pd
s1 = pd.Series([1, 3, 7, 12, 88, 23, 3, 1, 9, 0])
small_val = s1.idxmin()
large_val = s1.idxmax()
print(small_val)
print(large_val)'''

#Write a Pandas program to check inequality over the index axis of a given dataframe and a given series
'''import pandas as pd
df = pd.DataFrame({'W':[68,75,86,80,None],'X':[78,75,None,80,86], 'Y':[84,94,89,86,86],'Z':[86,97,96,72,83]});
s = pd.Series([68, 75, 86, 80, None]) 
print(df)
print(s)
rez = df.ne(s,axis=0)
print(rez)'''









