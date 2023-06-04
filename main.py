"""
main.py: A portfolio optimization tool using Modern Portfolio Theory.
The script fetches historical stock data, takes user input for desired tickers
and minimum weights, calculates possible return range and optimizes portfolio
composition to achieve user's desired return while minimizing portfolio risk.
"""

import warnings
from data import get_tickers, fetch_historical_data, fetch_saved_data
from date import get_date
from risk_return import calculate_risk_return
from user_input import get_user_input
from prepare_data import prepare_portfolio_data
from input_processing import calculate_return_range, get_user_desired_return
from portfolio_optimize import optimize
from results import display_output, plot_portfolio

warnings.filterwarnings('ignore')

def main(): 
    # Retrieve tickers for S&P 500, NASDAQ Composite, and DJIA
    combined_list = get_tickers()

    # Define date range for historical data
    date_start, date_today = get_date()

    # Load historical data fetched from Yahoo Finance API or from pickle file)
    # h_data = fetch_historical_data(combined_list, date_start, date_today)
    h_data = fetch_saved_data()

    # Calculate return and risk data for each ticker
    return_risk_data, return_df = calculate_risk_return(h_data)

    # Get user input for desired tickers and minimum weights
    valid_tickers, min_weights = get_user_input(return_risk_data)

    # Prepare portfolio data for optimization
    return_data, risk_data, cov_matrix_input = prepare_portfolio_data(
        return_risk_data, valid_tickers, return_df)

    # Calculate possible return range based on user-inputted minimum weights
    min_return, max_return = calculate_return_range(
        min_weights, return_risk_data, valid_tickers, return_data)

    # Get user's desired expected return within the calculated range
    user_return = get_user_desired_return(min_return, max_return)

    # Optimize portfolio based on user's input and calculated data
    optimal_portfolio, portfolio_return, portfolio_std_dev = optimize(
        min_weights, valid_tickers, cov_matrix_input, return_data, user_return)

    # Display portfolio optimization results 
    display_output(valid_tickers, optimal_portfolio,
                   portfolio_return, portfolio_std_dev)
    
    # Plot portfolio optimization results 
    plot_portfolio(valid_tickers, optimal_portfolio,
                   portfolio_return, portfolio_std_dev)

if __name__ == "__main__": 
    main()
