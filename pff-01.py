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
# # df = web.get_data_yahoo('GOOG', start, end)
# df = web.DataReader('TSLA', 'yahoo', start, end)

# print(df.tail(10))

"""
Video 1 (CON MORNINGSTAR - Alternativa del autor)
"""
# start = datetime.datetime(2015, 1, 1)
# end = datetime.datetime.now()
# df = web.DataReader("TSLA", 'morningstar', start, end)
# df.reset_index(inplace=True)
# df.set_index("Date", inplace=True)
# df = df.drop("Symbol", axis=1)

# print(df.head())

"""
Video 1 (CON ROBIN HOOD - Alternativa de usuario 'The Urbanist')
"""
# df = web.DataReader('CNP', 'robinhood', start, end)
# df.reset_index(inplace=True)
# df.drop(['symbol', 'interpolated', 'session'], axis=1, inplace=True)
# df.rename(index=str, columns={'close_price': 'Close', 
#                              'high_price': 'High',
#                              'low_price': 'Low',
#                              'open_price': 'Open',
#                              'volume': 'Volume',
#                              'begins_at': 'Date'}, inplace=True)
# df.set_index('Date', inplace=True)
# print(df.head())

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
Video 5
"""
import bs4 as bs
import pickle
import requests

def save_sp500_tickers():
    resp = requests.get('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
    soup = bs.BeautifulSoup(resp.text, 'lxml')
    table = soup.find('table', {'class':'wikitable sortable'})
    tickers = []
    for row in table.findAll('tr')[1:]:
        ticker = row.findAll('td')[0].text
        tickers.append(ticker)
    
    with open("sp500tickers.pickle", "wb") as f:
        pickle.dump(tickers, f)
    
    print(tickers)
    return tickers

save_sp500_tickers()
