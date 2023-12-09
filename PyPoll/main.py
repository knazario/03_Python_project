import os
import csv

poll_csv = os.path.join("Resources", "election_data.csv")

with open(poll_csv) as csv_file:

    csvreader = csv.reader(csv_file, delimiter=',')

    csv_header = next(csvreader)

    total_votes = 0
    candidates = ['Charles Casper Stockham','Diana DeGette','Raymon Anthony Doane']
    votes = [0,0,0,0]
    percent_vote = []
    candidate_str = []
    win_count = 0
    
    for row in csvreader:
        total_votes += 1
        if row[2] == candidates[0]:
            votes[0]+= 1
        elif row[2] == candidates[1]:
            votes[1]+= 1
        elif row[2] == candidates[2]:
            votes[2]+= 1
        else:
            votes[3] += 1

for x in range(len(candidates)):
    percent_vote.append(round(100*votes[x]/total_votes,3))
    candidate_str.append(candidates[x]+": "+ str(percent_vote[x]) + "% (" + str(votes[x])+ ")")
    if votes[x] > win_count: 
        win_name = candidates[x]
        win_count = votes[x]

poll_txt = os.path.join("Analysis", "PyPoll_analysis.txt")
printout = ['Election Results', '-------------------------------------',
         'Total Votes: '+ str(total_votes), '-------------------------------------',
          candidate_str[0],candidate_str[1],candidate_str[2], '-------------------------------------',
          'Winner: ' + win_name,
          '-------------------------------------',
          ]

with open(poll_txt, 'w') as txt:
    for line in printout:
        txt.write(line)
        txt.write('\n\n')
        print(line + '\n')