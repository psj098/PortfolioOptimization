import pickle
import yahoo_fin.stock_info as si
from yahoo_fin.stock_info import get_data

# Getting list of tickers for S&P 500, Nasdaq Composite and DJIA 
def get_tickers():
    sp500_list = si.tickers_sp500() 
    nasdaq_list = si.tickers_nasdaq() 
    dow_list = si.tickers_dow()
    combined_list = list(set(sp500_list + nasdaq_list + dow_list))
    print(f"Number of stocks in S&P 500: {len(sp500_list)}")
    print(f"Number of stocks in Nasdaq Composite: {len(nasdaq_list)}")
    print(f"Number of stocks in DJIA: {len(dow_list)}") 
    print()
    return combined_list

# Fetching historical data for each ticker
def fetch_historical_data(combined_list, date_start, date_today):
    h_data = {} 
    for ticker in combined_list: 
        try: 
            temp_data = get_data(ticker, start_date=date_start,
                                 end_date=date_today, index_as_date=False,
                                 interval="1wk") 
            if not (temp_data['date'].iloc[-1] == temp_data['date'].iloc[0]): 
                h_data[ticker] = temp_data 
                print(f"Fetching data for {ticker}")
        except Exception as e: 
            print(f"Could not fetch data for {ticker}, Error {e}")
    return h_data

# Method to fetch saved historical data
def fetch_saved_data():
    with open(
        'C:\\Users\\sjpar\\Desktop\\iCloudDrive\\DataProject2\\h_data.pkl',
        'rb') as f:
        h_data = pickle.load(f)
    return h_data

