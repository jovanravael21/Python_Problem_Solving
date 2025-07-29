# You are given a string and your task is to swap cases. 
# TODO: In other words, convert all lowercase letters to uppercase letters and and vice versa

"""
INPUT: Www.HackerRank.com
OUTPUT:  wWW.hACKERrANK.COM

INPUT: Pythonist 2
OUTPUT: pYTHONIST 2
"""

def swap_case(s):
    for words in s:
        if words.isalpha():
            if words.islower():
                words.upper()
            else:
                words.lower()
    return s

sentence_input = input("")
result = swap_case(sentence_input)
print(result)