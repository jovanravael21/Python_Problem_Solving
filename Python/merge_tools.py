# Example

"""
s = 'AAABCADDE'
k = 3
"""

"""
There are three substrings of length  to consider: 'AAA', 'BCA' and 'DDE'. 
The first substring is all 'A' characters, so u1 = 'A' . 
The second substring has all distinct characters, so u2 = 'BCA'. 
The third substring has 2 different characters, so u3 = 'DE'. 
Note that a subsequence maintains the original order of characters encountered. 
The order of characters in each subsequence shown is important.
"""

def merge_the_tools(text,n):
    substring = []
    result = []
    substring_container = ""
    
    i = 0
    while i < len(text):
        substring.append(text[i:i+n]) # TODO: Create substring of length n
        i += n
    
    # * Iterate through the substring list and remove duplicates
    for items in substring:
        for a in range (len(items)):
            if items[a] not in substring_container: # TODO: Check if the character is already in the substring_container
                substring_container += items[a]
        result.append(substring_container)
        substring_container = ""

    for items in result:
        print(items)

text_input = input()
n_input = int(input())
merge_the_tools(text_input,n_input)