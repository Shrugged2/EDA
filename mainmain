import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
# import statsmodels.formula.api as smf

file_path = '/Users/rick/PycharmProjects/EDA/Final Project/seda_cov_admindist_annual_2024.1.csv'
df = pd.read_csv(file_path)

print("First few rows:")
print(df.head())

print("\nColumn names:")
print(df.columns.tolist())

print(df.head())         # Shows the first 5 rows
print(df.columns)        # Lists all column names
print(df.info())         # Summary of data types and non-null counts
print(df.describe())     # Summary stats for numeric columns


# Find how many missing values are in each column
print(df.isnull().sum())

# Find how many missing values are in each column
print(df.isnull().sum())

# Drop rows with any missing values
df_clean = df.dropna()
print("Cleaned dataset shape:", df_clean.shape)

# Replace 'state' with your actual column name for state
df_sorted = df.sort_values(by='state')
print(df_sorted.head())

# ** To Do List
# Detailed steps:
##### 1: load/read original data
##### 2: clean data
##### 3: summary statistics based on clean data in step  #2
##### 4: clean data with only variables that you will use for your project
# 5: summary statistics based on clean data in step #4
# 6: correlation matrix based on clean data in step #4
# 7: scatter plot of Y and main X1
# 8: linear regression of Y on main X1
# 9: multiple regression of Y on main X1, X2,
# 10: multiple regression of Y on main X1, X2, X3
# 11: multiple regression of Y on main X1, X2, X3, X4
# 12: multiple regression of Y on main X1, X2, X3, X4, X5
# You can have more lines of code if you have run additional regression.

# Y Var = cs_mn_avg_mth_ol
# Against


# trying to find variables
recovery_vars = ['unit', 'year', 'subject', 'subgroup',
                 'growth_1924', 'avg_achv', 'avg_se', 'growth_1924_se',
                 'frpl', 'ell', 'black', 'white', 'hispanic']


df_recovery = df_clean[recovery_vars]
print(df_recovery.head())

