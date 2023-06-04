def get_user_input(return_risk_data):
    user_input = input("Tickers of the stocks (separated by space): ")
    tickers = list(set(user_input.split()))

    # Check that user input contains valid tickers 
    valid_tickers = [ticker for ticker in tickers if
                     ticker in return_risk_data]
    if len(valid_tickers) < len(tickers): 
        diff = len(tickers) - len(valid_tickers)
        print(f"Warning: {diff} tickers not found in data", end="\n\n")

    # Ask user for minimum weights
    min_weights = {}
    for ticker in valid_tickers:
        min_weight = float(input(f"Enter min. weight for {ticker} (0 - 1): "))
        min_weights[ticker] = min_weight
    assert sum(min_weights.values()) <= 1, "Error: Sum of minimum weight > 1"
    print() 

    return valid_tickers, min_weights
