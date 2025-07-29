# Kevin and Stuart want to play the 'The Minion'

# TODO:
"""
Both players are given the same string, S.
Both players have to make substrings using the letters of the string S.
"""

# ! Stuart has to make words starting with consonants.
# ! Kevin has to make words starting with vowels.

# * The game ends when both players have made all possible substrings.

# TODO:
"""
String S = BANANA
Kevin's vowel beginning word = ANA
Here, ANA occurs twice in BANANA. Hence, Kevin will get 2 Points.
"""

"""
Function Description
Complete the minion_game in the editor below.
1. minion_game has the following parameters:
2. string string: the string to analyze

Prints
string: the winner's name and score, separated by a space on one line, or Draw if there is no winner
"""

vowels_list = "AIUEO"

global kevin
global stuart 

def minion_games(text):
    kevin,stuart = 0,0
    length = len(text)
    
    for a in range (length):
        if text[a] in vowels_list:
            kevin += length - a # TODO: Kevin's score is incremented by the number of substrings starting with a vowel.
            # * BANANA -> A, AN, ANA, ANAN, ANANA
        else:
            stuart += length - a # TODO: Stuart's score is incremented by the number of substrings starting with a consonant.
            # * BANANA -> B, BA, BAN, BANA, BANAN, BANANA

    if kevin > stuart:
        print(f"Kevin {kevin}")
    elif kevin < stuart:
        print(f"Stuart {stuart}")
    else:
        print(f"Draw")

minion_input = input().strip()
minion_games(minion_input)