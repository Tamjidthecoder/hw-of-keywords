import pandas as pd

# Sample data
data = {
    'CustomerID': [1, 2, 3],
    'TotalAmountDue': [1000, 1500, 1200],
    'PaymentsMade': [200, 500, 300]
}

# Create DataFrame
df = pd.DataFrame(data)

# Calculate Due Amount
df['DueAmount'] = df['TotalAmountDue'] - df['PaymentsMade']

print(df)