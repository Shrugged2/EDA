
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

## QUESTION 1
# Count the number of teachers by counting rows. should be good enough for our purposes here
num_teachers = df_tch.shape[0]

print(f"Total number of public school teachers in the dataset: {num_teachers}")

## QUESTION 2, 3, 4
#Define the gender, and race columns based on file layout information and pdf (https://nces.ed.gov/surveys/sass/pdf/PublicTeacher/tchpub99_layout.pdf)

# Load the dataset
file_path_tch = "/Users/rick/Desktop/EDA Exam/tchpub99.sav"
df_tch, meta_tch = pyreadstat.read_sav(file_path_tch)

# Define column names
gender_column = "T0356"
race_column = "T0357"
hispanic_column = "T0359"
age_column = "AGE_T"


# Define mappings
gender_mapping = {1: "Male", 2: "Female"}
race_mapping = {
    1: "American Indian/Alaska Native",
    2: "Asian",
    3: "Black",
    4: "White"
}
hispanic_mapping = {1: "Yes", 2: "No"}

# Apply mappings
df_tch[gender_column] = df_tch[gender_column].map(gender_mapping)
df_tch[race_column] = df_tch[race_column].map(race_mapping)
df_tch[hispanic_column] = df_tch[hispanic_column].map(hispanic_mapping)

# Count occurrences
gender_counts = df_tch[gender_column].value_counts()
race_counts = df_tch[race_column].value_counts()
hispanic_counts = df_tch[hispanic_column].value_counts()
age_summary = df_tch[age_column].value_counts()

# Display results
print("\nTeacher Gender Distribution:")
print(gender_counts)

print("\nTeacher Race Distribution:")
print(race_counts)

print("\nTeacher Hispanic Identification Distribution:")
print(hispanic_counts)

print("\nTeacher Age Summary:")
print(age_summary)


# AGE_T
# 1 = "Less than 30 years"
# 2 = "30 to 39 years"
# 3 = "40 to 49 years"
# 4 = "50 years or older"
# Define the correct age group mapping and apply to summary
age_mapping = {
    1: "Less than 30 years",
    2: "30 to 39 years",
    3: "40 to 49 years",
    4: "50 years or older"
}

# Apply the mapping
df_tch["AGE_GROUP"] = df_tch["AGE_T"].map(age_mapping)
# Count occurrences of each age group
age_distribution = df_tch["AGE_GROUP"].value_counts().sort_index()
# Print the age distribution table
print("\nPublic School Teachers' Age Distribution:")
print(age_distribution)

##### QUESTION 5 #####
# How many teachers are teaching elementary school, middle school, and high school teachers?

