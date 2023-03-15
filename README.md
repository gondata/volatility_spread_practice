# Financial Asset Portfolio Volatility Analysis with Python

This repository contains a Python script that uses the `numpy`, `matplotlib`, `yfinance`, and `pandas-datareader` libraries to perform an analysis of the volatility of a financial asset portfolio.

## How the code works

The script downloads the adjusted closing prices of a financial asset portfolio (AAPL, TESLA, AMZN, NFLX, GOOG) from January 1st, 2020 to March 8th, 2023 using `yfinance` and `pandas-datareader`. It then calculates the annualized volatility of the portfolio using the rolling standard deviation formula and plots the results using `matplotlib`.

## How to use the code

1. Clone this repository to your local machine.
2. Make sure you have the required libraries (`numpy`, `matplotlib`, `yfinance`, and `pandas-datareader`) installed.
3. Run the script using `python volatility_analysis.py`.
4. The script will output a plot of the volatility spread of the financial asset portfolio.

Feel free to modify the script to fit your own needs, such as using a different portfolio or adjusting the time period. Enjoy!
