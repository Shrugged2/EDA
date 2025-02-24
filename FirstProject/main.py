
# we using pandas shocker
import pandas as pd
#pyreadstat should be a sufficient package to work with .sav files
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

# Column names
## Commenting out, just what I was using to make sure I had things set up
## print("School Data Columns:", df_sch.columns)
## print("Teacher Data Columns:", df_tch.columns)

# Variable Labels
## Commenting out, just what I was using to make sure I had things set up
## print("School Data Labels:", meta_sch.column_labels)
## print("Teacher Data Labels:", meta_tch.column_labels)


###### MERGE #####
# Commenting out a var merge of this data. Im typically reluctant to delete code especially for somehting like
# class. This is my version of showing my work

# This is going to be for our merge
# Find common columns
common_columns = set(df_sch.columns) & set(df_tch.columns)
print("Common columns:", common_columns)

# if "school_id" in df_sch.columns and "school_id" in df_tch.columns:
#     df_merged = pd.merge(df_sch, df_tch, on="school_id", how="inner")
#     print("Merged Data Preview:")
#     print(df_merged.head())

##### END MERGE #####

##### TEACHER DATASET SECTION #####

# Load the public teacher dataset
file_path_tch = "/Users/rick/Desktop/EDA Exam/tchpub99.sav"
df_tch, meta_tch = pyreadstat.read_sav(file_path_tch)

# Count the number of teachers by counting rows. should be good enough for our purposes here
num_teachers = df_tch.shape[0]

print(f"Total number of public school teachers in the dataset: {num_teachers}")


