import os
import csv

inputpath = os.path.join("Resources","election_data.csv")
with open(inputpath,'r') as electionfile:
    electiondata=csv.reader(electionfile,delimiter=",")
    header=next(electiondata) #store header

    totalvote = 0
    candidate_names = [] # to store all canditate names from every row of the csv
    candidate_list = []  #var to provide list of only candidate names available within the csv

    for row in electiondata:
        totalvote += 1
        candidate=row[2]
        candidatelist.append(candidate)
        if candidate not in uniquelist:
            uniquelist.append(candidate)
    #print(uniqueist)

#create array [0, 0, ...,0] to count votes for each candidate
    count_individual_vote = []
    for a in range(len(uniquelist)):
        count_individual_vote.append(0)
    #print(count_individual_vote)

#use candidatelist to count vote and adding to the corresponding index for the array above
    for candidate in candidatelist:
        if candidate in uniquelist:
            count_individual_vote[uniquelist.index(candidate)] +=1
  
    
    percentage_vote = [] 
    for percent in count_individual_vote:
        percentage_vote.append(round(percent/totalvote*100,3))
   

    finaltextstart = (f"Election Results\n-------------------------\
    \nTotal Votes: {totalvote}\n-------------------------")
#print start text
    print(finaltextstart)

#print middle text
    winnerpercent=0.000
    for n in range(len(uniquelist)):
        if winnerpercent < percentage_vote[n]:
            winnerpercent = percentage_vote[n]
        print(f"{uniquelist[n]}: {percentage_vote[n]}% ({count_individual_vote[n]})")

    finaltextend = (f"-------------------------\
    \nWinner: {uniquelist[percentage_vote.index(winnerpercent)]}\
    \n-------------------------") 
#print final text
    print(finaltextend)

#write to the text file
middletext=[]
for n in range(len(uniquelist)):
    middletext.append(f"{uniquelist[n]}: {percentage_vote[n]}% ({count_individual_vote[n]})")

outputpath = os.path.join("analysis","election_output.txt")
with open(outputpath,'w') as electionout:

    electionout.write(finaltextstart)
    electionout.write("\n")
    electionout.write("\n".join(str(m) for m in middletext))
    electionout.write("\n")
    electionout.write(finaltextend)

###THE END###