def prepare_portfolio_data(return_risk_data, valid_tickers, return_df):
    # Return and risk data for valid tickers 
    return_data = [return_risk_data[ticker][0] for ticker in valid_tickers]
    risk_data = [return_risk_data[ticker][1] for ticker in valid_tickers]

    # Covariance matrix for valid tickers only 
    cov_matrix_input = return_df[valid_tickers].cov() 

    return return_data, risk_data, cov_matrix_input
