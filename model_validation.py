import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import numpy as np

# load data
pd_btc_usd = pd.read_csv('pd_btc_usd.csv')
pd_eur_usd = pd.read_csv('pd_eur_usd.csv')

pd_btc_usd.sort_values("datetime")
pd_eur_usd.sort_values("datetime")

pd_btc_usd_20 = pd_btc_usd.head(20)
pd_eur_usd_20 = pd_eur_usd.head(20)

X = pd_eur_usd_20["close"].values
X_shape = X.reshape(-1,1)
y = pd_btc_usd_20["close"].values
y_shape = y.reshape(-1,1)

reg = LinearRegression()
reg.fit(X_shape,y)
y_pred = reg.predict(X_shape)
y_pred_shape = y_pred.reshape(-1,1)

# Compute R-squared
r_squared = reg.score(X_shape, y_pred_shape)

# Compute RMSE
rmse = mean_squared_error(y_pred, y_pred_shape, squared=False)

# Print the metrics
print("R^2: {}".format(r_squared))
print("RMSE: {}".format(rmse))

from sklearn.model_selection import cross_val_score, KFold
kf = KFold(n_splits=4, shuffle=True, random_state=42)

cv_results = cross_val_score(reg, X_shape, y_shape, cv=kf)

# Print the mean
print(np.mean(cv_results))

# Print the standard deviation
print(np.std(cv_results))

# Print the 95% confidence interval
print(np.quantile(cv_results, [0.025, 0.975]))