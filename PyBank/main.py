#importing needed libraries for reading file path and reading csv files
import os
import csv

# setting path for csv file to bank_csv variable 
bank_csv = os.path.join("Resources", "budget_data.csv")

# setting necessary variables to hold strings, values, calculations and create 2 placeholder list for info needed during loop
total_months = 0
total_profits = 0
prior_month = 0
g_increase = 0
g_decrease = 0
change_total = 0

# open csv and condult analysis
with open(bank_csv) as csv_file:
    #read in csv file 
    csvreader = csv.reader(csv_file, delimiter=',')
    # store and skip header row prior to loop
    csv_header = next(csvreader)
    # for loop through each row from csv file and performs calculations 
    for row in csvreader:
        #incease total months by 1 and add current profit/loss value to total_profits
        total_months += 1                  
        total_profits += int(row[1])        
        
        #perform change comparisons after the first month (skip first iteration- no comparison month)
        if total_months > 1:
            #calculate change between current month and prior month
            change = int(row[1]) - prior_month  
            change_total += change
            #conditionals to check if current increase or decrease is the greatest increase or decrease 
            #assigns value if true
            if g_increase < change:
                 g_increase = change
                 g_increase_month = row[0]
            
            elif g_decrease > change:
                 g_decrease = change
                 g_decrease_month = row[0]
        # assigns prior month to current row month for next interation of loop
        prior_month = int(row[1])          

# calculate average change rounded to 2 decimal values. 1 less value than total_months due to not including first month
average_change = round((change_total/(total_months-1)),2)

#sets a path for analysis text file
bank_txt = os.path.join("Analysis", "PyBank_Analysis.txt")
# create a list of lines of analysis to print on terminal and write on text file
printout = ['\nFinancial Analysis', '---------------------------------------------',
         'Total Months: '+ str(total_months),
         'Total: $'+ str(total_profits),
         'Average Change: $'+ str(average_change), 
         'Greatest Increase in Profits: '+ g_increase_month + '($'+ str(g_increase) + ')',
         'Greatest Decrease in Profits: '+ g_decrease_month + '($'+ str(g_decrease) + ')']
# open and write on text file
with open(bank_txt, 'w') as txt:
    #for each line, write line with additional line breaks on text file and then print same info to the terminal
    for line in printout:
        txt.write(line)
        txt.write('\n\n')
        print(line + '\n')