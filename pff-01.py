import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
from mpl_finance import candlestick_ohlc
import matplotlib.dates as mdates
import pandas as pd
import pandas_datareader.data as web
from pandas.plotting import register_matplotlib_converters
style.use('ggplot')
register_matplotlib_converters()

"""
Video 1
"""
# start = dt.datetime(2015,1,1)
# end = dt.datetime(2019,5,25)
# df = web.DataReader('TSLA', 'yahoo', start, end)

# print(df.tail(10))

"""
Video 2
"""
# df.to_csv('stocks/tsla.csv')
# df = pd.read_csv('stocks/tsla.csv', parse_dates=True, index_col=0)

# print(df.head())

# column_values_df = df['High']
# subset = df[['High', 'Low']]
# loc = df.loc[df.shape[0]-1]
# shape = df.shape[0]

# print(column_values_df)
# print(subset)
# print(loc)
# print(shape)

# print(df[['Open', 'High']].head())

# df['Adj Close'].plot()
# plt.show()

""" 
Video 3
"""
# df = pd.read_csv('stocks/tsla.csv', parse_dates=True, index_col=0)
# # df['100ma']: promedio de los 100 ultimos precios
# df['100ma'] = df['Adj Close'].rolling(window=100, min_periods=0).mean()

# ax1 = plt.subplot2grid((6,1), (0,0), rowspan=5, colspan=1)
# ax2 = plt.subplot2grid((6,1), (5,0), rowspan=1, colspan=1, sharex=ax1)

# ax1.plot(df.index, df['Adj Close'])
# ax1.plot(df.index, df['100ma'])
# ax2.bar(df.index, df['Volume'])

# plt.show()

""" 
Video 4
"""
df = pd.read_csv('stocks/tsla.csv', parse_dates=True, index_col=0)

df_ohlc = df['Adj Close'].resample('10D').ohlc()
df_volume = df['Volume'].resample('10D').sum()

df_ohlc.reset_index(inplace=True)

df_ohlc['Date'] = df_ohlc['Date'].map(mdates.date2num)

ax1 = plt.subplot2grid((6,1), (0,0), rowspan=5, colspan=1)
ax2 = plt.subplot2grid((6,1), (5,0), rowspan=1, colspan=1, sharex=ax1)
ax1.xaxis_date()


candlestick_ohlc(ax1, df_ohlc.values, width=2, colorup='g')
ax2.fill_between(df_volume.index.map(mdates.date2num), df_volume.values, 0)

plt.show()