import matplotlib.pyplot as plt

def display_output(valid_tickers, optimal_portfolio, portfolio_return, portfolio_std_dev):
    print("Optimal portfolio weights:") 
    for i in range(len(valid_tickers)): 
        print(f"{valid_tickers[i]:<5}: {optimal_portfolio.x[i] * 100:.2f}%")
    print() 

    print("Portfolio Optimized!")
    print(f"Portfolio return: {portfolio_return * 100:.4f}%")
    print(f"Portfolio standard deviation: {portfolio_std_dev * 100:.4f}%")

def plot_portfolio(valid_tickers, optimal_portfolio, portfolio_return, portfolio_std_dev):
    # Create a dictionary for holding the ticker and its corresponding weight
    weights = {valid_tickers[i]: optimal_portfolio.x[i] for
               i in range(len(valid_tickers))}

    # Create a pie chart
    plt.figure(figsize=(10,7))
    plt.pie(weights.values(), labels=weights.keys(), autopct='%1.1f%%')
    plt.title(f'Portfolio Composition\nExpected Return: {portfolio_return * 100:.2f}%\nStandard Deviation: {portfolio_std_dev * 100:.2f}%')
    plt.show()
