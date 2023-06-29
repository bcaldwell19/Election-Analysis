# Open Modules

import csv
import os

# open/write Path

file_to_load = os.path.join("Resources", "election_results.csv")
file_to_save = os.path.join("Analysis", "election_analysis.txt")

## Open the election results and read the file.

with open(file_to_save, "w") as txt_file:
    txt_file.write(
        "Counties in the Election\n-------------------------\nArapahoe\nDenver\nJefferson"
    )

total_votes = 0  # set total votes to zero
candidate_options = []  # declare empty list for candidates
candidate_votes = {}  # declare empy dictory to store candidates
winning_candidate = ""
winning_count = 0
winning_percentage = 0

with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    # Read the header row.
    headers = next(file_reader)
    # Print each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count.
        total_votes += 1
        # Get the candidate name from each row.
        candidate_name = row[2]
        # If the candidate does not match any existing candidate, add the
        # the candidate list.
        if candidate_name not in candidate_options:
            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)
            # And begin tracking that candidate's voter count.
            candidate_votes[candidate_name] = 0
        # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1

# Save the results to our text file.
with open(file_to_save, "w") as txt_file:
    # After opening the file print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n"
    )
    print(election_results, end="")
    # After printing the final vote count to the terminal save the final vote count to the text file.
    txt_file.write(election_results)
    for candidate_name in candidate_votes:
        # Retrieve vote count and percentage.
        votes = candidate_votes[candidate_name]
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n"
        # Print each candidate's voter count and percentage to the terminal.
        print(candidate_results)
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)
        # Determine winning vote count, winning percentage, and winning candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage
    # Print the winning candidate's results to the terminal.
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n"
    )
    print(winning_candidate_summary)
    # Save the winning candidate's results to the text file.
    txt_file.write(winning_candidate_summary)

# skeleton code
##Total number of Votes (Number of Ballots)
##Number of Candidates who received votes (For loop with If Statement to add one to the count)
##Number of Votes per Candidate (List or Dict)
##Percentage of Votes per Canidate (Votes Per Candidate/Total Number of Votes)*100
###Winner by popular vote (if/elif/else statement)
