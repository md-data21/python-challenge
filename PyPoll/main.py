# This is my Python code for the PyPoll assignment. Within this code, I will be importing and reading a csv file, 
# using functions to manipulate and calculate the required data, and finally I will be writing an output file with 
# a summary csv file (located in the analysis folder) as well as printing it the terminal. 

# The data summary will include:
# total number of votes in dataset, amount of votes for each candidate (sum and % of total), and the winner of the election. 

#You can find the raw data file in the Resources folder.

# Modules
import os
import csv

# Path to collect data from the Resources folder
election_csv = os.path.join('Resources', 'election_data.csv')

#Define variables
Total_Votes = 0
Khan_Votes = 0
Correy_Votes = 0
Li_Votes = 0
OTooley_Votes = 0 

# Read in the CSV file
with open(election_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=",")

    # Read the header row first
    csv_header = next(csvfile)



 # To get sum of Profit/Loss column
    for row in csvreader:

        # Calculating total $ in csv file, Profit/Loss column summed
        Total_Votes += 1

        # Tallying Votes for each candidate
        if row[2] == "Khan":
            Khan_Votes += 1
        elif row[2] == "Correy":
            Correy_Votes += 1
        elif row[2] =="Li":
            Li_Votes += 1
        else:
            OTooley_Votes += 1

# Total % by Candidate = Candidate Votes / Total Votes
Khan_percentage = Khan_Votes/Total_Votes
Correy_percentage = Correy_Votes/Total_Votes
Li_percentage = Li_Votes/Total_Votes
OTooley_percentage = OTooley_Votes/Total_Votes

#Formatting percentages to 3 decimal places
Khan_percentage = "{:.3%}".format(Khan_percentage)
Correy_percentage = "{:.3%}".format(Correy_percentage)
Li_percentage = "{:.3%}".format(Li_percentage)
OTooley_percentage = "{:.3%}".format(OTooley_percentage)

#Determining winner
if Khan_Votes > Correy_Votes and Khan_Votes > Li_Votes and Khan_Votes > OTooley_Votes:
    Winner = "Khan"
elif Khan_Votes < Correy_Votes and Correy_Votes > Li_Votes and Correy_Votes > OTooley_Votes:
    Winner = "Correy"
elif Khan_Votes < Li_Votes and Correy_Votes < Li_Votes and Li_Votes > OTooley_Votes:
    Winner = "Li"
else:
    Winner = "OTooley"


#Summary Documentation
summary_line1= (f'Election Results')
summary_line2= (f'-------------------------')
summary_line3= (f'Total Votes: {Total_Votes}')
summary_line4= (f'Khan: {Khan_percentage} ({Khan_Votes})')
summary_line5= (f'Correy: {Correy_percentage} ({Correy_Votes})')
summary_line6= (f'Li: {Li_percentage} ({Li_Votes})')
summary_line7= (f'OTooley: {OTooley_percentage} ({OTooley_Votes})')
summary_line8= (f'Winner: {Winner}')

# Printing summary results into terminal
print("")
print(summary_line1)
print(summary_line2)
print(summary_line3)
print(summary_line2)
print(summary_line4)
print(summary_line5)
print(summary_line6)
print(summary_line7)
print(summary_line2)
print(summary_line8)
print(summary_line2)

# Print the results into an output text file
# Specify the file to write to
output_path = os.path.join("Analysis", "Summary_Output.csv")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline='') as csvfile:

    #initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=' ')

    #write summary rows
    csvwriter.writerow(summary_line1.split())
    csvwriter.writerow(summary_line2.split())
    csvwriter.writerow(summary_line3.split())
    csvwriter.writerow(summary_line2.split())
    csvwriter.writerow(summary_line4.split())
    csvwriter.writerow(summary_line5.split())
    csvwriter.writerow(summary_line6.split())
    csvwriter.writerow(summary_line7.split())
    csvwriter.writerow(summary_line2.split())
    csvwriter.writerow(summary_line8.split())
    csvwriter.writerow(summary_line2.split())