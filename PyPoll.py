# The data we need to retrieve.
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote.

#Add our dependencies

import csv
import os

# Assign a variable for the file to load from the path
file_to_load = os.path.join("Resources", "election_results.csv")

# 1. Initialize a total vote counter.
total_votes = 0

# Declare empty list for Candidate Options 
candidate_options = []

# Declare empty dictionary for Candidate votes
candidate_votes = {}

# Winning Candidate and Winning Count Tracker

winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read and print the header row
    headers = next(file_reader)
    print(headers)
    
    # Print each row in the CSV file.
    for row in file_reader:
        # 2. Add the total vote count.
        total_votes += 1

        # Print the candidate name for each row.
        candidate_name = row [2]

        # If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
            # Add it to the list of candidates,
            candidate_options.append(candidate_name)

            # Begin tracking the candidate's votes count.
            candidate_votes[candidate_name] = 0
           
         # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1

# Print the candidate vote dictionary.
print(candidate_votes)


# Determine the percentage of votes for each candidate
# Iterate through the candidate list.

for candidate_name in candidate_votes:
    # Retrieve vote count of a candidate.
     votes = candidate_votes[candidate_name]
    # Calculate the percentage of votes.
     votes_percentage = float(votes) / float(total_votes) * 100

#Determine the percentage of votes for each candidate by looping through
    #1. Iterate through the candidate list.
for candidate_name in candidate_votes:
    #2.Retrieve vote count of a candidate.
    votes = candidate_votes[candidate_name]
    #3. Calculate the percentage of votes,
    votes_percentage = float(votes) / float(total_votes) * 100
 
 #To do: print out each candidate's name, vote count, and percentage votes to the terminal
    print(f"{candidate_name}: {votes_percentage:.1f}% ({votes:,})\n")

# Determine winning vote count and candidate
# Determine if the votes are greater than the winning count. 
    if (votes > winning_count) and (votes_percentage > winning_percentage):
         # If true then set winning_count = votes and winning_percent = vote_percentage
         winning_count = votes 
         winning_percentage = votes_percentage
        # Set the winning_candidate equal to the candidate's name.
         winning_candidate = candidate_name
winning_candidate_summary = (
    f"--------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"--------------------\n")
print(winning_candidate_summary)

#-------------------------------------------------------------------------------------------------
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
