import os
import csv
import pandas as pd

csvpath = os.path.join("..","Resources","election_data.csv")

votes = 0
candidateA = ""
candidateB = ""
candidates=[]
listcand=[]
countcand = 0

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile,delimiter=",")

    next(csvreader)

    for row in  csvreader:

        votes = votes + 1

        if row[2] not in candidates:

            candidates.append(row[2])

        df = csvreader

        name = pd.Names(row[2]) 

print(name)

        
            

                
           
print(listcand)
print(candidates)
print("Election Results")
print("-------------------------")
print (f"Total Votes: {votes}")
print("-------------------------")