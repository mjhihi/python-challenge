# importing csv and os modules
import csv
import os

# read-in the election_data.csv file
path=os.path.join('.','Resources','election_data.csv')
with open(path) as election_file:
    csvreader=csv.reader(election_file, delimiter=',')
    header = next(csvreader)
    cand_list=[cand[2] for cand in csvreader] # complete list of candidates receiving votes


# calculate the total num of votes cast
tot_votes=len(cand_list) 

# calculate total number of votes each candidate won
unique_candid_votes = [[candidate,cand_list.count(candidate)] for candidate in set(cand_list)]

# winner of the election based on popular vote
sorted_unique_candid_votes = sorted(unique_candid_votes, key=lambda x: x[1], reverse=True)

# print the analysis 
print('Election Results')
print('-------------------------')
print(f'Total Votes: {tot_votes}')
print('-------------------------')

# calculate percentage of votes each candidate won
for c in unique_candid_votes:
    percent=(c[1]/tot_votes)*100
    print(f'{c[0]}: {percent:6.3f}% ({c[1]})')

print('-------------------------')
print(f'Winner: {sorted_unique_candid_votes[0][0]}')
print("-------------------------")

# export the analysis result to the text file
p=os.path.join('.','analysis','results1.txt')
with open(p,'w') as results1:
    print('Election Results', file=results1)
    print('-------------------------', file=results1)
    print(f'Total Votes: {tot_votes}', file=results1)
    print('-------------------------', file=results1)

    # calculate percentage of votes each candidate won
    for c in unique_candid_votes:
        percent=(c[1]/tot_votes)*100
        print(f'{c[0]}: {percent:6.3f}% ({c[1]})', file=results1)

    print('-------------------------', file=results1)
    print(f'Winner: {sorted_unique_candid_votes[0][0]}', file=results1)
    print("-------------------------", file=results1)






