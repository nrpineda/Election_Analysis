#Assign a variable for the file to load and the path

file_to_load = 'Resources/election_results.csv'

# Open the election results and read the file.

# election_data = open(file_to_load, 'r')

#     print(election_data)

# #Close the file.

# election_data.close()

#Open the election results and read the file

with open(file_to_load) as election_data:

    print(election_data)

# Add a variable to save the file to a path.

file_to_save = 'analysis/election_results.txt'

# Initialize a total vote counter.

total_votes = 0

# Candidate Options and candidate votes.

winning_candidate = ''
winning_count = 0
winning_percentage = 0


candidate_options = ['Charles Casper Stockham', 
'Diana DeGette', 'Raymon Anthony Doane']

print(candidate_options)


candidate_votes = {'Charles Casper Stockham' : 85213,
'Diana DeGette': 272892, 'Raymon Anthony Doane': 11606}

print(candidate_votes)


winning_candidate = ('Diana DeGette')

