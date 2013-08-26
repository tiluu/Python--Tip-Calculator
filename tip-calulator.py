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

tax_value = options.tax*options.cost

meal_tip = options.cost*options.tip
total = options.cost+tax_value+meal_tip

print ('The base cost of you meal was ${}').format('{:.2f}'.format(options.cost))
print ('You need to pay ${} for tax.').format('{:.2f}'.format(tax_value))
print ('You should leave ${} for a tip.').format('{:.2f}'.format(meal_tip))
print ('The grand total of your meal is ${}').format('{:.2f}'.format(total))


