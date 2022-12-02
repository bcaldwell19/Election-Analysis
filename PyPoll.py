#Open Modules

import csv
import os

#open/write Path 

file_to_load = os.path.join("Resources","election_results.csv")
file_to_save = os.path.join("Analysis", "election_analysis.txt")

with open(file_to_save, "w") as txt_file:
    txt_file.write("Counties in the Election\n-------------------------\nArapahoe\nDenver\nJefferson")

## Open the election results and read the file.

with open(file_to_load) as election_data:

    file_reader = csv.reader(election_data)
    headers = next(file_reader)
    print(headers)

# To do: perform analysis.
##Total number of Votes (Number of Ballots)
##Number of Candidates who received votes (For loop with If Statement to add one to the count)
##Number of Votes per Candidate (List or Dict)
##Percentage of Votes per Canidate (Votes Per Canidate/Total Number of Votes)*100
###Winner by popular vote (if/elif/else statement)

#Print File








