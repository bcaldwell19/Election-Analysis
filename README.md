# Election-Analysis 

## Overview of Election Audit: Explain the purpose of this election audit analysis.

        "In this module, you'll be assisting a Colorado board of elections employee, Tom, in an election audit of the tabulated results for a U.S. congressional precinct in Colorado."
        "Altogether, the votes cast by these three methods will determine the final election results. After the votes are counted, your job is to generate a vote count report to certify this U.S. congressional race."

        Our customer, Tom, usually performs the audit using excel. Tom's manager, Seth, inquired about automating the process using python.  Our project was to explore Python's built-in functions and modules that assist in automating the audit process. 
        If successful, other congressional districts, senatorial districts, and local elections could use python to audit their elections.  A good majority of this code could also be reused with minor changes depending on variables if the other elections use a similar csv.    


## Election-Audit Results: Using a bulleted list, address the following election outcomes. Use images or examples of your code as support where necessary.

### How many votes were cast in this congressional election?

            ~Total Votes: 369,711 (Please see election_analysis.txt)

### Provide a breakdown of the number of votes and the percentage of total votes for each county in the precinct.

            ~County Votes: Jefferson: 10.5% (38,855), Denver: 82.8% (306,055), and Arapahoe: 6.7% (24,801) (Please see election_analysis.txt)

### Which county had the largest number of votes?

            ~Largest County of Voters: Denver (Denver: 82.8% (306,055)) (Please see election_analysis.txt)

### Provide a breakdown of the number of votes and the percentage of the total votes each candidate received.

            ~Charles Casper Stockham: 23.0% (85,213), Diana DeGette: 73.8% (272,892), and Raymon Anthony Doane: 3.1% (11,606) (Please see election_analysis.txt)

### Which candidate won the election, what was their vote count, and what was their percentage of the total votes?

            ~Winner: Diana DeGette 
            ~Winning Vote Count: 272,892
            ~Winning Percentage: 73.8%

## Election-Audit Summary: In a summary statement, provide a business proposal to the election commission on how this script can be used—with some modifications—for any election. Give at least two examples of how this script can be modified to be used for other elections.

    Dear to whom this may concern,
    I have a business proposition for audit certification for other congressional districts, senatorial districts, and local elections.  I personally asked Tom how long the audit certification took using an excel.  Tom responded due to the very manual process that it took approximately 3 hours including occasional breaks.  Tom and I created that python script that automates that whole process. I used an uncalibrated stopwatch to time the code, and the code took approximately 1.6 seconds.  The only thing the script requires is maybe 15 to 30 minutes to create a good path from the raw data.  In my opinion, the set-up time would get faster with the same user repeating the audit every time as well.  I would request to use this python script as skeleton code for the other audits. There will be minor modifications in the script such as column and row indexes, but those are rather easy to change for any trained programmer.  

The most obvious change would be to the raw data file's location.  The pathing will have be established for every new user, so that should be taken consideration by any new customer.
Similarly, the output file location will need to be setup as well. 

Depending on the raw data file, the row and column indexes will need to be updated. For example, if the raw data file had the candidates in column zero instead of column two.  This would be a rather minor change, but the script would likely throw an error if it was run.    

