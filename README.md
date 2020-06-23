# Guess XSD data type

The purpose of this 'package' is to guestimate a primitive XSD datatype as defined in section 3.3 here: https://www.w3.org/TR/xmlschema11-2/ Currently covers: string, decimal (and integer), date, anyURI...

If you have Python (3.x) installed you can run it from command line.
```
pip install guess-xsd-type
```

There are currently three functions. One requires a value inputted by a user:
```
python guess_xsd_user_input.py
```

Another function allows for a csv to be passed on. Currently the flavour of guessing is 'one-shot', which means that just for the first value of a column the XSD datatype is guessed. To use (function,filename,delimiter):
```
python guess_one_shot.py ./example_stolpersteine.csv ';'

```

A repeated one-shot function, checks for all values in a variable and provides a guestimate if for all values the same datatype was found, or suggest 'string' as datatype. In that case a warning is given and the number and type of datatypes found is reported.

```
python repeated_one_shot.py ./example_stolpersteine.csv ';'
```
