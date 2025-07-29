# You are given a string s consisting only of digits 0-9, commas (,) and dots (.)

# TODO:
"""
Your task is to complete the regex_pattern defined below, which will be used to re.split() all of the (,) and (.) symbols in .

It’s guaranteed that every comma and every dot in  is preceeded and followed by a digit.
"""

"""
SAMPLE INPUT:
100,000,000.00

SAMPLE OUTPUT:
100
000
000
00
"""

import re
regex_pattern = r"[,\.]"
string_input = input()

x = re.split(regex_pattern,string_input)
for items in x:
    print(items)