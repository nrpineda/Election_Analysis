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
winning_county = ""
winning_county_count = 0
winning_county_percentage = 0

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

            # 4a: Write an if statement that checks that the county 
            # does not match any other existing counties in the list
        if county_name not in county_options:
            # 4b: Add the county name to the county list
            county_options.append(county_name)
            # 4c: And begin tracking the county's count
            county_votes[county_name] = 0
        # 5: Add a vote to the county's vote count
        county_votes[county_name] += 1

# Save the results to a text file

with open(file_to_save, "w") as txt_file:
    #After opening the file print the final vote count to the terminal
    election_results = (
        f"\nElections Results\n"
        f"----------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-----------------------------\n")
    print(election_results, end="")
    txt_file.write(election_results)


# 6a: Write a for loop to get the county from the county dictionary
    for county_name in county_votes:
        # 6b: Retrieve the vote count per county
        votes = county_votes[county_name]
        # 6c: Calculate the percentage of votes per county
        county_percentage = float (votes) / float (total_votes) * 100
        # 6d: Print the county results to the terminal
        county_results = (
            f"{county_name}: {county_percentage: .1f}%({votes:,})\n")
        # 6e: Save the county votes to a text file
        print(county_results)
        txt_file.write(county_results)

        # 6f: Write an if statement to determine the winning county and
        # get its vote count.
            
        if (votes > winning_county_count) and (county_percentage > winning_county_percentage):
            #If true then set the winning_county_count = votes and winning_county_percentage =
            #vote percentage.
            winning_county_count = votes
            winning_county_percentage = county_percentage
            winning_county = county_name
    
    # 7.Print the winning county's results to the terminal.

    winning_county_summary = (
        f"-------------------------------\n"
        f"Winner County: {winning_county}\n"
        f"Winning County Count: {winning_county_count:,}\n"
        f"Winning County Percentage: {winning_county_percentage:.1f}%\n"
        f"-------------------------------\n")
    # Save the winning candidate's results to the text file.
    print(winning_county_summary)

# 8: Save the final candidate vote count to the text file.
    txt_file.write(winning_county_summary)