import pyreadstat

# Define file paths
file_path_teacher = "/Users/rick/Desktop/EDA Exam/tchpub99.sav"
file_path_school = "/Users/rick/Desktop/EDA Exam/schpub99.sav"

# Load teacher and school datasets
df_teacher, meta_teacher = pyreadstat.read_sav(file_path_teacher)
df_school, meta_school = pyreadstat.read_sav(file_path_school)

# Print number of observations in each dataset
print(f"Number of observations in Public Teacher Data: {df_teacher.shape[0]}")
print(f"Number of observations in Public School Data: {df_school.shape[0]}")


# Find common columns between teacher and school datasets
common_columns = set(df_teacher.columns).intersection(set(df_school.columns))

print("\nCommon columns between teacher and school datasets:")
print(common_columns)


# Merge teacher and school data using the common key
df_merged = df_teacher.merge(df_school, on="SCHCNTL", how="left")

# Print number of observations after merge
print(f"\nNumber of observations after merging: {df_merged.shape[0]}")
