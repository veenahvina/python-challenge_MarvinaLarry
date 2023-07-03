#Import modules to read os and csv
import os
import csv
from pathlib import Path

#Locate file for assignment
file_path = os.path.join('Resources','budget_data.csv')

#Establish parameters
Total_Months = 0
first_amount = 0
Net_Profit_Losses = 0
Net_Changes = 0
difference = 0


#Define the function and have it accept the 'budget_data' as the source
def changes(budget_data, first_amount):
    changes = budget_data - int(first_amount)
    return(changes)


#Open file for assignment

with open(file_path) as budget:
    #read file with csv package
    reader = csv.reader(budget, delimiter = ',')
    #determine if there is a header; move to next row if there is
    header = next(reader)
    #create a list container to capture all of the monthly differences
    monthly_changes = []

    #Create a loop to read each row
    #Capture the first amount and store it in the monthly changes container
    #Calculate the difference between current and previous months
    #Append difference to the monthly changes list
    for row in reader:
        Total_Months = Total_Months + 1
        Net_Profit_Losses = Net_Profit_Losses + int(row[1])
        difference = changes(int(row[1]), first_amount)
        first_amount = int(row[1])
        monthly_changes.append(difference)
    monthly_changes.pop(0)
    
    for i in monthly_changes:
        Net_Changes = Net_Changes + i

#File to output
output_file = os.path.join('Analysis','bank_analysis.txt')

#Results of script to write to output file
results = f"""
Financial Analysis \n
------------------------- \n
Total Months: {Total_Months}
"""
print(results)

#Net the Profit/Losses over the entire period; add a blank row
print(f"Net_Profit_Losses: {Net_Profit_Losses} \n")

#Calculate average of those changes; add a blank row
print(f"Average_Changes: {Net_Changes / len(monthly_changes)} \n")

#Calculate and display the month with the greatest increase in profits
print("Greatest Increase in Profits: ")

#Calculate and display the month with the greatest decrease in profits
print("Greatest Decrease in Profits: ")

#with open (output_file, "w") as file:
with open (output_file, "w") as file:
    file.write(results)
    #-------------------------
    #Net the Profit/Losses over the entire period; add a blank row
    file.write(f"Net_Profit_Losses: {Net_Profit_Losses} \n")

    #Calculate average of those changes; add a blank row
    file.write(f"Average_Changes: {Net_Changes / len(monthly_changes)} \n")

    #Calculate and display the month with the greatest increase in profits
    file.write("Greatest Increase in Profits: \n")

    #Calculate and display the month with the greatest decrease in profits
    file.write("Greatest Decrease in Profits: ")
    #-------------------------