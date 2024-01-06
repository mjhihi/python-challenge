# importing csv and os modules
import csv
import os

# create a list to store the budget data & read-in the budget_data.csv file
dat=[]
path=os.path.join('.','Resources','budget_data.csv')
with open(path) as buget_file:
    csvreader=csv.reader(buget_file, delimiter=',')
    header = next(csvreader)
    for row in csvreader:
        dat.append({'month':row[0], 'amount': int(row[1]), 'change':0})

# calculate the total months
total_months=len(dat) 

# calculate the net total amount of Profit/Losses
total_amt=sum(r['amount'] for r in dat)

# calculate the changes in Profit/Losses between months
pre_amt = dat[0]['amount']
for i in range(total_months):
    dat[i]['change']=dat[i]['amount']-pre_amt
    pre_amt=dat[i]['amount']

# calculate the avg of amount changes
total_change=sum(l['change'] for l in dat)
avg=round(total_change/(total_months-1),2)

# calculate the greatest increase & decrease of the changes
increase=max(dat,key=lambda i: i['change'])
decrease=min(dat,key=lambda d: d['change'])
print(increase)
print(decrease)

# analysis report
print('Financial Analysis')
print('----------------------------')
print(f'Total Months: {total_months}')
print(f'Total: ${total_amt}')
print(f'Average Change: ${avg}')
print(f'Greatest Increase in Profits: {increase["month"]} (${increase["change"]})')
print(f'Greatest Decrease in Profits: {decrease["month"]} (${decrease["change"]})')

#export the result to a text file
p=os.path.join('.','analysis','results.txt')
with open(p,'w') as results:
    print('Financial Analysis', file=results  )
    print('----------------------------', file=results)
    print(f'Total Months: {total_months}', file=results)
    print(f'Total: ${total_amt}', file=results)
    print(f'Average Change: ${avg}', file=results)
    print(f'Greatest Increase in Profits: {increase["month"]} (${increase["change"]})', file=results)
    print(f'Greatest Decrease in Profits: {decrease["month"]} (${decrease["change"]})', file=results)


