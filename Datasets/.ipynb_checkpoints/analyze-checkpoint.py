#!/usr/bin/env python3
import pandas as pd
import sys

def main():
    # Change the file path to your CSV file
    file_path = ['merged_UNSW-NB15.csv','UNSW_NB15_testing-set.csv','UNSW_NB15_training-set.csv']
    total_row = 0
    for counter,file in enumerate(file_path,start = 0):
        try:
            # Load the CSV file
            df = pd.read_csv(file)
            print("Reading: ",file)
        except Exception as e:
            print(f"Error reading the file: {e}")
            sys.exit(1)
        
        # Print dataset shape
        rows = 0
        cols = 0
        rows, cols = df.shape
        if counter >= 1:
            total_row = total_row + rows
        print(f"Dataset contains {rows} rows and {cols} columns.\n")
        
        # Display each column and its unique values.
        print("Columns and their unique values:")
        for col in df.columns:
            unique_vals = df[col].unique()
            # If too many unique values, display only the count
            if len(unique_vals) > 20:
                print(f"Column '{col}': {len(unique_vals)} unique values")
            else:
                print(f"Column '{col}': {unique_vals}")
        print("\n")
        
        # Calculate and print the percentage of 1's and 0's in the 'label' column
        label_field = "label"
        if label_field in df.columns:
            label_counts = df[label_field].value_counts()
            total = label_counts.sum()
            percents = (label_counts / total * 100).round(2)
            print(f"Label distribution in '{label_field}':")
            for label, count in label_counts.items():
                print(f"Label {label}: {count} ({percents[label]}%)")
        else:
            print(f"Column '{label_field}' not found in the dataset.")
    print("Total Rows=",total_row)

if __name__ == '__main__':
    main()
