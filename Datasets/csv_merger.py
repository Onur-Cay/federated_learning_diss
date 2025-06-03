import pandas as pd

# Specify the paths to your CSV files
file1 = './UNSW_NB15_testing-set.csv'
file2 = './UNSW_NB15_training-set.csv'
output_file = './merged_UNSW-NB15.csv'

# Read the first CSV file normally (including the header row)
df1 = pd.read_csv(file1)

# Read the second CSV file normally (including its header row)
df2 = pd.read_csv(file2)

# Remove the first row (header row) from the second DataFrame
df2 = df2.iloc[1:]

# Concatenate the two DataFrames; the header from the first file is retained
merged_df = pd.concat([df1, df2], ignore_index=True)

# Write the merged DataFrame to a new CSV file
merged_df.to_csv(output_file, index=False)

print(f"Merged file saved to {output_file}")
