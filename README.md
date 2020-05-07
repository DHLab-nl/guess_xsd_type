# Guess XSD data type

This is a small python script that tries to infer the XSD datatype of a string as inputted by a user. The purpose of this function is to guestimate a primitive XSD datatype as defined in section 3.3 here: https://www.w3.org/TR/xmlschema11-2/ Currently covers: string, decimal (and integer), date, anyURI...

If you have Python (3.x) installed you can run it from command line via:
```
python guess_xsd_type.py
```
