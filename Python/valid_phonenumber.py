# Let's dive into the interesting topic of regular expressions! You are given some input, and you are required to check whether they are valid mobile numbers.
# TODO: A valid mobile number is a ten digit number starting with a 7, 8 or 9.
"""
A valid mobile number is a ten digit number starting with a 7, 8 or 9 .

Input Format:
The first line contains an integer N, the number of inputs.
N lines follow, each containing some string.

Output Format:
For every string listed, print "YES" if it is a valid mobile number 
"NO" if it is not on separate lines. Do not print the quotes.
"""

import re
regex_pattern = r"^[789]\d"

number_input = int(input())
for i in range (number_input):
    phone_number_input = input()
    if re.match(regex_pattern,phone_number_input) and len(phone_number_input) == 10:
        print("YES")
    else:
        print("NO")