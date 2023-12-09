import os
import csv

bank_csv = os.path.join("Resources", "budget_data.csv")

total_months = 0
total_profits = 0
change_list = []
prior_month = 0
total_change = 0
g_increase = 0
g_decrease = 0
index_counter = 0
month_list= []

with open(bank_csv) as csv_file:

    csvreader = csv.reader(csv_file, delimiter=',')

    csv_header = next(csvreader)
    
    for row in csvreader:
        month_list.append(row[0])
        total_months += 1
        total_profits += int(row[1])
        change = int(row[1]) - prior_month
        change_list.append(change)
        prior_month = int(row[1])


change_list.pop(0)
month_list.pop(0)
for x in change_list:
        total_change += x
        if x > g_increase:
             g_increase = x
             g_increase_month = month_list[index_counter]
        if x < g_decrease:
            g_decrease = x
            g_decrease_month = month_list[index_counter]
        index_counter += 1

average_change = round((total_change/ len(change_list)),2)

bank_txt = os.path.join("Analysis", "PyBank_Analysis.txt")
printout = ['Financial Analysis', '---------------------------------------------',
         'Total Months: '+ str(total_months),
         'Total: $'+ str(total_profits),
         'Average Change: $'+ str(average_change), 
         'Greatest Increase in Profits: '+ g_increase_month + '($ '+ str(g_increase) + ')',
         'Greatest Decrease in Profits: '+ g_decrease_month + '($ '+ str(g_decrease) + ')']

with open(bank_txt, 'w') as txt:
    for line in printout:
        txt.write(line)
        txt.write('\n\n')
        print(line + '\n')