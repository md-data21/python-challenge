# This is my Python code for the PyBank assignment. Within this code, I will be importing and reading a csv file, 
# using functions to manipulate and calculate the required data, and finally I will be writing an output file with 
# a summary csv file (located in the analysis folder) as well as printing it the terminal. 

# The data summary will include:
# total number of months in dataset, total Profit/Loss over period, avg change in Profit/Loss over period,
# greatest increase in profits (date and amount), and great decrease in losses (date and amount). 

#You can find the raw data file in the Resources folder.

# Modules
import os
import csv

# Path to collect data from the Resources folder
bank_csv = os.path.join('Resources', 'budget_data.csv')

# Define variables 
total = 0
Total_Months = 0
Monthly_PL=[]
Monthly_Change=[]
Months=[]

# Read in the CSV file
with open(bank_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=",")

    # Read the header row first
    csv_header = next(csvreader)

    # To get sum of Profit/Loss column
    for row in csvreader:

        #Calculating total $ in csv file, Profit/Loss column summed
        total += int(row[1])

        # to determine total number of months in data file
        Total_Months += 1
        
        #Adding rows to the empty lists above for further manipulation
        Monthly_PL.append(int(row[1]))
        Months.append(row[0])

#Calculating Month over Month change and storing those numbers
for i in range(0,len(Monthly_PL)-1):
    Monthly_Change.append(Monthly_PL[i+1]- Monthly_PL[i])

#To find Largest Gains and Losses
Increase = max(Monthly_Change)
Decrease = min(Monthly_Change)

#To calculate Average Change over the whole file
Total_Change = sum(Monthly_Change)
Length_Change = len(Monthly_Change)
Average_Change = round(Total_Change/Length_Change,2)

#To find the corresponding months with the biggest gains and losses
# Had to add +1 because of the way I did the Monthly Change append
Max_Index = Monthly_Change.index(Increase)
Min_Index = Monthly_Change.index(Decrease)
Max_Month = Months[Max_Index+1]
Min_Month = Months[Min_Index+1]

#Summary Documentation
summary_line1= (f'Financial Analysis')
summary_line2= (f'-------------------------')
summary_line3= (f'Total Months: {Total_Months}')
summary_line4= (f'Total: ${total}')
summary_line5= (f'Average Change: ${Average_Change}')
summary_line6= (f'Greatest Increase in Profits: {Max_Month} (${Increase})')
summary_line7= (f'Greatest Decrease in Profits: {Min_Month} (${Decrease})')

# Printing summary results into terminal
print("")
print(summary_line1)
print(summary_line2)
print(summary_line3)
print(summary_line4)
print(summary_line5)
print(summary_line6)
print(summary_line7)

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
    csvwriter.writerow(summary_line4.split())
    csvwriter.writerow(summary_line5.split())
    csvwriter.writerow(summary_line6.split())
    csvwriter.writerow(summary_line7.split())
