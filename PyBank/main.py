#Call on the os module to ensure the program can navigate to the path laid out for the csv file used
import os
#Call on the csv module to ensure the program can read the commands in relation to the csv file that will be utilzed
import csv

# Define the path to the budget data in the Resources folder
budget_data_csv = os.path.join("pybank","Resources","budget_data.csv")

# Create lists to hold the data. The Months variable represents the months listed in column A of the csv data. PNL stands for Profit and Loss, and represents the data in column B of the csv data 
Months = []
PNL = []

# Open up the designated csv file to read
with open (budget_data_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)

    # Begin my for loop to collect and calculate data
    for row in csvreader:
        Months.append(row[0])
        PNL.append(int(row[1]))

# Complete the first task and find the total number of months included in the dataset
MonthCount = len(Months)
    
# Create a bucket to hold Month to Month changes 
m2m_change = []

# Initialize a variable that can be subtracted from
Begin_PNL = 0

# Equate End_PNL variable to the data in column B of the csv file. Once collected, subtract the number listed in Column B from the variable which is zero to obtain the positive or negative difference
End_PNL = int(row[1])
m2m_change_total = End_PNL - Begin_PNL

# Save the data into the bucket created to hold Month to Month changes
m2m_change.append(m2m_change_total)

# Create and initialize new variables to represent the PNL change by iniatilly setting it to zero. Set commands to do the math on each item in the PNL column from zero and find the average of Profit and Loss month to month
PNL_Changes = 0
PNL_Changes = PNL_Changes + m2m_change_total
Begin_PNL = End_PNL

# Calculate the average Month to Month change by dividing the PNL from the beggining by the Month Count variable
Average_m2m_change = (Begin_PNL/MonthCount)

#Find the greatest increase and decrease using the max and min functions, and place them with the correct months they occured using an index
#**Note TO GRADERS** I could not get this to work after trying various methods, I recognize the Greatest increase and decrease are incorrect :(

greatest_increase_PNL = max(m2m_change)
greatest_decrease_PNL = min(m2m_change)
increase_month = Months[m2m_change.index(greatest_increase_PNL)]
decrease_month = Months[m2m_change.index(greatest_decrease_PNL)]


# Display the requested data
print("Financial Analysis")
print("-------------------------")
print(f"Total Months: {MonthCount}")
print(f"Total: {sum(PNL)}")
print(f"Average Change: " + "$" + str(int(Average_m2m_change)))
print("Greatest Increase in Profits: " + str(increase_month) + " ($" + str(greatest_increase_PNL) + ")")
print("Greatest Decrease in Profits: " + str(decrease_month + " ($" + str(greatest_decrease_PNL)+ ")"))

# Generate a .txt document and write the requested data
with open("Financial_Analysis.txt", "w") as text:
    text.write("Financial Analysis\n")
    text.write("-------------------------\n")
    text.write(f"Total Months: {MonthCount}\n")
    text.write(f"Total: {sum(PNL)}\n")
    text.write(f"Average Change: " + "$" + str(int(Average_m2m_change)) + "\n")
    text.write("Greatest Increase in Profits: " + str(increase_month) + " ($" + str(greatest_increase_PNL) + ")\n")
    text.write("Greatest Decrease in Profits: " + str(decrease_month) + " ($" + str(greatest_decrease_PNL)+ ")\n")