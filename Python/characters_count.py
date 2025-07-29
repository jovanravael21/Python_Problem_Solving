def count_characters_count(sentence_input):
    characters_count = 0
    numbers_count = 0
    spaces_count = 0
    for items in sentence_input:
        if items.isalpha():
            characters_count+=1
        elif items.isdigit():
            numbers_count+=1
        else:
            spaces_count+=1
    print(f"{sentence_input} has {characters_count} alphabets, {numbers_count} numbers, & {spaces_count} spaces.")

user_input = str(input("Enter Your Sentence: "))
count_characters_count(user_input)