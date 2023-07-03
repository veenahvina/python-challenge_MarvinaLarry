#Import modules to read os and csv
import os
import csv

#Locate file for assignment
file_path = os.path.join('Resources','election_data.csv')

#Establish parameters
total_votes = 0
# first_candidate = 0
# candidate_votes = 0
# sum_ballots = 0
# sum = 0
candidate_names = []
candidate_votes = {}
winner = ""
winning_count = 0

#Define the function and have it accept the 'election_data' as the source
# def complete_list(election_data, first_candidate):
#     complete_list = (first_candidate), election_data
#     return(complete_list)


#Open file for assignment
with open(file_path) as election:
    #read file with csv package
    reader = csv.reader(election)
    #determine if there is a header; move to next row if there is
    header = next(reader)
    #create a container to capture all of the candidate votes
    # candidate_votes = []

#Create a loop to read each row
#Capture the first vote and store it in the candidate votes container
#Calculate the sum of current and previous ballots
#Append sum to the candidate_votes list
    for row in reader:
        total_votes = total_votes + 1

        # candidate_votes = candidate_votes, row[0]
        # sum = complete_list((row[0]), first_candidate)
        candidate_name = (row[2])
        if candidate_name not in candidate_names:
            candidate_names.append(candidate_name)
            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] += 1

#File to output
output_file = os.path.join('Analysis','election_analysis.txt')
with open (output_file, "w") as file:
    results = f"""
Election Results
-------------------------
Total Votes: {total_votes}
-------------------------
"""
    print(results)
    file.write(results)

    for candidate in candidate_votes:
        votes = candidate_votes.get(candidate)
        vote_percent = votes / total_votes * 100
        if(votes > winning_count):
            winning_count  = votes
            winner = candidate

        vote_results = f"{candidate}: {vote_percent: .3f}% ({votes})\n"
        print(vote_results)
        file.write(vote_results)
    winning_candidate = f"""
-------------------------
Winner: {winner}
-------------------------    
    
    """
    print(winning_candidate)
    file.write(winning_candidate)
#
    # for i in sum_ballots:
    #     sum_ballots = sum_ballots + i
     
#Print Title of analysis
##print("Election Results \n")

#Add a line of dashes; add a blank row
##print("------------------------- \n")

#Total the number of months; add a blank row
##print(f"total_votes: {Total_Votes} \n")

#Add a line of dashes; add a blank row
##print("------------------------- \n")

#Generate list of candidates who received votes


#Display candididate total votes and vote percentages


#Add a line of dashes; add a blank row
##print("------------------------- \n")


#Display the name of winner

#Add a line of dashes; add a blank row
##print("------------------------- \n")


