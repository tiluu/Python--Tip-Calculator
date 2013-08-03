 #! /usr/bin/env python 
cost = 20.00 #{:.2f}.format(20.00)
tax = 3.00/100 #{:.2f}.format(3.00)
tip = 15.00/100  #{:.2f}.format(3.45)
tax_value = tax*cost
meal_tax = cost+tax
meal_tip = cost*tip
total = meal_tax+meal_tip

print ('The base cost of you meal was $%f') % (cost)
print ('You need to pay $%f for tax.') % (tax)
print ('Tipping at a rate of 15%%, you should leave $%f for a tip.') % (tip)
print ('The grand total of your meal is $%f') % (total)


print ('NEW FORMAT!!!!!---------------------')
print ('The base cost of you meal was ${}').format(cost)
print ('You need to pay ${} for tax.').format(tax)
print ('Tipping at a rate of 15%, you should leave ${} for a tip.').format(tip)
print ('The grand total of your meal is ${}').format(total)

