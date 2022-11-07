
# the idea es to get information from https://twelvedata.com/

# libraries
import pandas as pd
from twelvedata import TDClient

# read the key for the API
with open('key.txt') as f:
    key = f.readlines()[0]
    
# initialize the API
td = TDClient(apikey=key) 
    
# load data
pd_btc_usd = td.time_series(
    symbol="BTC/USD",
    interval="1day",
    outputsize=730
    ).as_pandas()
pd_btc_usd.to_csv('pd_btc_usd.csv')

pd_eur_usd = td.time_series(
    symbol="EUR/USD",
    interval="1day",
    outputsize=730
    ).as_pandas()
pd_eur_usd.to_csv('pd_eur_usd.csv')

pd_btc_usd = pd.read_csv('pd_btc_usd.csv')
pd_eur_usd = pd.read_csv('pd_eur_usd.csv')

# check max date
print(pd_eur_usd.datetime.max())
print(pd_btc_usd.datetime.max())

# load data
Dow_Jones_Commodity_Index = td.time_series(
    symbol="DJCI",
    interval="1day",
    outputsize=730
    ).as_pandas()
Dow_Jones_Commodity_Index.to_csv('Dow_Jones_Commodity_Index.csv')

Dow_Jones_Industrial_Average = td.time_series(
    symbol="DJCI",
    interval="1day",
    outputsize=730
    ).as_pandas()
Dow_Jones_Industrial_Average.to_csv('Dow_Jones_Industrial_Average.csv')

# check max date
Dow_Jones_Industrial_Average    = pd.read_csv('Dow_Jones_Commodity_Index.csv')
Dow_Jones_Commodity_Index       = pd.read_csv('Dow_Jones_Industrial_Average.csv')

print(Dow_Jones_Industrial_Average.datetime.max())
print(Dow_Jones_Commodity_Index.datetime.max())