# we using pandas shocker
import pandas as pd
#pyreadstat should be a sufficient package to work with .sav files
import pyreadstat
import sys
import os

###### DONT FORGET TO UNCOMMENT WHEN FINISHED #####
# Define the log file path
log_directory = "/Users/rick/Desktop/EDA Exam/logs/"
log_filename = "school_output_log.txt"
log_filepath = os.path.join(log_directory, log_filename)

# Ensure the directory exists
os.makedirs(log_directory, exist_ok=True)

# Open log file and redirect print statements
log_file = open(log_filepath, "w")

# File paths
file_path_sch = "/Users/rick/Desktop/EDA Exam/schpub99.sav"

# Load the .sav files
df_sch, meta_sch = pyreadstat.read_sav(file_path_sch)

# Display the first few rows of each dataframe
print("School Data (schpub99.sav):")
print(df_sch.head())

######### data exploration ###########

# Display column names to identify relevant variables
print("Column Names in schpub99.sav:")
print(df_sch.columns)

# Display metadata for column descriptions
print("\nColumn Labels (Descriptions):")
print(meta_sch.column_labels)


##### QUESTION 1

# Display general info
print("Total number of records:", df_sch.shape[0])

# Check for a unique school identifier (SCHCNTL)
if 'SCHCNTL' in df_sch.columns:
    unique_schools = df_sch['SCHCNTL'].nunique()
    print("Total number of unique public schools:", unique_schools)
else:
    print("SCHCNTL variable not found in the dataset.")

####### QUESTION 2
# How many elementary schools are there in the state of Texas, in the state of CA, in the state of Florida?p


######### Question 3
# What are the average enrollment size (# of students) for high schools?
# Filter dataset for high schools (S0155 == 1)
df_high_schools = df_sch[df_sch["S0155"] == 1]

# Print number of high schools
print(f"Total number of high schools: {df_high_schools.shape[0]}")

print(df_sch["S0092"].dtype)

# Convert S0092 to numeric, forcing errors to NaN
df_sch["S0092"] = pd.to_numeric(df_sch["S0092"], errors="coerce")
# Verify the conversion
print(df_sch["S0092"].dtype)  # Should now be float or int

print("Number of missing values in S0092 after conversion:", df_sch["S0092"].isna().sum())

# Define mapping for enrollment categories
enrollment_mapping = {
    1: 200,  # Approximate midpoint of "Less than 300"
    2: 400,  # Approximate midpoint of "300 - 499"
    3: 600   # Conservative estimate for "500 or more"
}
# Convert S0092 categorical values to numeric estimates
df_sch["S0092_APPROX"] = df_sch["S0092"].map(enrollment_mapping)
# filter for high schools (S0155 == 1)
df_high_schools = df_sch[df_sch["S0155"] == 1]
# average estimated enrollment for high schools
avg_enrollment_hs = df_high_schools["S0092_APPROX"].mean()
print(f"\nrough average enrollment for high schools: {avg_enrollment_hs:.2f} students")



######### Question 4
# What is the average number of teachers in these public schools?
#
# Convert S0254 to numeric, coercing errors to NaN
df_sch["S0254"] = pd.to_numeric(df_sch["S0254"], errors="coerce")
# Verify conversion
print(f"Updated data type of S0254: {df_sch['S0254'].dtype}")

# Define mapping for teacher categories
teacher_mapping = {
    1: 15,  # Approximate midpoint for "Fewer than 25 teachers"
    2: 30,  # Approximate midpoint for "25 - 34 teachers"
    3: 40   # Conservative estimate for "35 or more"
}

# Apply mapping
df_sch["S0254_APPROX"] = df_sch["S0254"].map(teacher_mapping)

# Total estimated number of teachers across all schools
total_teachers = df_sch["S0254_APPROX"].sum()

# Average estimated number of teachers per school
avg_teachers_per_school = df_sch["S0254_APPROX"].mean()

print(f"\nTotal estimated teachers across all schools: {total_teachers:,.0f}")
print(f"Average estimated teachers per school: {avg_teachers_per_school:.2f}")




########## Question 5
# What is the average number of students eligible for the free lunch program?
# Filter schools that have free lunch program eligibility data
df_lunch_eligible = df_sch[df_sch["S0282"] == 1]

# Print how many schools reported eligibility
print(f"Total schools reporting free lunch eligibility: {df_lunch_eligible.shape[0]}")

# Define mapping for Pre-K eligible students
prek_mapping = {
    1: 0,    # No students
    2: 7,    # Midpoint of "1-14"
    3: 20,   # Conservative estimate for "15 or more"
    -8: None  # Skip these values
}

# Define mapping for K-12 eligible percentage
k12_mapping = {
    1: 0.03,  # 3% for "<5%"
    2: 0.12,  # 12% for "5-19%"
    3: 0.35,  # 35% for "20-49%"
    4: 0.75,  # 75% for "50% or more"
    -8: None  # Skip these values
}

# Apply mapping throwing error to use .loc?
df_lunch_eligible = df_lunch_eligible.copy()

df_lunch_eligible.loc[:, "S0283_APPROX"] = df_lunch_eligible["S0283"].map(prek_mapping)
df_lunch_eligible.loc[:, "S0284_PERCENT"] = df_lunch_eligible["S0284"].map(k12_mapping)
df_lunch_eligible.loc[:, "S0284_APPROX"] = df_lunch_eligible["S0284_PERCENT"] * df_lunch_eligible["S0092_APPROX"]

# Estimate K-12 eligible students using enrollment
df_lunch_eligible["S0284_APPROX"] = df_lunch_eligible["S0284_PERCENT"] * df_lunch_eligible["S0092_APPROX"]

# Compute total and average eligible students
total_eligible_students = df_lunch_eligible[["S0283_APPROX", "S0284_APPROX"]].sum().sum()
avg_eligible_students_per_school = df_lunch_eligible[["S0283_APPROX", "S0284_APPROX"]].sum(axis=1).mean()

print(f"\nTotal estimated students eligible for free lunch: {total_eligible_students:,.0f}")
print(f"Average number of eligible students per school: {avg_eligible_students_per_school:.2f}")

####### QUESTION 2
# How many elementary schools are there in the state of Texas, in the state of CA, in the state of Florida?
# doing this here because its hard

# Check unique values for school level
# print("Unique values for SCHLEVEL (School Level):")
# print(df_sch["SCHLEVEL"].unique())

# SCHLEVEL
# 1 = "Elementary"
# 2 = "Secondary"
# 3 = "Combined"

# Check unique values for region
# print("\nUnique values for REGION (Geographic Region):")
# print(df_sch["REGION"].unique())
#Unique values for REGION (Geographic Region):
# ['3' '4' '1' '2']

# REGION
# 1 = "Northeast: Connecticut, Maine, Massachusetts, New Hampshire, New Jersey, New York,
# Pennsylvania, Rhode Island, Vermont"
# 2 = "Midwest: Illinois, Indiana, Iowa, Kansas, Michigan, Minnesota, Missouri, Nebraska, North
# Dakota, Ohio, South Dakota, Wisconsin"
# 3 = "South: Alabama, Arkansas, Delaware, District of Columbia, Florida, Georgia, Kentucky,
# Louisiana, Maryland, Mississippi, North Carolina, Oklahoma, South Carolina, Tennessee, Texas,
# Virginia, West Virginia"
# 4 = "West: Alaska, Arizona, California, Colorado, Hawaii, Idaho, Montana, Nevada, New Mexico,
# Oregon, Utah, Washington, Wyoming"

# Define mapping for SCHLEVEL
school_level_mapping = {
    1: "Elementary",
    2: "Secondary",
    3: "Combined"
}

# Apply mapping to make output readable
df_sch["SCHLEVEL_LABEL"] = df_sch["SCHLEVEL"].map(school_level_mapping)

# Count elementary schools by region
df_elem_by_region = df_sch[df_sch["SCHLEVEL"] == 1]["REGION"].value_counts().sort_index()

print("\nTotal number of elementary schools by REGION:")
print(df_elem_by_region)

# this is an impossible  question with our given data
# going to merge the district data to the school level data if I can

# Define file path for district-level dataset
file_path_dist = "/Users/rick/Desktop/EDA Exam/distpub99.sav"

# Load the district dataset
df_dist, meta_dist = pyreadstat.read_sav(file_path_dist)

# Display first few rows
print("\nDistrict Data (distpub99.sav):")
print(df_dist.head())

# Get column names from both datasets
columns_sch = set(df_sch.columns)
columns_dist = set(df_dist.columns)

# Find common columns
common_columns = columns_sch.intersection(columns_dist)

print("\nCommon columns between school and district datasets:")
print(common_columns)

    # Display unique values
    print("\nUnique values in SURVEY:")
    print(df_dist["SURVEY"].unique())

# I give up. there is no unique identifier.



# # Close the log file
##### DONT FORGET TO UNCOMMENT WHEN DONE
log_file.close()