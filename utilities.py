import os
import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas_datareader.data as web
from matplotlib import style
from mpl_finance import candlestick_ohlc


def download_data_from_yahoo(ticker):
    start = dt.datetime(2000,1,1)
    end = dt.datetime.now()
    df = web.DataReader(ticker, 'yahoo', start, end)

    if not os.path.exists('stock_data'):
        os.makedirs('stock_data')

    df.to_csv('stock_data/{}.csv'.format(ticker))

    return df


def read_company_csv(ticker):
    df = pd.read_csv('stock_data/{}.csv'.format(ticker), parse_dates=True, index_col=0)

    return df


def plot_candlestick(ticker):
    download_data_from_yahoo(ticker)
    df = read_company_csv(ticker)
    style.use('ggplot')

    # Create new data frame ohlc (re-sample 10Days)-------------------------------------------------------------------
    df_ohlc = df['Adj Close'].resample('10D').ohlc()

    # Reset Index (0,1,2...)-------------------------------------------------------------------
    df_ohlc.reset_index(inplace=True)

    # Change Date to mdates-------------------------------------------------------------------
    df_ohlc['Date'] = df_ohlc['Date'].map(mdates.date2num)

    # Create new data frame for Volume-------------------------------------------------------------------
    df_volume = df['Volume'].resample('10D').sum()

    # Draw Grids-------------------------------------------------------------------
    ax1 = plt.subplot2grid((6, 1), (0, 0), rowspan=5, colspan=1)
    ax2 = plt.subplot2grid((6, 1), (5, 0), rowspan=1, colspan=1, sharex=ax1)

    # X-axis: date-------------------------------------------------------------------
    ax1.xaxis.set_major_formatter(mdates.DateFormatter('%d-%m-%Y'))

    # Create candlestick-------------------------------------------------------------------
    candlestick_ohlc(ax1, df_ohlc.values, width=2, colorup='g')

    # Volume on second grid -------------------------------------------------------------------
    ax2.fill_between(df_volume.index.map(mdates.date2num), df_volume.values, 0)

    plt.xlim(df_volume.index.map(mdates.date2num)[0], df_volume.index.map(mdates.date2num)[-1])
    plt.show()






