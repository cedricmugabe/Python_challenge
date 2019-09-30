import os
import csv

budget_data.csv = os.path.join('..', 'Resources', 'budget_data.csv')

mcount = 0; total = 0; PreValue = 0; Diff = 0; DiffMax = 0; DiffMin = 0


with open(budget_data.csv, newline='') as csvfile:
     csvreader = csv.reader(csvfile, delimiter=',')
     csv_header = next(csvreader)
     print(f'Financial Analysis'+'\n')
     print(f'----------------------------'+'\n')
     for i in csvreader:
         month = i[0]
         Amount = i[1]
         iAmount = int(Amount)
         Diff =  iAmount - PreValue
        
         if DiffMax < Diff:
            DiffMax = Diff
            DiffMaxDate = month
         
         if DiffMin > Diff:
            DiffMin = Diff
            DiffMinDate = month

         PreValue = iAmount   
       
         mcount = mcount + 1
         total += int(Amount) 


print(f'Total Months : {mcount}')

print(f'Total: $ {total}')

print(f'Greatest Increase in Profits: {DiffMaxDate} : ($ {DiffMax})')

print(f'Greatest Decrease in Profits: {DiffMinDate} : ($ {DiffMin})')
