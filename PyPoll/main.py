import os
import csv

inputpath = os.path.join("Resources","election_data.csv")
with open(inputpath,'r') as electionfile:
    electiondata=csv.reader(electionfile,delimiter=",")
    header=next(electiondata) #skip header

    totalvote = 0
    candidate_names = [] # to store all canditate names from every row of the csv
    candidate_list = []  #var to provide list of only candidate names available within the csv

    for row in electiondata:
        totalvote += 1
        candidate=row[2]
        candidate_names.append(candidate)
        if candidate not in candidate_list:
            candidate_list.append(candidate)
    #print(candidate_list)

#create list [0, 0, ...,0] to count votes for each candidate
    count_individual_vote = []
    for a in range(len(candidate_list)):
        count_individual_vote.append(0)
    #print(count_individual_vote)

#use candidate_names[] to count vote and adding to the corresponding index for candidate_list[]
    for candidate in candidate_names:
        if candidate in candidate_list:
            count_individual_vote[candidate_list.index(candidate)] +=1
  
 #percentage vote for each candidate in the count_individual_vote[]  
    percentage_vote = [] 
    for percent in count_individual_vote:
        percentage_vote.append(round(percent/totalvote*100,3))
   

    text_firstpart = (f"Election Results\n-------------------------\
    \nTotal Votes: {totalvote}\n-------------------------")
#print 1st part
    print(text_firstpart)

#print 2nd part
    winnerpercent=0.000
    for n in range(len(candidate_list)):
        if winnerpercent < percentage_vote[n]:
            winnerpercent = percentage_vote[n]
        print(f"{candidate_list[n]}: {percentage_vote[n]}% ({count_individual_vote[n]})")

    test_lastpart = (f"-------------------------\
    \nWinner: {candidate_list[percentage_vote.index(winnerpercent)]}\
    \n-------------------------") 
#print last part
    print(test_lastpart)

#write to the text file
#creat the list for the second part 
text_secondpart=[]
for n in range(len(candidate_list)):
    text_secondpart.append(f"{candidate_list[n]}: {percentage_vote[n]}% ({count_individual_vote[n]})")

outputpath = os.path.join("analysis","election_output.txt")
with open(outputpath,'w') as electionout:

    electionout.write(text_firstpart)
    electionout.write("\n")
    electionout.write("\n".join(str(m) for m in text_secondpart))
    electionout.write("\n")
    electionout.write(test_lastpart)

