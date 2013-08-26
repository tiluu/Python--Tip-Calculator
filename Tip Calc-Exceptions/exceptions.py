import sys
from optparse import OptionParser
from tip_calculator_as_functions import calculate_rate
from tip_calculator_as_functions import calculate_meal_costs


#response = sys.argv[1:] #grabs command line inputs, doesn't include filename
list = ['cost', 'tax', 'tip']
def main():
	results = {}
	
	for index, k in enumerate(list):
		try:
			results[k] = float(sys.argv[index+1])

		except (ValueError, IndexError):
			print 'Sorry, you must supply numbers for all input parameters to this script. Try again.' 
			
			results[k] = float(raw_input('Please enter meal'+k +':'))

	
	meal_info = calculate_meal_costs(results['cost'], results['tax'] , results["tip"])
	print "The base cost of your meal was ${0:.2f}.".format(meal_info['meal_base'])
	print "You need to pay ${0:.2f} for tax.".format(meal_info['tax_value'])
	print "Tipping at a rate of {0}%, you should leave ${1:.2f} for a tip.".format(
                                        int(100*meal_info['tip_rate']), 
                                        meal_info['tax_value'])
	print "The grand total of your meal is ${0:.2f}.".format(meal_info['total'])


if __name__ == '__main__':
    main()