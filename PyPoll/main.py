#importing needed libraries for reading file path and reading csv files
import os
import csv
# setting path for csv file to poll_csv variable 
poll_csv = os.path.join("Resources", "election_data.csv")

#open csv file and condult analysis
with open(poll_csv) as csv_file:
    #read in csv file 
    csvreader = csv.reader(csv_file, delimiter=',')
    # store and skip header row prior to loop
    csv_header = next(csvreader)

    #set variables needed- total votes, list of andidates, vote tally list, percecnt vote list, candidate string list, 
    # and winer index counter 
    total_votes = 0
    candidates = ['Charles Casper Stockham','Diana DeGette','Raymon Anthony Doane']
    votes = [0,0,0,0]
    percent_vote = []
    candidate_str = []
    win_count = 0
    
    #for each row, add a tally to votes list for the index that matches/corresponds with the index in candidate list
    # 4th element in list (votes[3] placed in else in case data has a typo or name program did not have in candidate list  
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

#for loop iterating through candidates to caluclate percent vote, concatenate candidate strings and compare total votes
# to store winner name and vote count (vote count used to compare to other candidates in list)
for x in range(len(candidates)):
    percent_vote.append(round(100*votes[x]/total_votes,3))
    candidate_str.append(candidates[x]+": "+ str(percent_vote[x]) + "% (" + str(votes[x])+ ")")
    if votes[x] > win_count: 
        win_name = candidates[x]
        win_count = votes[x]

#set path for output analysis text file
poll_txt = os.path.join("Analysis", "PyPoll_analysis.txt")
# store lines in a list for terminal and text output 
printout = ['\nElection Results', '-------------------------------------',
         'Total Votes: '+ str(total_votes), '-------------------------------------',
          candidate_str[0],candidate_str[1],candidate_str[2], '-------------------------------------',
          'Winner: ' + win_name,
          '-------------------------------------',
          ]
#for each line, write line with additional line breaks on text file and then print same info to the terminal
with open(poll_txt, 'w') as txt:
    for line in printout:
        txt.write(line)
        txt.write('\n\n')
        print(line + '\n')