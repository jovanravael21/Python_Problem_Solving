# You are given a string, and you have to validate whether it's a valid Roman numeral. 
# * If it is valid, print True. Otherwise, print False. 
# * Try to create a regular expression for a valid Roman numeral.

# TODO:
"""
Input Format
A single line of input containing a string of Roman characters.

Output Format
Output a single line containing True or False according to the instructions above.
"""

import re
pattern = r'^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|VI|V?I{0,3})$'
# ! M{0,3} = 0 to 3 Ms (1000–3000)
# !(CM|CD|D?C{0,3}) = 900(CM), 400(CD), or combinations of D and C(up to 800)
# !(XC|XL|L?X{0,3}) = 90(XC), 40(XL), or combinations of L and X
# !(IX|IV|V?I{0,3}) = 9(IX), 4(IV), or combinations of V and I

print(str(bool(re.match(pattern,input()))))