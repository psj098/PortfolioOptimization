from dateutil.relativedelta import relativedelta
import pandas as pd 
import numpy as np 

def calculate_risk_return(data):
    # Initialize dictionary to store return & risk data for each ticker 
    return_risk_data = {} 

    # Initialize dataframe to store return data for each ticker
    return_df = pd.DataFrame() 

    for ticker in data: 
        # Calculate annual return 
        time_difference = relativedelta(data[ticker]['date'].iloc[-1],
                                        data[ticker]['date'].iloc[0])
        duration = round(time_difference.years + time_difference.months/12 + 
                         time_difference.days/365, 3)
        annual_return = (data[ticker]['adjclose'].iloc[-1] /
                         data[ticker]['adjclose'].iloc[0]) ** (1/duration) - 1 
        
        # Calculate annual risk 
        returns = data[ticker]['adjclose'].pct_change().dropna() 
        risk = returns.std() 
        annual_risk = risk * np.sqrt(52) 
        
        return_df[ticker] = returns 
        
        return_risk_data[ticker] = (annual_return, annual_risk)

    return return_risk_data, return_df
