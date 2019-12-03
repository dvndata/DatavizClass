# Dependencies
import os
import csv

# Specify the path and the file
csvpath = os.path.join('election_data.csv')

# Specify the file to write to
output_path = os.path.join("new.txt")

# Define and Initialize variables
TotalVotes = 0
idx=0
max = 0
winner = " "

# Arrays to hold all candidates and the votes obtained
Names=[]
Votes = []

# Open the CSV
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Read the header row first. Don't process the header. 
    csv_header = next(csvfile)

    # Loop through from row 2 onward    
    for row in csvreader:   
        
        # If the candidate is found in the list Names, add 1 to the vote count for that candidate. 
        if row[2] in Names:
            idx = Names.index(row[2])
            Votes[idx] +=1
        
        # If not, add a new entry for that candidate and begin the vote count for him/her. 
        else:
            Names.append(row[2])    
            Votes.append(1)
            
        # Count all the votes cast
        TotalVotes = TotalVotes + 1
        

        
# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline='') as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')

    # Write to the output file
    csvwriter.writerow(["Election Results"])
    csvwriter.writerow(["-------------------------------------------------------"])
    csvwriter.writerow(["Total Votes: "+str(TotalVotes)])
    csvwriter.writerow(["-------------------------------------------------------"])

    # Print to the terminal
    print("Election Results")
    print("-------------------------------------------------------")
    print(f"Total Votes: {TotalVotes}")
    print("-------------------------------------------------------")
    
    # Loop through the candidate names list and print their names, vote % and votes obtained.
    # Format the percentages to 3 decimal points
    # write to the text file as well
    for idx in range(len(Names)):
        print(Names[idx] + ": " '{00:.3%}'.format(Votes[idx]/TotalVotes) + " " + str(Votes[idx]) )    
        csvwriter.writerow([Names[idx] +": " '{00:.3%}'.format(Votes[idx]/TotalVotes) + " " +str(Votes[idx])])

        # Find highest number of votes that a candidate obtained
        if max < Votes[idx]:
            max = Votes[idx]

    # Get the name of the candidate that obtained the highest number of votes.     
    idx = Votes.index(max)
    winner = Names[idx]

    # Print to the terminal 
    print("-------------------------------------------------------")
    print("Winner: "+ winner)
    print("-------------------------------------------------------")

    # Write the name of the winner in the text file
    csvwriter.writerow(["-------------------------------------------------------"])
    csvwriter.writerow(["Winner: "+ winner])
    csvwriter.writerow(["-------------------------------------------------------"])