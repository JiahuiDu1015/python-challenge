import os

import csv

election_data = {}
candidates_votes ={}
total_votes = 0
candidates = set()
winner = ""
max_votes = 0

csv_file_path = os. path. join("Resources", "election_data.csv")


with open(csv_file_path, 'r') as csvfile:
    csvreader = csv.reader(csvfile)

    csv_header = next(csvreader)
    #print(f"csv Header: {csv_header}")
    first_vote = next(csvreader)
    total_votes += 1
    
    for row in csvreader:
    
        # calculate the total votes
        total_votes += 1

        # Add the candidate to the set (assuming 'Candidate' is the third column)
        candidates.add(row[2])

        # Increment the vote count for the candidate in the dictionary
        candidate = row[2]
        
        if candidate in candidates_votes:
            candidates_votes[candidate] += 1
        else:
            candidates_votes[candidate] = 1

# Calculate the total number of votes
total_votes = sum(candidates_votes.values())
  
for candidate, votes in candidates_votes.items():
    print(f"{candidate}: {votes}")

# Print percentage of votes each candidate won
results = []
for candidate, votes in candidates_votes.items():
    percentage = (votes / total_votes) * 100
    results.append(f"{candidate}: {percentage:.3f}% ({votes})")

    # Determine the winner based on popular vote
    if votes > max_votes:
        max_votes = votes
        winner = candidate

# Output file path
output_file = "election_results.txt"

# Write results to the output file
with open(output_file, 'w') as file:
    file.write(f"Election Results\n")
    file.write("-------------------------\n")
    file.write(f"Total Votes: {total_votes}\n")
    file.write("-------------------------\n")
    for result in results:
        file.write(result + "\n")
    file.write("-------------------------\n")
    file.write(f"Winner: {winner}\n")
    file.write("-------------------------\n")

# Print confirmation message
print(f"Results have been saved to {output_file}")
       