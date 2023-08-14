# Modules
import os
import csv

from numpy import average
from prometheus_client import generate_latest

# Path for csv
csvpath = os.path.join(".", "Resources", "budget_data.csv")

# Open the csv 
with open(csvpath, 'r') as csvfile:
    budget = csv.reader(csvfile, delimiter=",")

    header = next(budget) #skip header row

#set initial variable and list to store variable 
    month_count = 0
    total_profit_loss = 0

    profitloss_change = 0
    profitloss_change_store = []
    profitloss_change_start =[]
    last_profitloss = 0

    for row in budget:
        month_count = month_count + 1
        total_profit_loss += int(row[1])

#change in the profit
        if month_count >= 2:
            profitloss_change = int(row[1]) - last_profitloss
            profitloss_change_store.append(profitloss_change)

            date_count = row[0]
            profitloss_change_start.append(date_count)
        last_profitloss = int(row[1])

    totalPLchange = sum(profitloss_change_store)
    averagePLchange = totalPLchange/len(profitloss_change_store)

#set the greatest increase and decrease = 0 to compare with the variable in the profitloss_change_store[]
    greatestincrease = 0
    greatestdecrease = 0
    i = 0  # index for greatest increase
    d = 0  # index for greatest decrease

    row_count=0
    for singlechange in profitloss_change_store:
            row_count +=1
            if greatestincrease< singlechange:
                greatestincrease = singlechange
                i = row_count -1
            if greatestdecrease > singlechange:
                greatestdecrease = singlechange
                d = row_count -1


    final_print=(f"Financial Analysis\n----------------------------\nTotal Months: {month_count}\nTotal: ${total_profit_loss}\
    \nAverage Change: ${round(averagePLchange,2)}\nGreatest Increase in Profits: {profitloss_change_start[i]} (${greatestincrease})\
    \nGreatest Decrease in Profits: {profitloss_change_start[d]} (${greatestdecrease})")

# print the analysis
    print(final_print)    

# export a text file to the analysis folder 
budgetanalysis_path = os.path.join("analysis","budget_output.txt")
with open(budgetanalysis_path,'w') as budgetout:
    budgetout.write(final_print)
