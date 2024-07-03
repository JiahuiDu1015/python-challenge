import os

import csv

csv_file_path = os. path. join("Resources", "budget_data.csv")

total_months = 0
net_total = 0
total_changes = 0
num_changes = 0
month_changes = []
previous_profit_loss = None
changes = []
average_change = 0
greatest_increase = ["",0]
greatest_decrease = ["",9999999999999999999]


with open(csv_file_path, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    
    csv_header = next(csvreader)
    print(f"csv Header: {csv_header}")
    first_row = next(csvreader)
    total_months += 1
    net_total += int(first_row[1])
    previous_profit_loss = int(first_row[1])

    for row in csvreader:

    # calculate total months
        total_months += 1
    

    # calculate the net total amount of "Profit/Losses"
        net_total += int(row[1])
    

    # calculate average change and changes list
        average_change = int(row[1]) - previous_profit_loss
        previous_profit_loss = int(row[1])
        changes += [average_change]
        month_changes += [row[0]] 
    
        
    # Calculate Greatest Increase
        if average_change > greatest_increase[1]:
           greatest_increase[0] = row[0]
           greatest_increase[1] = average_change
        
    # Calculate Greatest Increase
        if average_change < greatest_decrease[1]:
           greatest_decrease[0] = row[0]
           greatest_decrease[1] = average_change

average_change_final = sum(changes) / len(changes)

output = (f"Total Months: {total_months}\n"
          f"Net Total Amount of Profit/Losses: ${net_total}\n"
          f"Average Change: ${average_change_final}\n"
          f"Greatest increase in profits: {greatest_increase}\n"
          f"Greatest decrease in profits: {greatest_decrease}")

print(output)

txt_file_path = 'output.txt'
with open(txt_file_path, 'w') as txtfile:
     txtfile.write(output)
     

