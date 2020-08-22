from SP500_utility import visualise_SP500_heatmap, save_sp500_tickers, get_data_from_yahoo, compile_data
from ml_prediction import do_ml
from utilities import plot_candlestick

ticker = 'MMM'

# --------Plot ticker candlestick with volume-------
plot_candlestick(ticker)

# --------Plot SP500 correlation heatmap-------
# num_of_tickers = 5
# save_sp500_tickers()
# get_data_from_yahoo(num_of_tickers)
# compile_data(num_of_tickers)
visualise_SP500_heatmap()

# # --------Do machine learning to predict buy/sell/hold and get confidence-------
do_ml(ticker)
