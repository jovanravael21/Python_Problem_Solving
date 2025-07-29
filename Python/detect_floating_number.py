import re
# You are given a string N
# TODO: Your task is to check if N is a floating point number.

# * In this task, a valid float number must satisfy all of the following requirements:
# ! 1. Number can start with +, - or . symbol.
# ! 2. Number must contain at least 1 digit.
# ! 3. Number must have exactly one decimal point.
# ! 4. Number must not give any exceptions when converted using float(N)

"""
Input Format:
The first line contains an integer T, the number of test cases.
The next T line(s) contains a string N.

Output Format:
For each test case, print "True" if N is a valid float number. Otherwise, print "False".
"""

import re
regex_pattern = r"^[+-]?((\d*[1-9]\d*(\.\d*)?)|\.\d+)$" # TODO: Create a regex pattern to match the substring

input_number = int(input())
for i in range (input_number):
    input_items = input()
    if re.search(regex_pattern,input_items):
        print(True)
    else:
        print(False)