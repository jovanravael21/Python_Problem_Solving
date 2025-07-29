word_input = input("Enter Word:")
vowels_list = "aiueoAIUEO"
vowels = 0
consonants = 0

for word in word_input:
    if word in vowels_list:
        vowels += 1
    else:
        consonants += 1

print(f"{word_input}, Vowels:{vowels}, Consonants:{consonants}")