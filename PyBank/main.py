# Modules
import os
import csv

# Path for csv
csvpath = os.path.join(".", "Resources", "budget_data.csv")

# Open the csv using UTF-8 encoding
with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)

    # total_month = len(list(csvreader)) 
    # print("Total month: " + str(total_month))

    total_budget = 0
    for row in csvreader:
        total_budget = total_budget + int(row[1])
    print(f'Total: $ {total_budget}')

        the_changes = 