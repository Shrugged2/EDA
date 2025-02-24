# we using pandas shocker
import pandas as pd
#pyreadstat should be a sufficient package to work with .sav files
import pyreadstat

# File paths
file_path_sch = "/Users/rick/Desktop/EDA Exam/schpub99.sav"

# Load the .sav files
df_sch, meta_sch = pyreadstat.read_sav(file_path_sch)

# Display the first few rows of each dataframe
print("School Data (schpub99.sav):")
print(df_sch.head())

