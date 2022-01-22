# #importing the required librabies
# import datetime as dt
# import pandas_datareader as web
# import matplotlib.pyplot as plt
# import matplotlib.dates as mdates
# from mpl_finance import candlestick_ohlc

# start = dt.datetime(2021,1,1)
# end = dt.datetime.now()

# stock_name=input("ENTER THE STOCK NAME::")
# data = web.DataReader(stock_name,'yahoo',start,end)
# print(data.columns)
# data = data [['Open','High','Low','Close']]
# data.reset_index(inplace=True)
# data['Date']=data['Date'].map(mdates.date2num)

# ax = plt.subplot()
# ax.grid(True)
# ax.set_axisbelow(True)
# ax.set_facecolor('black')
# ax.figure.set_facecolor('#121212')
# ax.tick_params(axis='x',colors='white')
# ax.tick_params(axis='y',colors='white')
# ax.xaxis_date()
# candlestick_ohlc(ax, data.values, width=0.5,colorup='#00ff00')
# plt.show()






# import cv2 as cv

# immg = cv.imread('img.png')
# cv.imshow('img',immg)
# cv.waitKey(0)