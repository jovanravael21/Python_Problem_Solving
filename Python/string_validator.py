# String Validation

# TODO:
"""
In the first line, print True if S has any alphanumeric characters. Otherwise, print False.
In the second line, print True if S has any alphabetical characters. Otherwise, print False.
In the third line, print True if S has any digits. Otherwise, print False.
In the fourth line, print True if S has any lowercase characters. Otherwise, print False.
In the fifth line, print True if S has any uppercase characters. Otherwise, print False.
"""

s = input()
for char in s:
    print(any(char.isalnum()))

for char in s:
    print(any(char.isalpha()))

for char in s:
    print(any(char.isdigit()))

for char in s:
    print(any(char.islower()))

for char in s:
    print(any(char.isupper()))