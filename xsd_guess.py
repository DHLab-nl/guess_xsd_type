def guess_type(var):
	'''
	The purpose of this function is to guestimate a primitive XSD datatype
	as defined in section 3.3 here: https://www.w3.org/TR/xmlschema11-2/
	Currently covers: string, decimal (and integer), date, anyURI... 
	'''

	import re		# for regular expressions

	'''
	Converting input to string and then guessing 
	input data type
	'''
	
	var = str(var)
	var = var.lower()	# convenience for later on (checking for anyURI)
	
	if var.startswith('-'): # removes 'negative' sign. assuming it doesn't matter for strings
		var = var[1:]
	
	if var.isdigit():	# only numbers?
		'''
		Years are a tough to guess from a single element.
		In the future, might guess it from a series with
		the repitatieve first 2 digits, or variable name.
		For now basically 1000AD-2100AD
		'''
		if len(var)==4 and int(str(var)[:2])<21:
			varType = 'gYear'
		else:
			varType = 'integer'
	
	elif var.startswith('http')==False and var.count('.')==1: 	# perhaps a decimal, circumventing for http://bla.com
		twoParts = var.split('.')
		if twoParts[0].isdigit() and twoParts[1].isdigit():
			varType = 'decimal'
		else:
			varType = 'string'

	elif var.count('-')==2:		# perhaps a date
		threeParts = var.split('-')
		if threeParts[0].isdigit() and threeParts[1].isdigit() and threeParts[2].isdigit() \
		and len(threeParts[0])==4 and len(threeParts[1])==len(threeParts[2])==2:
			varType = 'date'
		else:
			varType = 'string'
	
	elif var.startswith('http')==True:	# perhaps a URI
			varType = 'anyURI'

	else:					# catchall
			varType = 'string'

	print('"'+var+'"'+'^^XSD:'+varType)

# guess_type()
