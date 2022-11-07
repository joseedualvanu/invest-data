import pandas as pd

# load data
Dow_Jones_Industrial_Average = pd.read_csv('Dow_Jones_Industrial_Average.csv',index_col=('datetime'))
# Dow_Jones_Commodity_Index = pd.read_csv('Dow_Jones_Commodity_Index.csv')

# FILTERS

# filter 1: new high
# we select only those stocks that are within 10 percent of their all-time high
Dow_Jones_Industrial_Average_max = Dow_Jones_Industrial_Average['close'].max()
filter1_DJCI = Dow_Jones_Industrial_Average['close'].values[0] > Dow_Jones_Industrial_Average_max*0.9

# filter 2: under 25
# we eliminate all stocks that are priced above 25 usd
filter2_DJIC = Dow_Jones_Industrial_Average['close'].values[0] < 25

# filter 3: EPS80+
# include only those stocks that have an earnings per share rank of 80+

# filter 4: RelStr 90+
# include only those stocks that have a high relative strength figure of 80+

# filter 5: group str A
# include only those stocks with a group of strenght of A

# filter I: 50-day MA
# 50-day moving average 

# filter II: williams %R, dips to -90%
# tracks the overbought and oversold status of an individual stock

# open interest

# action list