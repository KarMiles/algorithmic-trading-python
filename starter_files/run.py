import numpy as np  # The Numpy numerical computing library
import pandas as pd  # The Pandas data science library
import requests  # The requests library for HTTP requests in Python
import xlsxwriter  # The XlsxWriter libarary for
import math  # The Python math module

import sys
sys.path.append("starter_files")

from secrets_starter_files import IEX_CLOUD_API_TOKEN

stocks = pd.read_csv('./starter_files/sp_500_stocks.csv')
# print(type(stocks))

# print(IEX_CLOUD_API_TOKEN)


# Making Our First API Call
symbol = 'AAPL'
api_url = f'https://cloud.iexapis.com/stable/stock/{symbol}/quote?token={IEX_CLOUD_API_TOKEN}'
# print(api_url)
data = requests.get(api_url).json()
# print(type(data))

# Parsing Our API Call
# print(data)
price = data['latestPrice']
market_cap = data['marketCap']
# print(market_cap/1000000000000)

# Adding Our Stocks Data to a Pandas DataFrame
my_columns = [
    'Ticker',
    'Price',
    'Market Capitalization',
    'Number Of Shares to Buy']

final_dataframe = pd.DataFrame(columns=my_columns)

# Create a new row to add to the DataFrame
new_row = pd.Series([symbol, price, market_cap, 'N/A'], index=my_columns)

# Concatenate the new row DataFrame with the final_dataframe
final_dataframe = pd.concat(
    [final_dataframe, new_row],
    ignore_index=True
    )


print()
print('final_dataframe: ')
print(final_dataframe)
