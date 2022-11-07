
import pandas as pd
import matplotlib.pyplot as plt

# load data
pd_btc_usd = pd.read_csv('pd_btc_usd.csv')

# plot
plt.plot(pd_btc_usd['datetime'],pd_btc_usd['close'])

# labels & title
plt.xlabel('Date')
plt.ylabel('Price (USD)')
plt.title('Price BTC per day of the last 2 years')

# plt.xticks()
plt.show()

# load data
pd_eur_usd = pd.read_csv('pd_eur_usd.csv')

# plot
plt.plot(pd_eur_usd['datetime'],pd_eur_usd['close'])

# labels & title
plt.xlabel('Date')
plt.ylabel('Euro vs Dolar')
plt.title('Price Euro VS Dolar per day of the last 2 years')

# plt.xticks()
plt.show()

# load data
Dow_Jones_Industrial_Average = pd.read_csv('Dow_Jones_Industrial_Average.csv')

# plot
plt.plot(Dow_Jones_Industrial_Average['datetime'],Dow_Jones_Industrial_Average['close'])

# labels & title
plt.xlabel('Date')
plt.ylabel('Dow_Jones_Industrial_Average (USD)')
plt.title('Dow_Jones_Industrial_Average per day of the last 2 years')

# plt.xticks()
plt.show()

# load data
Dow_Jones_Commodity_Index = pd.read_csv('Dow_Jones_Commodity_Index.csv')

# plot
plt.plot(Dow_Jones_Commodity_Index['datetime'],Dow_Jones_Commodity_Index['close'])

# labels & title
plt.xlabel('Date')
plt.ylabel('Dow_Jones_Commodity_Index (USD)')
plt.title('Dow_Jones_Commodity_Index per day of the last 2 years')

# plt.xticks()
plt.show()
