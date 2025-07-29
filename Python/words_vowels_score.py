# Consider that vowels in the alphabet are a, e, i, o, u and y.

# TODO:
"""
The input is read by the provided locked code template. 
In the first line, there is a single integer n denoting the number of words. 
In the second line, there are n space-separated lowercase words.
"""

"""
SAMPLE INPUT:
3
programming is awsome

SAMPLE OUTPUT:
4
"""

"""
There are 3 words in the input: programming, is and awesome.
The score of programming is 1 since it contains 3 vowels, an odd number of vowels.
The score of is is also 1 because it has an odd number of vowels. 
The score of awesome is 2 since it contains 2 vowels, an even number of vowels. 
Thus, the total score is 1+1+2 = 4.
"""

number_input = int(input())
sentence_input = input().split()
vowels = "aiueoyAIUEOY"
vowels_count = 0
score = 0

for words in sentence_input:
    for a in range (len(words)):
        if words[a] in vowels:
            vowels_count+=1

    print(words,vowels_count)

    if vowels_count % 2 == 0:
        score += 2
    else:
        score += 1

    vowels_count = 0

print(score)