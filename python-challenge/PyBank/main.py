# Dependencies
import os
import csv

# Specify the path and the file
csvpath = os.path.join('budget_data.csv')

# Specify the file to write to
output_path = os.path.join("new.txt")

# Define and Initialize variables
months = 0
total = 0
max = 0
min = 0
previous = 0
change = 0
totalchange = 0
maxmonth = " "
minmonth = " "

# Open the CSV
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Read the header row first. Don't process the header. 
    csv_header = next(csvfile)

    # Loop through from row 2 onward    
    for row in csvreader:   
        
        # Number of months
        months = months +1
        
        # Change in profit/loss from previous to current month
        change = float(row[1]) - previous

        # Accumulate monthly increase/decrease. Skip first month. Better to use a separate flag. We are OK for the guven data. 
        if previous != 0:
            totalchange = totalchange + change 
        
        # Save the highest positive and negative changes and corresponding months
        if change > max:
           max = change  
           maxmonth = row[0]

        if change < min:
           min = change     
           minmonth = row[0] 
      
        # Total profit/losses
        total = total + float(row[1])

        # Save this month's profit/loss to compare with the next month's
        previous = float(row[1])
        
    print("Financial Analysis")
    print("-------------------------------------------------------")
    print(f"Total Months: {months}")
    print("Total: " '${:.0f}'.format(total))    
    print("Average Change: " '${:.2f}'.format(totalchange/(months-1)))
    print("Greatest Increase in Profits: " + maxmonth + " "'${:.0f}'.format(max))
    print("Greatest Decrease in Profits: " + minmonth + " "'${:.0f}'.format(min))
    
# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline='') as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')

    # Write to the output file
    csvwriter.writerow(["Financial Analysis"])
    csvwriter.writerow(["-------------------------------------------------------"])
    csvwriter.writerow(["Total Months: "+str(months)])
    csvwriter.writerow(["Total: " '${:.0f}'.format(total)])    
    csvwriter.writerow(["Average Change: " '${:.2f}'.format(totalchange/(months-1))])
    csvwriter.writerow(["Greatest Increase in Profits: " + maxmonth + " "'${:.0f}'.format(max)])
    csvwriter.writerow(["Greatest Decrease in Profits: " + minmonth + " "'${:.0f}'.format(min)])
