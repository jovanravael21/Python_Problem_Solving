import re
pattern = r'^\$[0-9]{1,4}\.[0]{2}'

if re.match(pattern,"$.00"):
    print("The result mathces with the description")
else:
    print("The result doesn't match with the description")
