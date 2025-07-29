import re
pattern = r'^\$[0-9]{1,4}\.[0]{2}'
print(re.match(pattern,"$.00"))