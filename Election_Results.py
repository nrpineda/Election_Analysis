#Add our dependencies

import csv
import os

# Assign a variable to the path from where we will get the data

file_to_load = os.path.join("Resources", "election_results.csv")
file_to_save = os.path.join("analysis", "election_results.txt")

# Initialize the total vote counter.

total_votes = 0 

# Candidate options and candidate votes

candidate_options = []
candidate_votes = {}

# 1: Create a county list and county votes dictionary.
county_options = []
county_votes = {}

# Track the winning candidate, vote count, and vote percentage

winning_candidate = ""
winning_count = 0
winning_percentage = 0

# 2: Track the largest county and county voter turn out
county_vote_count = 0
county_vote_percentage = 0
largest_county = ""
# Read the csv and convert it into a list of dictionaries.

with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    #Read the header row
    headers = next(file_reader)
    #Print each row in the CSV file
    for row in file_reader:
        #Add the total vote count.
        total_votes += 1
        #Get the candidate name from each row
        candidate_name = row[2]
        # 3: Extract the county name for each row
        county_name = row[1]
# If the candidate does not match any existing candidade add to the list

if candidate_name not in candidate_options:
    # Add the candidate name to the candidate list
    candidate_options.append(candidate_name)
    # And begin tracking the candidate's count
    candidate_votes[candidate_name] = 0
# Add a vote to that candidate's count
candidate_votes[candidate_name] += 1

    # If the name of the county does not match any existing counties add to
    # the list
if county_name not in county_options:
    # Add the county name to the county list
    county_options.append(county_name)
    #And begin tracking the county's count
    county_votes[county_name] = 0
# And begin tracking the number of votes per county
county_votes[county_name] += 1

# Save the results to a text file

with open(file_to_save, "w") as txt_file:
    #After opening the file print the final vote count to the terminal
    

