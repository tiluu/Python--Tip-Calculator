 #! /usr/bin/env python 
cost = 20.00 #{':.2f'}.format(20.00)
tax = 3.00/100 #{':.2f'}.format(3.00)
tip = 15.00/100  #{':.2f'}.format(3.45)
tax_value = tax*cost
meal_tax = cost+tax
meal_tip = cost*tip
total = meal_tax+meal_tip

print ('The base cost of you meal was $%s') % '{:.2f}'.format(cost)
print ('You need to pay $%s for tax.') % '{:.2f}'.format(tax)
print ('Tipping at a rate of 15%%, you should leave $%s for a tip.') % '{:.2f}'.format(tip)
print ('The grand total of your meal is $%s') % '{:.2f}'.format(total)


print ('NEW FORMAT!!!!!---------------------')
print ('The base cost of you meal was ${}').format('{:.2f}'.format(cost))
print ('You need to pay ${} for tax.').format('{:.2f}'.format(tax))
print ('Tipping at a rate of 15%, you should leave ${} for a tip.').format('{:.2f}'.format(tip))
print ('The grand total of your meal is ${}').format('{:.2f}'.format(total))

