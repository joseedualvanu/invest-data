

from twelvedata import TDClient
td = TDClient(apikey="c5ad74d6f4b54af39158780fa621e78d") 


# ts.with_macd().with_ema(time_period=20).with_ema(time_period=50).as_csv()


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



