
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# load data
pd_btc_usd = pd.read_csv('pd_btc_usd.csv')
pd_eur_usd = pd.read_csv('pd_eur_usd.csv')

# np_close_btc_usd = np.array(pd_btc_usd['close'])
# np_close_eur_usd = np.array(pd_eur_usd['close'])

print(pd_btc_usd.describe())
print(pd_eur_usd.describe())