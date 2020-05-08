# Guess XSD data type

The purpose of this 'package' is to guestimate a primitive XSD datatype as defined in section 3.3 here: https://www.w3.org/TR/xmlschema11-2/ Currently covers: string, decimal (and integer), date, anyURI...

If you have Python (3.x) installed you can run it from command line. There are two functions. One requires a value inputted by a user:
```
python guess_xsd_user_input.py
```

The other function allows for a csv to be passed on. Currently the flavour of guessing is 'one-shot', which means that just for the first value of a column the XSD datatype is guessed. To use (function,filename,delimiter):
```
python guess_one_shot.py ./example_stolpersteine.csv ';'
```
