# we using pandas shocker
import pandas as pd
#pyreadstat should be a sufficient package to work with .sav files
import pyreadstat
import sys
import os

###### DONT FORGET TO UNCOMMENT WHEN FINISHED #####
# # Define the log file path
# log_directory = "/Users/rick/Desktop/EDA Exam/logs/"
# log_filename = "school_output_log.txt"
# log_filepath = os.path.join(log_directory, log_filename)
#
# # Ensure the directory exists
# os.makedirs(log_directory, exist_ok=True)
#
# # Open log file and redirect print statements
# log_file = open(log_filepath, "w")

# File paths
file_path_sch = "/Users/rick/Desktop/EDA Exam/schpub99.sav"

# Load the .sav files
df_sch, meta_sch = pyreadstat.read_sav(file_path_sch)

# Display the first few rows of each dataframe
print("School Data (schpub99.sav):")
print(df_sch.head())












# # Close the log file
##### DONT FORGET TO UNCOMMENT WHEN DONE
# log_file.close()