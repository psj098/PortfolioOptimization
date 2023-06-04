def display_output(valid_tickers, optimal_portfolio,
                   portfolio_return, portfolio_std_dev):
    print("Optimal portfolio weights:") 
    for i in range(len(valid_tickers)): 
        print(f"{valid_tickers[i]:<5}: {optimal_portfolio.x[i] * 100:.2f}%")
    print() 

    print("Portfolio Optimized!")
    print(f"Portfolio return: {portfolio_return * 100:.4f}%")
    print(f"Portfolio standard deviation: {portfolio_std_dev * 100:.4f}%")
