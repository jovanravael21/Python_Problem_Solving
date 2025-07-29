import re
# These expressions return the indices of the start and end of the substring matched by the group.

# TODO: Create a regex pattern to match the substring
"""
1. You are given a string .
2. Your task is to find the indices of the start and end of string l in S.
"""

"""
SAMPLE INPUT:
aaadaa
aa

SAMPLE OUTPUT:
(0, 1)  
(1, 2)
(4, 5)
"""

import re

S = input()
k = input()

pattern = f'(?=({re.escape(k)}))' # TODO: Create a regex pattern to match the substring

matches = list(re.finditer(pattern, S)) # * Find all matches of the pattern in the string S

if matches:
    for match in matches:
        start = match.start()
        end = start + len(k) - 1
        print(f"({start}, {end})")
else:
    print("(-1, -1)")

