import pandas as pd

# Read a CSV file from the current workspace
file_path = 'Iris.csv'
df = pd.read_csv(file_path)
print(df.head())