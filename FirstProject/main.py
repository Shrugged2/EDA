# Import essential libraries
import pandas as pd
# import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Replace Placeholder Values:
# Replace 'your_file.csv' with the name or path to your dataset.
# Update 'your_column_here' in the visualize_data function call with a column name from your dataset for visualization.

# Function to load data
def load_data(file_path):
    """
    Load data from SPSS file.
    """
    try:
        data = pd.read_csv(/Users/rick/Desktop/EDA Exam)
        print(f"Data loaded successfully with {data.shape[0]} rows and {data.shape[1]} columns.")
        return data
    except Exception as e:
        print(f"Error loading data: {e}")
        return None

# Function to display basic dataset information
def dataset_summary(data):
    """
    Print summary statistics and information about the dataset.
    """
    print("Dataset Info:")
    print(data.info())
    print("\nSummary Statistics:")
    print(data.describe())
    print("\nMissing Values:")
    print(data.isnull().sum())

# Function to visualize data
def visualize_data(data, column):
    """
    Create visualizations for a specified column.
    """
    try:
        plt.figure(figsize=(10, 6))
        sns.histplot(data[column], kde=True)
        plt.title(f"Distribution of {column}")
        plt.show()
    except Exception as e:
        print(f"Error visualizing data: {e}")

# Function to clean data
def clean_data(data):
    """
    Handle missing values and perform basic cleaning.
    """
    data_cleaned = data.dropna()  # Example: Dropping rows with missing values
    print(f"Data cleaned. Rows before: {data.shape[0]}, Rows after: {data_cleaned.shape[0]}")
    return data_cleaned

# Main analysis workflow
def main(file_path):
    """
    Main workflow for data analysis project.
    """
    # Load the dataset
    data = load_data(file_path)

    if data is not None:
        # Summarize the dataset
        dataset_summary(data)

        # Example visualization
        # Update 'column_name' to match a column in your dataset
        column_name = 'your_column_here'
        if column_name in data.columns:
            visualize_data(data, column_name)
        else:
            print(f"Column '{column_name}' not found in dataset.")

        # Clean the dataset
        data_cleaned = clean_data(data)

        # Save cleaned data
        data_cleaned.to_csv('cleaned_data.csv', index=False)
        print("Cleaned data saved to 'cleaned_data.csv'.")

# Run the script (replace 'your_file.csv' with your dataset file path)
if __name__ == "__main__":
    main('your_file.csv')
