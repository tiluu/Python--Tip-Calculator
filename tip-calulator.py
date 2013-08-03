 #! /usr/bin/env python 
cost = float(raw_input('What is the cost of meal?'))
tax = float(raw_input('What is the tax?')) 
tip = float(raw_input('How much is tip?')) 
tip_percentage = tip/100
tax_percentage = tax/100

tax_value = tax*cost
meal_tax = cost*tax_percentage
meal_tip = cost*tip_percentage
total = cost+meal_tax+meal_tip

print ('The base cost of you meal was $%s') % '{:.2f}'.format(cost)
print ('You need to pay $%s for tax.') % '{:.2f}'.format(tax)
print ('Tipping at a rate of 15%%, you should leave $%s for a tip.') % '{:.2f}'.format(meal_tip)
print ('The grand total of your meal is $%s') % '{:.2f}'.format(total)


print ('NEW FORMAT!!!!!---------------------')
print ('The base cost of you meal was ${}').format('{:.2f}'.format(cost))
print ('You need to pay ${} for tax.').format('{:.2f}'.format(meal_tax))
print ('Tipping at a rate of 15%, you should leave ${} for a tip.').format('{:.2f}'.format(meal_tip))
print ('The grand total of your meal is ${}').format('{:.2f}'.format(total))


