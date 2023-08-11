# Modules
import os
import csv

from numpy import average, greater
from prometheus_client import generate_latest

# Path for csv
csvpath = os.path.join(".", "Resources", "budget_data.csv")

# Open the csv using UTF-8 encoding
with open(csvpath, 'r') as csvfile:
    budget = csv.reader(csvfile, delimiter=",")

    header = next(budget) #skip header row

    # total_month = len(list(csvreader)) 
    # print("Total month: " + str(total_month))

    # total_ = 0
    # for row in csvreader:
    #     total_budget = total_budget + int(row[1])
    # print(f'Total: $ {total_budget}')

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

    totalPLchange = sum(profitloss_change)
    averagePLchange = totalPLchange/len(profitloss_change)

greatestincrease = 0
greatestdecrease = 0
i = 0  # index for greatest increase
d = 0  # index for greatest decrease

rownumber=0
for singlechange in profitloss_change:
            rownumber +=1
            if greatestincrease< singlechange:
                greatestincrease = singlechange
                i = rownumber -1
            if greatestdecrease > singlechange:
                greatestdecrease = singlechange
                d = rownumber -1


finaltext=(f"Financial Analysis\n----------------------------\nTotal Months: {month_count}\nTotal: ${total_profit_loss}\
    \nAverage Change: ${round(averagePLchange,2)}\nGreatest Increase in Profits: {profitloss_change_start[i]} (${greatestincrease})\
    \nGreatest Decrease in Profits: {profitloss_change_start[d]} (${greatestdecrease})")

# print the analysis to the terminal 
print(finaltext)    

# export a text file with the results.
# budgetanalysis_path = os.path.join("analysis","budget_output.txt")
# with open(budgetanalysis_path,'w') as budgetout:
#     budgetout.write(finaltext)
