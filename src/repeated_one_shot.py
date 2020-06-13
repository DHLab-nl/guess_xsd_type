def repeated_one_shot():
	
	'''
	The purpose of this function is to read the example csv file
	and guess the XSD data type of each variable/column
	by just looking at the first value/cell in that 
	csv file.
	'''

	import pandas as pd					# working with csv as pandas table
	import argparse						# to allow user to define csv and csv format
	import sys						# to allow user to define path to csv
	import collections					# to count number of values
	import warnings						# to notify user of inconcluse datatypes

	from xsd_guess_single import guess_type			# this is our 'guess datatype' function	

	'''
	Allow for filepath to be added to command-line
	e.g. open file with: 'python guess_one_shot ./myfile.csv'
	'''

	parser = argparse.ArgumentParser()
	parser.add_argument('filename')
	parser.add_argument('sep')
	args = parser.parse_args()

	df = pd.read_csv(args.filename, sep = args.sep)		# read csv file

	'''
	For each column we apply the guess_type() to each value in that column
	Next we check whether all the values result in the same datatype
	If this is not the case we throw an error, and set the datatype to string
	'''

	for column in range (1,len(df.columns)):
		x = df.iloc[:,column].apply(guess_type)
		counter = collections.Counter(x)
		if len(counter)==1: #this means all values were coded in the same way
			print(df.columns[column], counter.most_common(1)[0][0])			# first element in the counter list
		else:
			# warnings.warn('Multiple datatypes in "' + df.columns[column] +'". Converted to string.\n', Warning, stacklevel=2)
			print(df.columns[column], 'string')

		
	'''
	The next bit of code is redundant but I wanted to raise
	a warning in the 'else' case (forcing to string) but it
	clutters the actual output.
	'''

	for column in range (1,len(df.columns)):
		x = df.iloc[:,column].apply(guess_type)
		counter = collections.Counter(x)
		if len(counter)>1: #this means values were not coded in the same way
			warnings.warn('Multiple datatypes in "' + df.columns[column] +'". Converted to string.\n', Warning, stacklevel=1)
			print(df.columns[column], counter.most_common())                 # first element in the counter list

repeated_one_shot()
