
# we using pandas shocker
import pandas as pd
#pyreadstat should be a sufficient package to work with .sav files
import pyreadstat
import os
import sys

# Define the log file path
log_directory = "/Users/rick/Desktop/EDA Exam/logs/"
log_filename = "teacher_output_log.txt"
log_filepath = os.path.join(log_directory, log_filename)

# Ensure the directory exists
os.makedirs(log_directory, exist_ok=True)

# Open log file and redirect print statements
log_file = open(log_filepath, "w")

class Logger:
    def __init__(self, file):
        self.terminal = sys.stdout  # Keep standard output
        self.log = file  # Log file

    def write(self, message):
        self.terminal.write(message)  # Print to console
        self.log.write(message)  # Write to file

    def flush(self):
        pass  # Prevent errors when Python tries to flush a closed file

# Redirect print output to both console and file
sys.stdout = Logger(log_file)



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
# Commenting out a var merge of this data. Im reluctant to delete code especially for somehting like
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

# Define column names
teacher_level_column = "TEALEV"
teacher_level_simple_column = "TEALEV2"

# Define mappings
teacher_level_mapping = {
    1: "Elementary",
    2: "Middle",
    3: "Secondary",
    4: "Other"
}

teacher_level_simple_mapping = {
    1: "Elementary",
    2: "Secondary"
}

# Apply mappings
df_tch["TEACHER_LEVEL"] = df_tch[teacher_level_column].map(teacher_level_mapping)
df_tch["TEACHER_LEVEL_2"] = df_tch[teacher_level_simple_column].map(teacher_level_simple_mapping)

# Count teachers in each category
teacher_level_distribution = df_tch["TEACHER_LEVEL"].value_counts()
teacher_level_simple_distribution = df_tch["TEACHER_LEVEL_2"].value_counts()

# Print distributions
print("\nNumber of Teachers by Level (Detailed):")
print(teacher_level_distribution)

print("\nNumber of Teachers by Level (Elementary vs. Secondary):")
print(teacher_level_simple_distribution)

###### QUESTION 6 ######

# What are their general fields of main assignment (ASSIGN)?

# ASSIGN maps to the following
# 1 = "Prekindergarten, kindergarten, and general elementary"
# 2 = "Math and science"
# 3 = "English/language arts"
# 4 = "Social science"
# 5 = "Special education"
# 6 = "Foreign languages"
# 7 = "Bilingual/ESL education"
# 8 = "Vocational/technical education"
# 9 = "All others"4 = "Long-term substitute (i.e., your assignment requires that you fill the role of a regular
# teacher on a long-term basis, but you are still considered a substitute)"
# 8 = "Administrator (e.g., principal, assistant principal, director, school head)"
# 9 = "Library media specialist or librarian"
# 10 = "Other professional staff (e.g., counselor, curriculum coordinator, social worker)"
# 11 = "Support staff (e.g., secretary)"


assign_mapping = {
    1: "PreK, Kindergarten, General Elementary",
    2: "Math & Science",
    3: "English/Language Arts",
    4: "Social Science",
    5: "Special Education",
    6: "Foreign Languages",
    7: "Bilingual/ESL Education",
    8: "Vocational/Technical Education",
    9: "All Others",
    10: "Long-term Substitute",
    11: "Administrator (Principal, Director, etc.)",
    12: "Library Media Specialist/Librarian",
    13: "Other Professional Staff (Counselor, Social Worker, etc.)",
    14: "Support Staff (Secretary, etc.)"
}

# Apply the mapping
df_tch["MAIN_ASSIGNMENT"] = df_tch["ASSIGN"].map(assign_mapping)

# Count occurrences of each assignment field
assignment_distribution = df_tch["MAIN_ASSIGNMENT"].value_counts()

# Print the assignment distribution
print("\nTeacher Main Assignment Fields:")
print(assignment_distribution)




# Close the log file
log_file.close()