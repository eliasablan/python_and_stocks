import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web

style.use('ggplot')

# start = dt.datetime(2015,1,1)
# end = dt.datetime(2019,5,25)
# df = web.DataReader('TSLA', 'yahoo', start, end)

# df.to_csv('files/tsla.csv')
df = pd.read_csv('files/tsla.csv', parse_dates=True, index_col=0)

# print(df.head())

# column_values_df = df['High']
# subset = df[['High', 'Low']]
# loc = df.loc[df.shape[0]-1]
# shape = df.shape[0]

# print(shape)

df['Adj Close'].plot()
plt.show()