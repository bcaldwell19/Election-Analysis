#Open Modules

import csv
import os

#open/write Path 

file_to_load = os.path.join("Resources","election_results.csv")
file_to_save = os.path.join("Analysis", "election_analysis.txt")

## Open the election results and read the file.

with open(file_to_save, "w") as txt_file:txt_file.write("Counties in the Election\n-------------------------\nArapahoe\nDenver\nJefferson")

total_votes=0 #set total votes to zero
candidate_options = [] #declare empty list for candidates
candidate_votes = {} #declare empy dictory to store candidates
winning_candidate = ""
winning_count = 0
winning_percentage = 0

with open(file_to_load) as election_data:

    file_reader = csv.reader(election_data)

    headers = next(file_reader)

    for row in file_reader:
        total_votes +=1 #Increment total votes per row
        candidate_name = row[2] #search col. 2
        
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] += 1

for candidate_name in candidate_votes:
    # 2. Retrieve vote count of a candidate.
    votes = candidate_votes[candidate_name]
    # 3. Calculate the percentage of votes.
    vote_percentage = float(votes) / float(total_votes) * 100
    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

   # Determine winning vote count and candidate
   # # 1. Determine if the votes are greater than the winning count.
    if (votes > winning_count) and (vote_percentage > winning_percentage):
     # 2. If true then set winning_count = votes and winning_percent =
     # vote_percentage.
     winning_count = votes
     winning_percentage = vote_percentage
     # 3. Set the winning_candidate equal to the candidate's name.
     winning_candidate = candidate_name
winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)
  

# To do: perform analysis.
##Total number of Votes (Number of Ballots)
##Number of Candidates who received votes (For loop with If Statement to add one to the count)
##Number of Votes per Candidate (List or Dict)
##Percentage of Votes per Canidate (Votes Per Candidate/Total Number of Votes)*100
###Winner by popular vote (if/elif/else statement)

#Print File






