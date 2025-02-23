import pandas as pd
import pyreadstat

# File paths
file_path_sch = "/Users/rick/Desktop/EDA Exam/schpub99.sav"
file_path_tch = "/Users/rick/Desktop/EDA Exam/tchpub99.sav"

# Load the .sav files
df_sch, meta_sch = pyreadstat.read_sav(file_path_sch)
df_tch, meta_tch = pyreadstat.read_sav(file_path_tch)

# Display the first few rows of each dataframe
print("School Data (schpub99.sav):")
print(df_sch.head())

print("\nTeacher Data (tchpub99.sav):")
print(df_tch.head())
