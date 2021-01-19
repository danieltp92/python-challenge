import os
import csv

csvpath = os.path.join("..", "Resources", "budget_data.csv")

count = 0
money = 0
value1 = 0
value2 = 0
diffval = 0
difftotal = 0
countavg = 0
diffavg = 0
maxval = 0
minval = 0

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile,delimiter=",")

    #column = len(csvfile[0])

    next(csvreader)

    for row in csvreader:
        
        #Count number of registers are in file
        count = count + 1

        #Sum the total value of the Profit/Loss column
        money = int(row[1]) + money
        
        #Math the profit change of the entire period
        if value1 != 0:

            value1 = value2

            value2 = int(row[1])

        else:

            value2 = int(row[1])     

            value1 = value2       



        diffval = int(value2) - int(value1)

        if countavg != diffval:

            countavg = countavg + 1

        else:

            countavg = 0

        difftotal = difftotal + diffval

        row.append(diffval)


        #Math Greatest increase in profits
        if maxval < int(row[2]):

            maxval = int(row[2])
            fecmax = row[0]


        #Math Greatest decrease in profits
        if minval > int(row[2]):

            minval = int(row[2])
            fecmin = row[0]


    #Math the average change of the entire period
    diffavg = difftotal / countavg

    print(f"Total Months: {count}")
    print(f"Total: $ {money}")
    print(f"Average Change: $ {float(diffavg)}")
    print(f"Greatest Increase in Profits: {fecmax}, $ {maxval}")
    print(f"Greatest Decrease in Profits: {fecmin}, $ {minval}")

    print(f"Total Months: {count}", file=open("Results_PyBank.txt", "a"))
    print(f"Total: $ {money}", file=open("Results_PyBank.txt", "a"))
    print(f"Average Change: $ {float(diffavg)}", file=open("Results_PyBank.txt", "a"))
    print(f"Greatest Increase in Profits: {fecmax}, $ {maxval}", file=open("Results_PyBank.txt", "a"))
    print(f"Greatest Decrease in Profits: {fecmin}, $ {minval}", file=open("Results_PyBank.txt", "a"))