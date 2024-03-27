#pandas time series exercises at w3resource.com

#Write a Pandas program to create:
#a) Datetime object for Jan 15 2012.
#b) Specific date and time of 9:20 pm.
#c) Local date and time.
#d) A date without time.
#e) Current date.
#f) Time from a datetime.
#g) Current local time.
'''import datetime
from datetime import datetime
print('\ndatetime obj for jan 11 2012: ')
print(datetime(2012,1,11)) 
print('\nspecific date and time of 9:20pm')
print(datetime(2011,1,11,21,20))
print('\nlocal date and time: ')
print(datetime.now())
print('\n a date without time: ')
print(datetime.date(datetime(2012,5,22)))
print('\ncurrent date:')
print(datetime.now().date())
print('\ntime from a datetime: ')
print(datetime.time(datetime(2012,12,15,18,12)))
print('\ncurrent local time: ')
print(datetime.now().time())'''

#Write a Pandas program to create:a) a specific date using timestamp; b) date and time using timestamp;
#c) a time adds in the current local date using timestamp; d) current date and time using timestamp.
'''import pandas as pd
dt = pd.Timestamp('2016-11-10')
print(dt)
print('\ndate and time using timestamp')
dt2 = pd.Timestamp('2012-05-03 11:30')
print(dt2)
print('\na time adds in the current local date using timestamp:')
dt3 = pd.Timestamp('11:30')
print(dt3)
print('\ncurrent date and time')
dt4 = pd.Timestamp.today()
print(dt4) '''

#Write a Pandas program to create a date from a given year, month, day and another date from a given string formats
'''from datetime import datetime
date1 = datetime(year=2020, month=12, day=25)
print('\ndate from given year,month,day')
print(date1)    
from dateutil import parser
d2 = parser.parse("1st of January, 2021")
print(d2)  '''

#Write a Pandas program to print the day after and before a specified date. Also print the days between two given dates
'''import datetime
from datetime import date,datetime
import pandas as pd
cur_date = datetime(2012,10,30)
print('current date: ',cur_date)
tmr_date = cur_date + pd.Timedelta(1,unit='day')
#tmr_date = cur_date + pd.Timedelta(days=1)
print('tomorrow: ',tmr_date)
yesterday = cur_date - pd.Timedelta(1,unit='day')
#yesterday = cur_date - pd.Timedelta(days=1)
print('yesterday: ',yesterday)  
d1 = datetime(2016,8,2)
d2 = datetime(2016,7,22)
print('differece between 2 dates: ',d1-d2)'''

#Write a Pandas program to create a time-series with two index labels and random values. Also print the type of the index
'''import pandas as pd
import numpy as np
import datetime
from datetime import datetime, date
dates = [datetime(2011, 9, 1), datetime(2011, 9, 2)]
print('\ntime-series with 2 index labels: ')
ts = pd.Series(np.random.randn(2),index=dates) 
print(ts)      
print('\ntype of the index:')
print(type(ts.index))'''

#Write a Pandas program to create a time-series from a given list of dates as strings.
'''import pandas as pd
import numpy as np
import datetime
from datetime import datetime, date 
dates = ['2014-08-01','2014-08-02','2014-08-03','2014-08-04']
ts = pd.Series(np.random.randn(4),dates)
print(ts)'''

#Write a Pandas program to create a time series object that has time indexed data. \
#Also select the dates of same year and select the dates between certain dates
'''import pandas as pd
index = pd.DatetimeIndex(['2011-09-02', '2012-08-04',
                          '2015-09-03', '2010-08-04',
                          '2015-03-03', '2011-08-04',
                          '2015-04-03', '2012-08-04'])
s_dates = pd.Series([0, 1, 2, 3, 4, 5, 6, 7], index=index)
#print(s_dates)  
print('\ndates of same year: ')
print(s_dates['2015'])
print('\ndates between 2012-01-01 and 2012-12-31: ')
print(s_dates['2012-01-01':'2012-12-31'])'''

#Write a Pandas program to create a date range using a startpoint date and a number of periods
'''import pandas as pd
date_range = pd.date_range('2020-01-01', periods=45)
print(date_range)'''

#Write a Pandas program to create a whole month of dates in daily frequencies.\
#Also find the maximum, minimum timestamp and indexs
'''import pandas as pd
dates = pd.Series(pd.date_range(start='2022-12-01',periods=31,freq='D'))
#print(dates)    
max_date = dates.max()
print(max_date)
min_date = dates.min()
print(min_date)
max_index = dates.index.max()
print(max_index)    
min_index = dates.index.min()
print(min_index)'''

#Write a Pandas program to create a time series using three months frequency
'''import pandas as pd
dates = pd.date_range('2021-01-31',periods=36,freq='3M')
print(dates)  '''

#Write a Pandas program to create a sequence of durations increasing by an hour
'''import pandas as pd
ts = pd.timedelta_range(start='0 days',periods=49,freq='H')  
print('hourly range of periods 49: ')
print(ts)'''

#Write a Pandas program to convert year and day of year into a single datetime column of a dataframe
'''import pandas as pd
data = {\
"year": [2002, 2003, 2015, 2018],
"day_of_the_year": [250, 365, 1, 140]}
df = pd.DataFrame(data)
#print(df)   
df['combined'] = df['year']*1000+df['day_of_the_year']
#print(df)
df['date'] = pd.to_datetime(df['combined'],format='%Y%j')
print(df) '''

#Write a Pandas program to create a series of Timestamps from a DataFrame of integer or string columns.\
#Also create a series of Timestamps using specified columns
'''import pandas as pd
df = pd.DataFrame({'year': [2018, 2019, 2020],
                   'month': [2, 3, 4],
                   'day': [4, 5, 6],
                   'hour': [2, 3, 4]})
#print(df)                      
ts = pd.to_datetime(df)
print('\nseries of timestamps from the dataframe: ')
print(ts)   
ts1 = pd.to_datetime(df[['year','month','day']])
print(ts1)  '''

#Write a Pandas program to check if a day is a business day (weekday) or not
'''import pandas as pd
def is_business_day(date):
    return bool(len(pd.bdate_range(date,date)))
print('2020-12-01',is_business_day('2020-12-01'))       
print('2020-12-06',is_business_day('2020-12-06'))
print('2020-12-07',is_business_day('2020-12-07'))
print('2020-12-08',is_business_day('2020-12-08'))'''

#Write a Pandas program to get a time series with the last working days of each month of a specific year.
'''import pandas as pd
ts = pd.date_range('2022-01-01',periods=12,freq='BM')
print(ts) 
print('\nlast working days of each month of a specific year: ')
df = pd.DataFrame(ts,columns=['Date'])
print(df)'''

#Write a Pandas program to create a time series combining hour and minute
'''import pandas as pd
ts = pd.timedelta_range(start='0 days',periods=30,freq='1H20T')
print('\nfor a frequency of 1 hour 20 min, here i have combined the hour and min: ')
print(ts) '''

#Write a Pandas program to convert unix/epoch time to a regular time stamp in UTC.\
#Also convert the said timestamp in to a given time zone
'''import pandas as pd
epoch_t = 1621132355 #seconds
ts = pd.to_datetime(epoch_t,unit='s')
print('\nregular timestamp in UTC: ')
print(ts)   
print('\nconvert timestamp in to US/Pacific: ')
ts_convert = ts.tz_localize('UTC').tz_convert('US/Pacific')
print(ts_convert)
print('\nconvert timestamp in to Europe/Berlin: ')
ts_convert2 = ts.tz_localize('UTC').tz_convert('Europe/Berlin')
print(ts_convert2)'''

#Write a Pandas program to remove the time zone information from a Time series data
'''import pandas as pd
date1 = pd.Timestamp('2019-01-01', tz='Europe/Berlin')
date2 = pd.Timestamp('2019-01-01', tz='US/Pacific')
date3 = pd.Timestamp('2019-01-01', tz='US/Eastern')
print('\ntime series data with timezone: ')
print(date1)
print(date2)
print(date3)
print('\ntimeseries data without timezone: ')
print(date1.tz_localize(None))
print(date2.tz_localize(None))
print(date3.tz_localize(None))'''

#Write a Pandas program to subtract two timestamps of same time zone or different time zone
'''import pandas as pd
print("Subtract two timestamps of same time zone:")
date1 = pd.Timestamp('2019-03-01 12:00', tz='US/Eastern')
date2 = pd.Timestamp('2019-04-01 07:00', tz='US/Eastern')
rez = date2 - date1
print(rez)  
d1 = pd.Timestamp('2020-03-01 12:00',tz='US/Pacific')
d2 = pd.Timestamp('2020-03-01 08:00',tz='Europe/Berlin')
print("Subtract two timestamps of different time zone:")
rez2 = d1.tz_localize(None) - d2.tz_localize(None)
print(rez2)'''

#Write a Pandas program to calculate all Thursdays between two given days.
'''import pandas as pd
ts = pd.date_range(start='2020-01-01',end='2020-12-31',freq='W-THU')
print(ts)   
print('\nall thursdays between 2020-01-01 and 2020-31-12: ')
print(ts.values)'''

#Write a Pandas program to find the all the business quarterly begin and end dates of a specified year
'''import pandas as pd
print("\nAll the business quarterly begin dates of 2020:")
ts_begin = pd.date_range('2020-01-01','2020-12-31',freq='BQS-JUN')
print(ts_begin.values)
print("\nall the business quarterly end dates of 2020: ")
ts_end = pd.date_range('2020-01-01','2020-12-31',freq='BQ')
print(ts_end.values)'''

#Write a Pandas program to generate sequences of fixed-frequency dates and time spans intervals
'''import pandas as pd
print("\nSequences of fixed-frequency dates and time spans (1 H):")
dts = pd.date_range('2030-01-01',periods=10,freq='H')
print(dts)  
print("\nSequences of fixed-frequency dates and time spans (3 H):")
dts2 = pd.date_range('2030-01-01',periods=10,freq='3H')
print(dts2) '''

#Write a Pandas program to generate time series combining day and intraday offsets intervals
'''import pandas as pd
print('\ntime-series with frequency 3h10min: ')
ts1 = pd.date_range('2029-01-01',periods=20,freq='190t')
#print(ts1)  
print("\ntime-series with frequency 1 day 10 min 20 microseconds")
ts2 = pd.date_range('2029-01-01',periods=20,freq='1D10T20U')
print(ts2) '''

#Write a Pandas program to extract the day name from a specified date. \n
#Add 2 days and 1 business day with the specified date
'''import pandas as pd
ts = pd.Timestamp('2020-02-07')
print('\nfirst day: ')
print(ts)   
print("\nthe day name of the date: ")
print(ts.day_name())
print('\nadd 2 days with the said date: ')
rez = ts + pd.Timedelta('2 day')
print(rez.day_name())
print('\nnext business day: ') 
bd = rez + pd.offsets.BDay()
print(bd.day_name()) '''

#Write a Pandas program to convert integer or float epoch times to Timestamp and DatetimeIndex
'''import pandas as pd
print("\nConvert integer or float epoch times to Timestamp and DatetimeIndex upto second: ")
ts = pd.to_datetime([1329806505, 129806505, 1249892905,
                1249979305, 1250065705], unit='s')
print(ts)                   
print("\nConvert integer or float epoch times to Timestamp and DatetimeIndex upto milisecond: ")
ts2 = pd.to_datetime([1249720105100, 1249720105200, 1249720105300,
                1249720105400, 1249720105500], unit='ms')
print(ts2)  '''

# Write a Pandas program to calculate one, two, three business day(s) from a specified date.\n
# Also find the next business month end from a specific date.
'''import pandas as pd
ts = pd.Timestamp(2020,1,4)
print('\nspecified date: ')
print(ts)   
print('\none business day from the date: ')
rez1 = ts + pd.offsets.BDay()
print(rez1) 
print('\n2 business days from the date: ')
rez2 = ts + pd.offsets.BDay(2)
print(rez2) 
print("\nthree business days from the date: ")
rez3 = ts + pd.offsets.BDay(3)
print(rez3) 
print('\nnext business month end from the date: ')
rez4 = ts + pd.offsets.BusinessMonthEnd()
print(rez4) '''

#Write a Pandas program to create a period index represent all monthly boundaries of a given year. \n
#Also print start and end time for each period object in the said index.
'''import pandas as pd
import datetime
from datetime import datetime, date
sdt = datetime(2020, 1, 1)
edt = datetime(2020, 12, 31)
print(sdt)  
print(edt)  
print('\nall monthly boundaries of a given year: ')
p_idx = pd.period_range(sdt,edt,freq='M')
print(p_idx)    
print('\nstart and end time for each period object in the said index:')
for i in p_idx:
    print("{0}{1}".format(i.start_time,i.end_time)) '''

#Write a Pandas program to create a period index represent all monthly boundaries of a given year.\n
#Also print start and end time for each period object in the said index  
'''import pandas as pd
import numpy as np
s = pd.Series(np.random.randn(36),pd.period_range('2029-01','2031-12',freq='M'))
print('\nperiodIndex which represents all the calendar months periods in 2029 and 2030: ')
print(s)       
print("\nvalues for all periods in 2030: ")
print(s['2030'])'''

#Write a Pandas program to generate holidays between two dates using the US federal holiday calendar
'''import pandas as pd
from pandas.tseries.holiday import *
from datetime import datetime,date
sdt = datetime(2021,1,1)
edt = datetime(2030,12,31)
#print(sdt)
#print(edt)          
hld = USFederalHolidayCalendar()
for i in hld.holidays(start=sdt,end=edt):
    print(i)'''

#Write a Pandas program to create a monthly time period and display the list of names in the current local scope.    
'''import pandas as pd
s = pd.Period('2021-11','M')
print(s)    
print('\nlists of names in the current local scope: ')
print(dir(s))'''

#Write a Pandas program to create a yearly time period from a specified year and display the properties of this period. 
'''import pandas as pd
s = pd.Period('2020','A-DEC')
print('yearly time period: ',s)
print(dir(s)) '''


    
