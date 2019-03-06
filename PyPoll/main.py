# Your task is to create a Python script that analyzes the votes and 
# calculates each of the following:
# The total number of votes cast
# A complete list of candidates who received votes
# The percentage of votes each candidate won
# The total number of votes each candidate won
# The winner of the election based on popular vote

# election_data.csv is composed of three columns: Voter ID, County, and Candidate

import os
import csv

csvpath = os.path.join('./election_data.csv')

# Dictionary of candidate and number of votes
candidates = {}

# Total votes
total_votes = 0

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile)

    # First row contains header
    # Voter ID, County, and Candidate
    csv_header = next(csvreader)
    
    for row in csvreader:
        total_votes = total_votes + 1
        person = row[2]
        # If candidate is not in dict then add candidate
        if not person in candidates:
            candidates[person] = 1
        # If candidate is in dict then increment value by 1
        else:
            candidates[person] += 1
     
# Print analysis to the terminal
print("Election Results")
print(" -------------------------")
print(f" Total Votes: {total_votes}")
print(" -------------------------")
for person in candidates:
    print(f"{person}: {format(100*candidates[person]/total_votes,'0.2f')}% ({candidates[person]})")
print(" -------------------------")
print(f" Winner: {max(candidates, key=candidates.get)}")
print(" -------------------------")

# Export a text file with the results
output_path = os.path.join("./output.txt")
with open(output_path,'w',newline='') as txtfile:
    txtfile.write("Election Results\n")
    txtfile.write(" -------------------------\n")
    txtfile.write(f" Total Votes: {total_votes}\n")
    txtfile.write(" -------------------------\n")
    for person in candidates:
        txtfile.write(f"{person}: {format(100*candidates[person]/total_votes,'0.2f')}% ({candidates[person]})\n")
    txtfile.write(" -------------------------\n")
    txtfile.write(f" Winner: {max(candidates, key=candidates.get)}\n")
    txtfile.write(" -------------------------\n")