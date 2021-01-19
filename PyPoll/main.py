import os
import csv

csvpath = os.path.join("..","Resources","election_data.csv")

votes = 0
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

                

print("Election Results")
print("-------------------------")
print (f"Total Votes: {votes}")
print("-------------------------")
print (f"Candidates: {candidates}")

print("Election Results", file=open("Results_PyRoll.txt", "a"))
print("-------------------------", file=open("Results_PyRoll.txt", "a"))
print (f"Total Votes: {votes}", file=open("Results_PyRoll.txt", "a"))
print("-------------------------", file=open("Results_PyRoll.txt", "a"))
print (f"Candidates: {candidates}", file=open("Results_PyRoll.txt", "a"))
