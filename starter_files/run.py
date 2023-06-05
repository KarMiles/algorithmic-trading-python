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

symbol = 'AAPL'
api_url = f'https://cloud.iexapis.com/stable/stock/{symbol}/quote?token={IEX_CLOUD_API_TOKEN}'

print(api_url)
data = requests.get(api_url).json()
print(data['latestPrice'])
print(data['marketCap'])
