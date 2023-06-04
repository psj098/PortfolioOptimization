def calculate_return_range(min_weights, return_risk_data,
                                    valid_tickers, return_data):
    # Find range of possible return considering the minimum weights 
    min_return = sum([min_weights[ticker] * return_risk_data[ticker][0] for
                      ticker in valid_tickers]) + min(return_data) *\
                          (1-sum(min_weights.values())) 
    max_return = sum([min_weights[ticker] * return_risk_data[ticker][0] for
                      ticker in valid_tickers]) + max(return_data) *\
                          (1-sum(min_weights.values()))
    return min_return, max_return

def get_user_desired_return(min_return, max_return):
    # Ask user for desired return
    user_return = float(input(f"Enter desired expected return (between "
                              f"{min_return:.4f} and {max_return:.4f}): "))
    print() 
    assert min_return <= user_return <= max_return, "User return out of range" 
    return user_return
