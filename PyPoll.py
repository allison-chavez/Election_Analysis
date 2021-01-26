# The data we need to retrieve.
# 1. The total number of votes cast
# 2. A complete list of canidates who received votes
# 3. The percentage of votes each canidate won
# 4. The total number of votes each canidate won
# 5. The winner of the election based on popular vote.

# Add our dependencies.
import csv
import os
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# 1. Initialize a total vote counter.
total_votes = 0

# Candidate Options and candidate votes
candidate_options = []

# declare empty dictionary for votes
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file:
with open(file_to_load) as election_data:
    # Read the file object with the reader function.
    file_reader =  csv.reader(election_data)

    # Read and Print the header row.
    headers = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count.
        total_votes += 1
        # print the candidate name for each row.
        candidate_name = row[2]
        # If canddate does not match any existing candidate...
        if candidate_name not in candidate_options:
            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)
            # candidate's vote count tracking.
            candidate_votes[candidate_name] = 0
        # add a vote to candidates count
        candidate_votes[candidate_name] += 1
# Determine the percentage of votes for each candidate by looping through the counts.
# Iterate through the candidates list.
for candidate_name in candidate_votes:
    # Retrieve vote count of a candidate.
    votes =  candidate_votes[candidate_name]
    # Calculate the percentages of votes.
    vote_percentage = float(votes) / float(total_votes) * 100
    
    # To do: Print out each candidates name, vote count, and percentage of votes to the terminal
    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

    # Determine winning vote count and candidate
    # Determine if the votes is greater than the winning count.
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        # if true then set winning_count = votes and winning_percent = vote_percentage
        # And set the winning_candidate equal to the candidates name
        winning_count = votes
        winning_percentage = vote_percentage
        winning_candidate = candidate_name
# to do: print out the winning candidate, vote count and percentage to terminal
winning_candidate_summary = (
    f"--------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)





    



