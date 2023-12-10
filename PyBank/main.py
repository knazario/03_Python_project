#importing needed libraries for reading file path and reading csv files
import os
import csv

# setting path for csv file to bank_csv variable 
bank_csv = os.path.join("Resources", "budget_data.csv")

# setting necessary variables to hold strings, values, calculations and create 2 placeholder list for info needed during loop
total_months = 0
total_profits = 0
change_list = []
prior_month = 0
total_change = 0
g_increase = 0
g_decrease = 0
index_counter = 0
month_list= []

# open csv and condult analysis
with open(bank_csv) as csv_file:
    #read in csv file 
    csvreader = csv.reader(csv_file, delimiter=',')
    # store and skip header row prior to loop
    csv_header = next(csvreader)
    # for each row, store data and conduct calculations 
    for row in csvreader:
        month_list.append(row[0])           #append month to month list
        total_months += 1                   # increase total month counter by 1
        total_profits += int(row[1])        # add total profits sum to current row profit/loss
        change = int(row[1]) - prior_month  # calculate change between current month and prior month
        change_list.append(change)          # store change in list of all changes (aligns with month list)
        prior_month = int(row[1])           # sets prior month to current row month for next interation of loop

#Remove the first value in change_list and month_list - not part of analysis because first row has not comparison/prior month
change_list.pop(0)
month_list.pop(0)

#for loop to iterate through change_list, sum up total change across months use conditionals in order to track
# greatest increase and decrase. using an index counter to refer to appropriate index in month_list to pull string that 
# corresponds to the change value
for x in change_list:
        total_change += x
        if x > g_increase:
             g_increase = x
             g_increase_month = month_list[index_counter]
        if x < g_decrease:
            g_decrease = x
            g_decrease_month = month_list[index_counter]
        index_counter += 1
# calculate average change rounded to 2 decimal values
average_change = round((total_change/ len(change_list)),2)

#sets a path for analysis text file
bank_txt = os.path.join("Analysis", "PyBank_Analysis.txt")
# create a list of lines of analysis to print on terminal and write on text file
printout = ['\nFinancial Analysis', '---------------------------------------------',
         'Total Months: '+ str(total_months),
         'Total: $'+ str(total_profits),
         'Average Change: $'+ str(average_change), 
         'Greatest Increase in Profits: '+ g_increase_month + '($ '+ str(g_increase) + ')',
         'Greatest Decrease in Profits: '+ g_decrease_month + '($ '+ str(g_decrease) + ')']
# open and write on text file
with open(bank_txt, 'w') as txt:
    #for each line, write line with additional line breaks on text file and then print same info to the terminal
    for line in printout:
        txt.write(line)
        txt.write('\n\n')
        print(line + '\n')