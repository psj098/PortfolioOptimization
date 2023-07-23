# Portfolio Optimization Tool

This project implements a portfolio optimization tool based on Modern Portfolio Theory, developed by Harry Markowitz. The tool utilizes historical stock data from three key indices - S&P 500, Nasdaq Composite, and Dow Jones Industrial Average (DJIA), to calculate optimal portfolio weights. These weights aim to mitigate portfolio risk while securing a specified expected return.

## Features

- <b>Custom Stock Selection</b>: Users can input their preferred stock tickers to tailor the portfolio.
- <b>Defined Weight Allocations</b>: Users can set a desired minimum weight allocation for each stock in the portfolio.
- <b>Expected Return</b>: The tool calculates the range of possible returns, taking into account the minimum weights, and requests the user to indicate the desired expected return.
- <b>Optimal Portfolio Composition</b>: Utilizing mathematical optimization techniques with the `scipy` library, the tool determines the optimal portfolio composition that achieves the user's desired return while reducing portfolio risk.
- <b>Portfolio Weight Constraints</b>: The tool ensures that the sum of the weights of all stocks in the portfolio equals 1 and that no individual weight is less than the user-defined minimum.
- <b>Reliable Data Source</b>: Historical stock data is procured from the `yahoo_fin` library.

## How to Use

1. Run the script in Python.
2. When prompted, enter the tickers of the stocks you're interested in.
3. When prompted, enter the minimum weight for each stock (each between 0 and 1, with their sum totaling up to less than 1).
4. When prompted, enter the desired expected return (between the calculated minimum and maximum possible returns).
5. The script will print out the optimal weights for the portfolio, along with the portfolio's expected return and associated standard deviation.

Please note that this script assumes the user has a basic understanding of financial markets and Modern Portfolio Theory. It is important to emphasize that this tool should not be used as financial advice.

#### Usage Example
Number of stocks in S&P 500: 503<br>
Number of stocks in Nasdaq Composite: 5181<br>
Number of stocks in DJIA: 30

Tickers of the stocks (separated by space): AAPL MSFT NVDA AMZN KO GOOG MA JPM META TSLA<br>
Enter min. weight for AAPL (0 - 1): 0.03<br>
Enter min. weight for AMZN (0 - 1): 0.04<br>
Enter min. weight for NVDA (0 - 1): 0.05<br>
Enter min. weight for KO (0 - 1): 0.10<br>
Enter min. weight for MA (0 - 1): 0.01<br>
Enter min. weight for GOOG (0 - 1): 0.02<br>
Enter min. weight for TSLA (0 - 1): 0.05<br>
Enter min. weight for MSFT (0 - 1): 0.05<br>
Enter min. weight for JPM (0 - 1): 0.02<br>
Enter min. weight for META (0 - 1): 0.03

Enter desired expected return (between 0.1521 and 0.4717): 0.28

Optimal portfolio weights:<br>
AAPL : 9.12%<br>
AMZN : 9.84%<br>
NVDA : 12.92%<br>
KO   : 14.95%<br>
MA   : 6.70%<br>
GOOG : 7.54%<br>
TSLA : 11.69%<br>
MSFT : 11.04%<br>
JPM  : 7.21%<br>
META : 8.99%

Portfolio Optimized!<br>
Portfolio return: 28.0000%<br>
Portfolio standard deviation: 2.4073%

![portfolio-optimization-result](https://raw.githubusercontent.com/psj098/PortfolioOptimization/master/portfolio_pie_chart.png)



