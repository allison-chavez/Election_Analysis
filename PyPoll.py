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

# Using the open() function with the "w" mode we will write data to the file.
with open(file_to_load) as election_data:
    # To do: read and analyze the data here.
    # Read the file object with the reader function.
    file_reader =  csv.reader(election_data)

    # Read and Print the header row.
    headers = next(file_reader)
    print(headers)

    



