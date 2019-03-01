# Your task is to create a Python script that analyzes the records to 
# calculate each of the following:
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

    # First row contains header
    csv_header = next(csvreader)

    # Count total number of months in the data
    total_months = 0
    # Total net profit/loss
    total_net = 0

    # Changes from month to month
    total_change = 0
    changes = {}
    previous = 0

    for row in csvreader:
        total_months = total_months + 1
        total_net = total_net + int(row[1])
        # Compute change from previous month
        if(total_months > 1):
            changes[row[0]]= int(row[1])-previous
        previous = int(row[1])

# Compute average change
for i in changes:
    print(int(changes[i]))
    total_change = total_change + int(changes[i])
average_change = total_change / len(changes)

# Compute max and min change
max_i = max(changes, key=changes.get)
min_i = min(changes, key=changes.get)
max_val = changes[max_i]
min_val = changes[min_i]

# Print results to terminal
print("Financial Analysis")
print(" ----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_net}")
print(f"Average Change: ${format(average_change,'.2f')}")
print(f"Greatest Increase in Profits: {max_i} $({max_val})")
print(f"Greatest Decrease in Profits: {min_i} $({min_val})")

# Export results to a text file
output_path = os.path.join(".",'PyBank',"output.txt")
with open(output_path,'w',newline='') as txtfile:
    txtfile.write("Financial Analysis\n")
    txtfile.write(" ----------------------------\n")
    txtfile.write(f"Total Months: {total_months}\n")
    txtfile.write(f"Total: ${total_net}\n")
    txtfile.write(f"Average Change: ${format(average_change,'0.2f')}\n")
    txtfile.write(f"Greatest Increase in Profits: {max_i} $({max_val})\n")
    txtfile.write(f"Greatest Decrease in Profits: {min_i} $({min_val})\n")
    