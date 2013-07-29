 #! /usr/bin/env python 
cost = {:.2f}.format(20.00)
tax = {:.2f}.format(3.00)
tip = {:.2f}.format(3.45)
total = {:.2f}.format(26.45)

print ('The base cost of you meal was $%f') % (20.00)
print ('You need to pay $%f for tax.') % (3.00)
print ('Tipping at a rate of 15%%, you should leave $%f for a tip.') % (3.45)
print ('The grand total of your meal is $%f') % (26.45)


print ('NEW FORMAT!!!!!---------------------')
print ('The base cost of you meal was ${}').format(cost)
print ('You need to pay ${} for tax.').format(tax)
print ('Tipping at a rate of 15%, you should leave ${} for a tip.').format(tip)
print ('The grand total of your meal is ${}').format(total)

#the % sign, is it an