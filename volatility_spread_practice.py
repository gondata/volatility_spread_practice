# Importing the libraries

import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf
from pandas_datareader import data as pdr

yf.pdr_override()

# Getting the data

tickers = ['AAPL', 'TESLA', 'AMZN', 'NFLX', 'GOOG']
startdate = '2020-01-01'
enddate = '2023-03-08'

data = pdr.get_data_yahoo(tickers, start=startdate, end=enddate)['Adj Close']

# Returns

returns = data.pct_change()[1:]

# Variables

period = 100

vol = returns.rolling(period).std() * np.sqrt(period)
vol = vol.iloc[period:]

# Graph

vol.plot(figsize=(10, 8))
plt.title("Volatility Spread")
plt.show()