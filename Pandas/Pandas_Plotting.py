#pandas plotting exercises at w3resource.com

#Write a Pandas program to create a line plot of the historical stock prices of Alphabet Inc. between two specific dates
'''import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_csv('alphabet_stock_data.csv')
#print(df.head())
start = pd.to_datetime('2020-04-01')
end = pd.to_datetime('2020-09-30')
df['Date'] = pd.to_datetime(df['Date'])
filt = (df['Date'] >= start)&(df['Date'] <= end)
df1 = df.loc[filt]
df2 = df1.set_index('Date')
plt.figure(figsize=(7,5))
plt.suptitle('stock price of alphabet inc.,\n01-04-2020 to 30-09-2020',fontsize=18,color='black')
plt.xlabel('Date',fontsize=16,color='black')
plt.ylabel('$price',fontsize=16,color='black')
df2['Close'].plot(color='green')
plt.show()'''

#Write a Pandas program to create a line plot of the opening, closing stock prices of Alphabet Inc. between two specific dates
'''import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('alphabet_stock_data.csv')
#print(df.head())
start = pd.to_datetime('2020-04-01')
end = pd.to_datetime('2020-09-30')
df['Date'] = pd.to_datetime(df['Date'])
filt = (df['Date']>=start)&(df['Date']<=end)
df1 = df.loc[filt] 
plt.figure(figsize=(8,5))
df1.plot(x='Date',y=['Open','Close'])
plt.suptitle("Opening/Closing stock prices of Alphabet inc.,\n01-04-2020 to 30-09-2020",\
        fontsize=18,color='black')
plt.xlabel('Date',fontsize=16,color='black')
plt.ylabel('$price',fontsize=16,color='black')
plt.show()'''

#Write a Pandas program to create a bar plot of the trading volume of Alphabet Inc. stock between two specific dates
'''import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('alphabet_stock_data.csv')
#print(df.head())
start = pd.to_datetime('2020-04-01')
end = pd.to_datetime('2020-04-30')
df['Date'] = pd.to_datetime(df['Date'])
filt = (df['Date']>start)&(df['Date']<end)
df1 = df.loc[filt]
df2 = df1.set_index('Date')
plt.figure(figsize=(6,6))
plt.suptitle('Trading Volume of Alphabet Inc. stock,\n01-04-2020 to 30-04-2020',\
        fontsize=16,color='black')
plt.xlabel('Date',fontsize=12,color='black')
plt.ylabel('Trading Volume',fontsize=12,color='black')
df2['Volume'].plot(kind='bar')        
plt.show()'''

#Write a Pandas program to create a bar plot of opening, closing stock prices of Alphabet Inc. between two specific dates.
'''import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('alphabet_stock_data.csv')
#print(df.head())
start = pd.to_datetime('2020-04-01')
end = pd.to_datetime('2020-04-30')
df['Date'] = pd.to_datetime(df['Date'])
filt = (df['Date']>start)&(df['Date']<end)
df1 = df.loc[filt]
plt.figure(figsize=(6,6))
df1.plot(x='Date',y=['Open','Close'],kind='bar')
plt.suptitle('Opening/Closing stock prices Alphabet Inc.,\n01-04-2020 to 30-04-2020',\
        fontsize=16,color='black')
plt.xlabel('Date',fontsize=12,color='black')        
plt.show()'''

#Write a Pandas program to create a stacked bar plot of opening, closing stock prices of Alphabet Inc. between two specific dates
'''import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('alphabet_stock_data.csv')
#print(df.head())
start = pd.to_datetime('2020-04-01')
end = pd.to_datetime('2020-04-30')
df['Date'] = pd.to_datetime(df['Date'])
filt = (df['Date']>start)&(df['Date']<end)
df1 = df.loc[filt]
df2 = df1[['Date','Open','Close']]
df3 = df2.set_index('Date')
plt.figure(figsize=(7,7))
df3.plot.bar(stacked=True)
plt.suptitle('Opening/Closing stock prices Alphabet Inc.,\n01-04-2020 to 30-04-2020',\
        fontsize=16,color='black')      
plt.show()'''

#Write a Pandas program to create a horizontal stacked bar plot of opening, closing stock prices of Alphabet Inc. between two specific dates
'''import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('alphabet_stock_data.csv')
#print(df.head())
start = pd.to_datetime('2020-04-01')
end = pd.to_datetime('2020-04-30')
df['Date'] = pd.to_datetime(df['Date'])
filt = (df['Date']>start)&(df['Date']<end)
df1 = df.loc[filt]
df2 = df1[['Date','Open','Close']]
df3 = df2.set_index('Date')
plt.figure(figsize=(20,20))
df3.plot.barh(stacked=True)
plt.suptitle('Opening/Closing stock prices Alphabet Inc.,\n01-04-2020 to 30-04-2020',\
        fontsize=16,color='black')
plt.show() '''

#Write a Pandas program to create a histograms plot of opening, closing, high, low stock prices of Alphabet Inc.\
#between two specific dates.
'''import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('alphabet_stock_data.csv')
#print(df.head())
start = pd.to_datetime('2020-04-01')
end = pd.to_datetime('2020-09-30')
df['Date'] = pd.to_datetime(df['Date'])
filt = (df['Date']>start)&(df['Date']<end)
df1 = df.loc[filt]
df2 = df1[['Open','Close','High','Low']]
plt.figure(figsize=(7,7))
df2.plot.hist(alpha=0.5)
plt.suptitle('Opening/Closing/High/Low stock prices of Alphabet Inc.,\nfrom 01-04-2020 to 30-09-2020',\
        fontsize=16,color='blue')
plt.show()'''

#Write a Pandas program to create a stacked histograms plot of opening, closing, high, low stock prices\
#of Alphabet Inc. between two specific dates
'''import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('alphabet_stock_data.csv')
#print(df.head())
start = pd.to_datetime('2020-04-01')
end = pd.to_datetime('2020-04-30')
df['Date'] = pd.to_datetime(df['Date'])
filt = (df['Date']>start)&(df['Date']<end)
df1 = df.loc[filt]
df2 = df1[['Open','Close','High','Low']]
plt.figure(figsize=(8,8))
df2.plot.hist(stacked=True,bins=20)
plt.suptitle('Opening/Closing/High/Low stock prices of Alphabet Inc.,\nfrom 01-04-2020 to 30-09-2020',\
        fontsize=16,color='blue')
plt.show() '''

#Write a Pandas program to draw a horizontal and cumulative histograms plot of opening stock prices\
#of Alphabet Inc. between two specific dates
'''import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('alphabet_stock_data.csv')
#print(df.head())
start = pd.to_datetime('2020-04-01')
end = pd.to_datetime('2020-04-30')
df['Date'] = pd.to_datetime(df['Date'])
filt = (df['Date']>start)&(df['Date']<end)
df1 = df.loc[filt]
df2 = df1[['Open']]
plt.figure(figsize=(7,7))
df2.plot.hist(orientation='horizontal',cumulative=True)
plt.suptitle('Opening stock price of Alphabet Inc.,\nfrom 01-04-2020 to 30-04-2020',\
        fontsize=16,color='black')      
plt.show() '''

#Write a Pandas program to create a stacked histograms plot of opening, closing, high, low stock prices\
#of Alphabet Inc. between two specific dates with more bins
'''import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('alphabet_stock_data.csv')
#print(df.head())
start = pd.to_datetime('2020-04-01')
end = pd.to_datetime('2020-09-30')
df['Date'] = pd.to_datetime(df['Date'])
filt = (df['Date']>start)&(df['Date']<end)
df1 = df.loc[filt]
df2 = df1[['Open','Close','High','Low']]
plt.figure(figsize=(8,8))
df2.plot.hist(stacked=True,bins=200)
plt.suptitle('Opening/Closing/High/Low stock prices of Alphabet Inc.,\nfrom 01-04-2020 to 30-09-2020',\
        fontsize=16,color='black')
plt.show() '''

#Write a Pandas program to create a stacked histograms plot with more bins of opening, closing, high,\
#low stock prices of Alphabet Inc. between two specific dates.
'''import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('alphabet_stock_data.csv')
#print(df.head())
start = pd.to_datetime('2020-04-01')
end = pd.to_datetime('2020-09-30')
df['Date'] = pd.to_datetime(df['Date'])
filt = (df['Date']>start)&(df['Date']<end)
df1 = df.loc[filt]
df2 = df1[['Open','Close','High','Low']]
plt.figure(figsize=(15,15))
df2.hist()
plt.suptitle('Opening/Closing/High/Low stock prices of Alphabet Inc., from 01-04-2020 to 30-09-2020',\
        fontsize=11,color='black')
plt.show()  '''

#Write a Pandas program to create a plot of stock price and trading volume of Alphabet Inc. between two specific dates.
'''import pandas  as pd
import matplotlib.pyplot as plt
df = pd.read_csv('alphabet_stock_data.csv')
#print(df.head())
start = pd.to_datetime('2020-04-01')
end = pd.to_datetime('2020-09-30')
df['Date'] = pd.to_datetime(df['Date'])
filt = (df['Date']>start)&(df['Date']<end)
df1 = df.loc[filt]
df2 = df1.set_index('Date')
#plt.figure(figsize=(8,8))
top_graph = plt.subplot2grid((5,4),(0,0),rowspan=3,colspan=4)
top_graph.plot(df2.index,df2['Close'])
plt.title('Historical stock prices of Alphabet Inc. [01-04-2020 to 30-09-2020]')
bottom_graph = plt.subplot2grid((5,4),(3,0),rowspan=1,colspan=4)
bottom_graph.bar(df2.index,df2['Volume'])
plt.title('\nAlphabet Inc. Trading Volume',y=-0.60)
plt.gcf().set_size_inches(12,8)
plt.show()'''

#Write a Pandas program to create a plot of Open, High, Low, Close, Adjusted Closing prices\
#and Volume of Alphabet Inc. between two specific dates.
'''import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('alphabet_stock_data.csv')
#print(df.head())
start = pd.to_datetime('2020-04-01')
end = pd.to_datetime('2020-09-30')
df['Date'] = pd.to_datetime(df['Date'])
filt = (df['Date']>=start)&(df['Date']<=end)
df1 = df.loc[filt]
df2 = df1.set_index('Date')
df2.plot(subplots=True,figsize=(8,8))
plt.legend(loc='best')
plt.suptitle('Open,High,Low,Close,Adj Close prices & Volume of Alphabet Inc., from 01-04-2020 to 30-09-2020',\
        fontsize=12,color='black')
plt.show()'''

#Write a Pandas program to create a plot of adjusted closing prices, thirty days and forty days\
#simple moving average of Alphabet Inc. between two specific dates
'''import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('alphabet_stock_data.csv')
#print(df.head())
start = pd.to_datetime('2020-04-01')
end = pd.to_datetime('2020-09-30')
df['Date'] = pd.to_datetime(df['Date'])
filt = (df['Date']>=start)&(df['Date']<=end)
df1 = df.loc[filt]
stock_data = df.set_index('Date')
close_data = stock_data['Adj Close']
stock_data['SMA_30_days'] = stock_data.iloc[:,4].rolling(window=30).mean()
stock_data['SMA_40_days'] = stock_data.iloc[:,4].rolling(window=40).mean()
plt.figure(figsize=(10,8))
plt.grid(True)
plt.suptitle('Historical stock prices of Alphabet Inc.,[01-04-2020 to 30-09-2020]',\
        fontsize=16,color='black')
plt.plot(stock_data['Adj Close'],label='Adjusted Closing Price',color='black')
plt.plot(stock_data['SMA_30_days'],label='30 days simple moving average',color='red')
plt.plot(stock_data['SMA_40_days'],label='40 days simple moving average',color='green')
plt.legend(loc=2)
plt.show()'''

#Write a Pandas program to create a plot of adjusted closing prices, 30 days simple moving average\
#and exponential moving average of Alphabet Inc. between two specific dates
'''import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('alphabet_stock_data.csv')
#print(df.head())
start = pd.to_datetime('2020-04-01')
end = pd.to_datetime('2020-09-30')
df['Date'] = pd.to_datetime(df['Date'])
filt = (df['Date']>=start)&(df['Date']<=end)
df1 = df.loc[filt]
stock_date = df1.set_index('Date')
close_date = stock_date['Adj Close']
stock_date['SMA_30_days'] = stock_date.iloc[:,4].rolling(window=30).mean()
stock_date['EMA_20_days'] = stock_date.iloc[:,4].ewm(span=20,adjust=False).mean()
plt.figure(figsize=(10,8))
plt.grid(True)
plt.suptitle('Historical stock prices of Alphabet Inc.,[01-04-2020 to 30-09-2020]',\
        fontsize=16,color='black')
plt.plot(stock_date['Adj Close'],label='Adjusted Closing Price',color='black')
plt.plot(stock_date['SMA_30_days'],label='30 days Simple moving average',color='red')
plt.plot(stock_date['EMA_20_days'],label='20 days Exponential moving average',color='green')
plt.legend(loc=2)        
plt.show()'''

#Write a Pandas program to create a scatter plot of the trading volume/stock prices of Alphabet Inc. \
#stock between two specific dates
'''import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('alphabet_stock_data.csv')
#print(df.head())
start = pd.to_datetime('2020-04-01')
end = pd.to_datetime('2020-09-30')
df['Date'] = pd.to_datetime(df['Date'])
filt = (df['Date']>=start)&(df['Date']<=end)
df1 = df.loc[filt]
df2 = df1.set_index('Date')
x = ['Close'];y = ['Volume']
plt.figure(figsize=(10,8))
df2.plot.scatter(x,y,s=50)
plt.grid(True)
plt.title('Trading Volume/Price of Alphabet Inc. stock,\n01-04-2020 to 30-09-2020',\
        fontsize=16,color='black')
plt.xlabel('Stock Price',fontsize=12,color='black')
plt.ylabel('Trading Volume',fontsize=12,color='black')
plt.show()'''

#Write a Pandas program to create a plot to visualize daily percentage returns of Alphabet Inc. stock price\
#between two specific dates
'''import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('alphabet_stock_data.csv')
#print(df.head())
start = pd.to_datetime('2020-04-01')
end = pd.to_datetime('2020-09-30')     
df['Date'] = pd.to_datetime(df['Date'])
filt = (df['Date']>=start)&(df['Date']<=end)
df1 = df.loc[filt]
df2 = df1[['Date','Adj Close']]
df3 = df2.set_index('Date')
changes = df3.pct_change(periods=1)
changes['Adj Close'].plot(figsize=(10,8),legend=True,marker='o',linestyle='--')
plt.grid(True)
plt.suptitle("Daily % return of Alphabet Inc. stock price,\n01-04-2020 to 30-09-2020",\
        fontsize=12,color='black')
plt.show()'''

#Write a Pandas program to plot the volatility over a period of time of Alphabet Inc. stock price between two specific dates
'''import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('alphabet_stock_data.csv')
#print(df.head())
start = pd.to_datetime('2020-04-01')
end = pd.to_datetime('2020-09-30')
df['Date'] = pd.to_datetime(df['Date'])
filt = (df['Date']>=start)&(df['Date']<=end)
df1 = df.loc[filt]
df2 = df1[['Date','Close']]
df3 = df2.set_index('Date')
data_filled = df3.asfreq('D',method='ffill')
data_return = data_filled.pct_change()
data = data_return.rolling(window=30,min_periods=30).std()
plt.figure(figsize=(10,8))
data.plot()
plt.grid(True)
plt.suptitle('Volatility over a period of time of Alphabet Inc. stock price,\n01-04-2020 to 30-09-2020',\
        fontsize=12,color='black')
plt.show()  '''


#Write a Pandas program to create a histogram to visualize daily return distribution of Alphabet Inc.\
#stock price between two specific dates. 
'''import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
df = pd.read_csv('alphabet_stock_data.csv')
#print(df.head())
start = pd.to_datetime('2020-04-01')
end = pd.to_datetime('2020-09-30')
df['Date'] = pd.to_datetime(df['Date'])
filt = (df['Date']>=start)&(df['Date']<=end)
df1 = df.loc[filt]
df2 = df1[['Date','Adj Close']]
df3 = df2.set_index('Date')
data_pct = df3.pct_change(periods=1)
plt.figure(figsize=(10,8))
data_pct.plot.hist(legend=False,bins=20)
sb.distplot(data_pct['Adj Close'].dropna(),bins=100,color='purple')
plt.suptitle("Daily % return of Alphabet Inc. stock price,\n01-04-2020 to 30-09-2020",\
        fontsize=12,color='black')
plt.xlabel('Adj Close',fontsize=8,color='black')        
plt.grid(True)
plt.show()'''


