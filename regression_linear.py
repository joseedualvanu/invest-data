
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.formula.api import ols
import seaborn as sns
import numpy as np

# load data
pd_btc_usd = pd.read_csv('pd_btc_usd.csv')
pd_btc_usd.sort_values("datetime")
pd_btc_usd_20 = pd_btc_usd.head(20)

pd_eur_usd = pd.read_csv('pd_eur_usd.csv')
pd_eur_usd.sort_values("datetime")
pd_eur_usd_20 = pd_eur_usd.head(20)

dataset = pd.concat([pd_btc_usd_20['close'], pd_eur_usd_20['close']], axis=1, keys=['btc', 'euro_vs_dolar'])

fig = plt.figure()

sns.scatterplot(x="euro_vs_dolar",
                y="btc",
                data=dataset)

# sns.regplot(x="euro_vs_dolar",
#             y="btc",
#             data=dataset)
            # ci=None)
# plt.show()

btc_vs_euro = ols("euro_vs_dolar ~ btc", data=dataset)
mdl_btc_vs_euro = btc_vs_euro.fit()
print(mdl_btc_vs_euro.params)

explanatory_data = pd.DataFrame({'btc': np.arange(18000,23000,100)})
# print(explanatory_data)

prediction_data = mdl_btc_vs_euro.predict(explanatory_data)
# print(prediction_data)

prediction_data = explanatory_data.assign(prediction_data = prediction_data)

# Print the result
# print(prediction_data)

# Add a scatter plot layer to the regplot

sns.scatterplot(x="prediction_data",
                y="btc",
                data=prediction_data,
                color='red')

# Show the layered plot
plt.show()

# Print the coeff of determination for mdl_click_vs_impression_orig
print("R^2 of mdl_btc_vs_euro: " + str(mdl_btc_vs_euro.rsquared))

# Calculate mse_orig for mdl_click_vs_impression_orig
mse_orig = mdl_btc_vs_euro.mse_resid

# Calculate rse_orig for mdl_btc_vs_euro and print it
rse_orig = np.sqrt(mse_orig)
print("RSE of mdl_btc_vs_euro:", rse_orig)

