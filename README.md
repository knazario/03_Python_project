# 3_Python_project

This folder contains 2 different pyton projects. PyBank reads in csv data with monthly profits/losses over time and conducts analysis of the data to output to the terminal and text file (stored in Analysis folder). PyPoll reads in voting data for a local election and does analysis to determine the proportion of vote for each candidate and disply summary with winner (popular vote). 


Code Sources: 
* used examples provdied in below tutorial to read/write to a text file with proper syntax 
https://www.pythontutorial.net/python-basics/python-write-text-file/
* For the Pypoll script, line 28 ( if row[2] not in candidate_dict:)- I received support from a Learning Assistant to get the "not in" logic for a conditional 
* For the PyBank script, line 29 (if total_months > 1:)- I brainstormed with a study group regarding this line of code to exclude the first month profits/losses, from the change realted calculations. 