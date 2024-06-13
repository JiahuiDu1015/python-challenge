import os

import csv

election_data = {}
candidate_votes ={}
total_votes = 0

csv_file_path = os. path. join("Resources", "election_data.csv")


with open(csv_file_path, 'r') as csvfile:
    csvreader = csv.DictReader(csvfile, delimiter=',')

    csv_header = next(csvreader)
    print(f"csv Header: {csv_header}")
    
    
    # for row in csvreader:
        # print(row)



    for row in csvreader:
        candidate = {row['Candidate']}

        candidates = ["Charles Casper Stockham", "Diana DeGette", "Raymon Anthony Doane"]

    for candidate in candidate_votes:

        if candidate in candidate_votes:
            candidate_votes[candidate] += 1
        else:
            candidate_votes[candidate] = 1

    
       
    print("Total number of votes each candidate won: ")

    for candidate, votes in candidate_votes.items():
        print(f"{candidate}: {votes} votes")

    for row in csvreader:
        candidate = row['Candidate']
        total_votes += 1

        if candidate in candidate_votes:
            candidate_votes[candidate] += 1
        else:
            candidate_votes[candidate] = 1

    print("Percentage of votes each candidate won:")
    
    for candidate, votes in candidate_votes.items():
        percentage = (votes / total_votes) * 100
        print(f"{candidate}: {percentage:.3f}%")

txt_file_path = 'output.txt'
with open(txt_file_path, 'w') as txtfile:
     txtfile.write("Total number of votes each candidate won: ")
     txtfile.write("Charles Casper Stockham: ")
     txtfile.write("Diana DeGette: ")
     txtfile.write("Raymon Anthony Doane: ")
     txtfile.write("Winner: Diana DeGette")

       