import pandas as pd
import numpy as np
import statsmodels.api as sm

# Sample Data: Replace this with your actual dataset
data = {
    'Active Users': [200, 300, 250, 400, 150, 350, 500],
    'Network Latency (ms)': [20, 30, 25, 40, 15, 35, 45],
    'CPU Usage (%)': [65, 75, 70, 85, 60, 80, 90],
    'Memory Utilization (%)': [70, 80, 75, 90, 65, 85, 95],
    'Response Time (s)': [1.2, 1.8, 1.5, 2.5, 1.1, 2.0, 2.7]
}

# Creating a DataFrame
df = pd.DataFrame(data)

# Define independent variables (X) and dependent variable (Y)
X = df[['Active Users', 'Network Latency (ms)', 'CPU Usage (%)', 'Memory Utilization (%)']]
Y = df['Response Time (s)']

# Add a constant (intercept) to the independent variables
X = sm.add_constant(X)

# Perform the regression analysis
model = sm.OLS(Y, X).fit()

# Print out the regression analysis summary
print(model.summary())
