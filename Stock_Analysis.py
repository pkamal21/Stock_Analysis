import pandas as pd
pd.core.common.is_list_like = pd.api.types.is_list_like
import pandas_datareader
import numpy as numpy
import matplotlib.pyplot as plt
import pandas_datareader.data as web
import datetime as datetime

tesla = pd.read_csv("Tesla_Stock.csv")
ford = pd.read_csv("Ford_Stock.csv")
gm = pd.read_csv("GM_Stock.csv")
## Plot for Open Price for all 3 Stocks
# tesla['Open'].plot(label = "Tesla",figsize = (9,5), title = "Open Price")
# ford['Open'].plot(label="Ford")
# gm['Open'].plot(label="GM")
# plt.legend()
# plt.show()


## Plot for Volume traded of all 3 stocks
# tesla['Volume'].plot(label = "Tesla",figsize = (9,5), title = "Volume Traded",alpha=0.3)
# ford['Volume'].plot(label="Ford")
# gm['Volume'].plot(label="GM")
# plt.legend()
# plt.show()


## Plot for total market cap = (volume*open price) for all 3 stocks
# tesla["Total_Traded"] = tesla['Open']*tesla['Volume']
# ford["Total_Traded"] = ford['Open']*ford['Volume']
# gm["Total_Traded"] = gm['Open']*gm['Volume']

# tesla['Total_Traded'].plot(label='Tesla',figsize=(9,5))
# gm['Total_Traded'].plot(label='GM')
# ford['Total_Traded'].plot(label='Ford')
# plt.legend()
# plt.ylabel('Total Traded')
# plt.show()


##Mean average of General Motor Stock
# gm['MA50'] = gm['Open'].rolling(50).mean()
# gm['MA200'] = gm['Open'].rolling(200).mean()
# gm[['Open','MA50','MA200']].plot(label = 'gm',figsize=(9,5))
# plt.show()


##Scatter Matrix to see the relationship between the three "CAR" companies
from pandas.plotting import scatter_matrix
car_comp = pd.concat([tesla['Open'],gm['Open'],ford['Open']],axis=1)
car_comp.columns = ['Tesla Open','GM Open','Ford Open']
scatter_matrix(car_comp,figsize=(5,5),alpha=0.2,hist_kwds={'bins':50});
plt.show()