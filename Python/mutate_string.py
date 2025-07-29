# Read a given string, change the character at a given index and then print the modified string.

# TODO:
"""
Function Description

Complete the mutate_string function in the editor below.

mutate_string has the following parameters:
1. string string: the string to change
2. int position: the index to insert the character at
3. string character: the character to insert

Returns:
1. string: the altered string
"""

# TODO:
"""
The first line contains a string, string.
The next line contains an integer position, the index location and a string character, separated by a space.
"""

def mutate_string(arguments, position, character):
    contain_list = list(arguments)
    new_sentence = ""
    contain_list[position] = character
    for word in contain_list:
        new_sentence += word
    return new_sentence

argument_input = input()
index,char = input().split()
print(mutate_string(argument_input,int(index),char))