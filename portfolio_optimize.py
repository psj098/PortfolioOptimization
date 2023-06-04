from scipy.optimize import minimize, Bounds
import numpy as np

def optimize(min_weights, valid_tickers, cov_matrix_input,
             return_data, user_return):
    # Define the objective function
    def objective(weights):
        return np.dot(weights.T, np.dot(cov_matrix_input, weights))

    # Initial guess for weights of portfolio: weight for each ticker set to 
    # minimum weight (min_weights[ticker]) and remaining weight distributed 
    # equally among rest of tickers 
    weights_guess = [min_weights[ticker] + (1 - sum(min_weights.values())) /
                     len(valid_tickers) for ticker in valid_tickers]

    # Lower bound for weights set to minimum weight (min_weights[ticker]) 
    # Upper bound is set to 1.0  
    bounds = Bounds([min_weights[ticker] for ticker in valid_tickers],
                    [1.0]*len(valid_tickers))

    # Define constraints:
    # 1. Weights sum up to 1 
    # 2. Portfolio return equal to user's desired return 
    constraints = [{'type': 'eq', 'fun': lambda x: np.sum(x) - 1}, 
                   {'type': 'eq', 'fun': lambda x: 
                       np.dot(x, return_data) - user_return}]

    # Solve the optimization problem
    optimal_portfolio = minimize(fun=objective, x0=weights_guess,
                                 method='SLSQP', bounds=bounds,
                                 constraints=constraints)
    
    # Calculate portfolio return and standard deviation 
    portfolio_return = np.dot(optimal_portfolio.x, return_data)
    portfolio_variance = np.dot(optimal_portfolio.x.T, np.dot(
        cov_matrix_input,optimal_portfolio.x))
    portfolio_std_dev = np.sqrt(portfolio_variance)

    return optimal_portfolio, portfolio_return, portfolio_std_dev
