# Your task is to create a Python script that analyzes the records to calculate each of the following:
# The total number of months included in the dataset
# The net total amount of "Profit/Losses" over the entire period
# The average of the changes in "Profit/Losses" over the entire period
# The greatest increase in profits (date and amount) over the entire period
# The greatest decrease in losses (date and amount) over the entire period

# budget_data.csv is composed of two columns: Date and Profit/Losses
    
import os
import csv

csvpath = os.path.join('.','PyBank', 'budget_data.csv')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile)

    # first row contains header
    csv_header = next(csvreader)
    print(csv_header)

    # count total number of months in the data
    total_months = 0
    # total net profit/loss
    total_net = 0

    # changes
    total_change = 0
    changes = {}
    previous = 0

    for row in csvreader:
        total_months = total_months + 1
        total_net = total_net + int(row[1])
        # compute change from previous month
        if(total_months > 1):
            changes[row[0]]= int(row[1])-previous
        previous = int(row[1])

# compute average change
for i in changes:
    print(int(changes[i]))
    total_change = total_change + int(changes[i])
average_change = total_change / len(changes)

# compute max and min change
max_i = max(changes, key=changes.get)
min_i = min(changes, key=changes.get)
max_val = changes[max_i]
min_val = changes[min_i]

# Print results to terminal
print("Financial Analysis")
print(" ----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_net}")
print(f"Average Change: ${average_change}")
print(f"Greatest Increase in Profits: {max_i} $({max_val})")
print(f"Greatest Decrease in Profits: {min_i} $({min_val})")

# Financial Analysis
#  ----------------------------
# Total Months: 86
# Total: $38382578
# Average  Change: $-2315.12
# Greatest Increase in Profits: Feb-2012 ($1926159)
# Greatest Decrease in Profits: Sep-2013 ($-2196167)

# Export results to a text file