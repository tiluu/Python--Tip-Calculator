 #! /usr/bin/env python 
from optparse import OptionParser #how OptionParser is imported

parser = OptionParser() 

parser.add_option('-c', '--cost', dest='cost', type='float')
parser.add_option('-s', '--tax', dest='tax', type='float')
parser.add_option('-t', '--tip', dest='tip', type='float') 

(options, args) = parser.parse_args()

if not options.cost:
    parser.error('You didn\'t enter the cost of meal')
if not options.tax:
    parser.error('You did\'t enter the tax of meal')
    
tip_valaue = options.tip/100
tax_value = options.tax/100

tax_value = options.tax*option.cost
meal_tax = options.cost+tax_value
meal_tip = options.cost*tip_value
total = options.cost+meal_tax+meal_tip

print ('The base cost of you meal was $%s') % '{:.2f}'.format(options.cost)
print ('You need to pay $%s for tax.') % '{:.2f}'.format(meal_tax)
print ('Tipping at a rate of 15%%, you should leave $%s for a tip.') % '{:.2f}'.format(meal_tip)
print ('The grand total of your meal is $%s') % '{:.2f}'.format(total)


print ('NEW FORMAT!!!!!---------------------')
print ('The base cost of you meal was ${}').format('{:.2f}'.format(options.cost))
print ('You need to pay ${} for tax.').format('{:.2f}'.format(meal_tax))
print ('Tipping at a rate of 15%, you should leave ${} for a tip.').format('{:.2f}'.format(meal_tip))
print ('The grand total of your meal is ${}').format('{:.2f}'.format(total))


