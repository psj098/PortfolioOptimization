# Portfolio Optimization Tool

This project implements a portfolio optimization tool based on Modern Portfolio Theory, developed by Harry Markowitz. The tool uses historical stock data from S&P 500, Nasdaq Composite, and Dow Jones Industrial Average (DJIA) to calculate the optimal portfolio weights that minimize portfolio risk for a given expected return.

## Features

- User provides a list of stock tickers and their desired minimum weight allocation for each stock in their portfolio.
- The tool determines the range of possible returns based on the minimum weights and prompts the user to specify the desired expected return.
- Mathematical optimization techniques, utilizing the `scipy` library, are employed to determine the optimal portfolio composition that achieves the user's desired return while minimizing portfolio risk.
- The tool enforces constraints such as ensuring the sum of weights for all stocks in the portfolio adds up to 1 and no individual weight falls below the user-defined minimum.
- Historical stock data is fetched from the `yahoo_fin` library.

## How to Use

1. Run the script in Python.
2. When prompted, enter the tickers of the stocks you're interested in.
3. When prompted, enter the minimum weight for each stock (each between 0 and 1, with their sum totaling up to less than 1).
4. When prompted, enter the desired expected return (between the calculated minimum and maximum possible returns).
5. The script will print out the optimal weights for the portfolio, along with the portfolio's expected return and associated standard deviation.

Please note that this script assumes the user has a basic understanding of financial markets and Modern Portfolio Theory. It is important to emphasize that this tool should not be used as financial advice.
