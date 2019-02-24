# Your task is to create a Python script that analyzes the votes and calculates each of the following:
# The total number of votes cast
# A complete list of candidates who received votes
# The percentage of votes each candidate won
# The total number of votes each candidate won
# The winner of the election based on popular vote

# election_data.csv is composed of three columns: Voter ID, County, and Candidate. 

import os
import csv

csvpath = os.path.join('.','PyPoll', 'election_data.csv')

# dictionary of candidate and number of votes
candidates = {}

# total votes
total_votes = 0

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile)

    # first row contains header
    # Voter ID, County, and Candidate
    csv_header = next(csvreader)
    # print(csv_header)
    for row in csvreader:
        total_votes = total_votes + 1
        person = row[2]
        # if candidate is not in dict then add candidate
        if not person in candidates:
            candidates[person] = 1
        # if candidate is in dict then increment value by 1
        else:
            candidates[person] += 1
     
# Print analysis to the terminal
print("Election Results")
print(" -------------------------")
print(f" Total Votes: {total_votes}")
print(" -------------------------")
for person in candidates:
    print(f"{person}: {candidates[person]/total_votes} ({candidates[person]})")
print(" -------------------------")
print(f" Winner: {max(candidates, key=candidates.get)}")
print(" -------------------------")

# Election Results
# -------------------------
# Total Votes: 3521001
# -------------------------
# Khan: 63.000% (2218231)
# Correy: 20.000% (704200)
# Li: 14.000% (492940)
# O'Tooley: 3.000% (105630)
# -------------------------
# Winner: Khan
# -------------------------

# Export a text file with the results