import pandas as pd

# Define the data as a dictionary
data = {
    'Apples': [35, 41],
    'Bananas': [21, 34]
}

# Define the index (years) for the DataFrame
index = ['2017 Sales', '2018 Sales']

# Create the DataFrame
df = pd.DataFrame(data, index=index)

# Write the DataFrame to a CSV file
csv_file_path = 'fruit.csv'
df.to_csv(csv_file_path)

print(f"Data has been written to {csv_file_path}")
