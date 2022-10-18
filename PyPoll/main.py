#Call on the os module to ensure the program can navigate to the path laid out for the csv file used
import os
#Call on the csv module to ensure the program can read the commands in relation to the csv file that will be utilzed
import csv

# Define the path to the election data in the Resources folder
csvpath = os.path.join("PyPoll", 'Resources', 'election_data.csv')

# Initialize all variables up front
All_votes = 0
Stockham_votes = 0
DeGette_votes = 0
Doane_votes = 0
candidate = set()
winner = 0

# Open the CSV path where the file is located
with open(csvpath) as csvfile :
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    
    #Begin my loop to read and collect data
    for row in csvreader:

        # Complete the first task and collect the total number of votes
        All_votes += 1
        candidate.add(row[2])

        # Use conditions to count the amount of votes for each candidate
        if (row[2] == "Charles Casper Stockham"):
            Stockham_votes += 1
        elif (row[2] == "Diana DeGette"):
            DeGette_votes += 1
        elif (row[2] == "Raymon Anthony Doane"):
            Doane_votes += 1
       

# Calculate the percentage of votes for each candidate
Stockham_Percent = (Stockham_votes/All_votes) 
DeGette_percent = (DeGette_votes/All_votes) 
Doane_percent = (Doane_votes/All_votes) 

# Create a list using variables to store  
vote_total = [Stockham_votes, DeGette_votes, Doane_votes]

# Assign variables to identify the winning number of votes
winner_counts = max(vote_total)
#print(winner_counts)
winner_name = ""

# Use conditional statement to assign the winning number of votes to a name
if winner_counts == Stockham_votes :
    winner_name = "Charles Casper Stockham"

elif winner_counts == DeGette_votes :
    winner_name = "Diana DeGette"   

elif winner_counts == Doane_votes :
    winner_name = "Raymon Anthony Doane"

# Display the requested data
print("Election Results")
print("---------------------")
print("Total Votes: " + str(All_votes))
print("---------------------")
print("Stockham: " + "{:.3%}".format(Stockham_Percent) + " " + (str(Stockham_votes)))
print("DeGette: " + "{:.3%}".format(DeGette_percent) + " " + (str(DeGette_votes)))
print("Doane: " + "{:.3%}".format(Doane_percent) + " " + (str(Doane_votes)))
print("---------------------")
print("Winner: " +  winner_name)
print("---------------------")
print("----")

# Generate a .txt document and write the requested data
with open("Election_Results.txt", "w") as file:
    file.write("Election Results\n")
    file.write("------------------\n")
    file.write("Total Votes: " + str(All_votes) + "\n")
    file.write("------------------\n")
    file.write("Stockham: " + "{:.3%}".format(Stockham_Percent) + " (" + (str(Stockham_votes)) + ")" + "\n")
    file.write("DeGette: " + "{:.3%}".format(DeGette_percent) + " (" + (str(DeGette_votes)) + ")" + "\n")
    file.write("Doane: " + "{:.3%}".format(Doane_percent) + " (" + (str(Doane_votes)) + ")" + "\n")
    file.write("------------------\n")
    file.write("Winner: " +  winner_name + "\n")
    file.write("-------------------\n")