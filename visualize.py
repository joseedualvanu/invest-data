
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