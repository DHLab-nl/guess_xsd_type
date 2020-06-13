def guess_one_shot():
	
	'''
	The purpose of this function is to read the example csv file
	and guess the XSD data type of each variable/column
	by just looking at the first value/cell in that 
	csv file.
	'''

	import pandas as pd
	import argparse
	import sys

	from xsd_guess import guess_type			# this is our 'guess datatype' function	

	'''
	Allow for filepath to be added to command-line
	e.g. open file with: 'python guess_one_shot ./myfile.csv'
	'''

	parser = argparse.ArgumentParser()
	parser.add_argument('filename')
	parser.add_argument('sep')
	args = parser.parse_args()

	df = pd.read_csv(args.filename, sep = args.sep)		# read csv file

	fvalue = df.iloc[0]					# retrieve all first values as pd.series
	
	fvalue.apply(guess_type)
	
	
guess_one_shot()

	
