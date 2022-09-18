# The data we need to retrieve.
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote.

#Add our dependencies

import csv
from email import header
import os

# Assign a variable for the file to load from the path
file_to_load = os.path.join("Resources", "election_results.csv")

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

# Read and print the header row
    headers = next(file_reader)
    print(headers)
    

# ----------------------------------------------------

# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis","election_analysis.txt")
# Using the with statement open the file as a text file. 

with open(file_to_save, "w") as txt_file:
 # Write three counties to the file on a separate line
    txt_file.write("Counties in the Election\n-------------------\nArapahoe\nDenver\nJefferson")

    # # Write three counties to the file.
    # txt_file.write("Arapahoe, ")
    # txt_file.write("Denver, ")
    # txt_file.write("Jefferson")
    # We can also write all three counties in one line
    # Like this: txt_file.write("Arapahoe, Denver, Jefferson")