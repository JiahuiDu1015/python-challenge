import os

import csv

csv_file_path = os. path. join("Resources", "budget_data.csv")

total_months = 0
net_total = 0
total_changes = 0
num_changes = 0
previous_profit_loss = None
changes = []
average_change = 0
greatest_increase_date = None
greatest_increase_amount = 0


with open(csv_file_path, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)
    print(f"csv Header: {csv_header}")

   # for row in csvreader:
       # print(row)

    # calculate total months
    for row in csvreader:
        total_months += 1
    print(f'Total Months: {total_months}')

    # calculate the net total amount of "Profit/Losses"

    for row in csvreader:
         net_total += int(row['Profit/Losses'])
    print(f"Net Total Amount of Profit/Losses: ${net_total}")

    for row in csvreader:
        current_profit_loss = int(row['Profit/Losses'])
        
        if previous_profit_loss is not None:
            change = current_profit_loss - previous_profit_loss
            total_changes += change
            num_changes += 1
            changes.append(change)
        
        previous_profit_loss = current_profit_loss

    print(f"Total Changes: {total_changes}")
    print(f"Average Change: {average_change}")

    for row in csvreader:
        date = row[0]
        profit = int(row[1])
    print(f"Greatest increase in profits: {greatest_increase_date}")
    print(f"Greatest decrease in profits: {greatest_increase_date}")

txt_file_path = 'output.txt'
with open(txt_file_path, 'w') as txtfile:
     txtfile.write("Total Months: 86")
     txtfile.write("Net Total Amount of Profit/Losses: $0")
     txtfile.write("Total Changes: 0")
     txtfile.write("Average Change: 0")
     txtfile.write("Greatest increase in profits: None")
     txtfile.write("Greatest decrease in profits: None")

