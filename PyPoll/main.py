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

    #set variables needed- total votes, empty dictionary for candidates, winner name string and winner vote count placeholder
    total_votes = 0
    candidate_dict = {}
    winner = ""
    win_votes = 0

    #for loop to iterate through each line in read in csv file (without header)
    for row in csvreader:
        #increases total vote count by 1 
        total_votes += 1 
       
        # if current row value (candidate name) does not exist in our dictionary, 
        # create a new key and assign value of 1(1st vote)
        if row[2] not in candidate_dict:
            candidate_dict[row[2]] = 1
       
        #else (candidate already in dictionary), increase value by 1 (increase vote count)
        else:
                candidate_dict[row[2]] += 1

#set path for output analysis text file
poll_txt = os.path.join("Analysis", "PyPoll_analysis.txt")

#open text file to write summary info
with open(poll_txt, 'w') as txt:
    #print opening formatting and total votes to termainal and text file
    print(f'\nElection Results\n-------------------------------------\n'+
          f'Total Votes: {total_votes}\n-------------------------------------')
    
    txt.write(f'\nElection Results\n-------------------------------------\n'+
                    f'Total Votes: {total_votes}\n-------------------------------------\n')
         
    # For loop that for each key_value(candidate) in dictionary
    for key in candidate_dict:    
       #calculate percent of votes by dividing value associated with key (votes) with total votes
        percent_vote = round(((candidate_dict[key]/total_votes)*100),3)
      
        #print string of Name, percent vote and vote count and write same info to text file
        print(f'{key}: {percent_vote}% ({candidate_dict[key]})\n' )
        txt.write(f'{key}: {percent_vote}% ({candidate_dict[key]})\n')
      
       # if current value(votes) is greater than stored winning vote count, replace name and vote count with current values
        if candidate_dict[key] > win_votes:
            win_name = key
            win_votes = candidate_dict[key]

   #print Winner of election to terminal and write to text file 
    print(f'-------------------------------------\nWinner: {win_name}'+
          f'\n-------------------------------------')
    txt.write(f'-------------------------------------\nWinner: {win_name}'+
          f'\n-------------------------------------')