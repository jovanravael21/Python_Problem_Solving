while True:
    word = input("Enter a word: ")
    if word.lower() == "quit":
        print("End program")
        break
    
    lower_word = word.lower()
    error_found = False
    
    #* Check all letter sequences in the word
    for i in range(len(lower_word)-1):
        #* Case 1: 'ei' not preceded by 'c' -> ERROR
        if lower_word[i:i+2] == "ei" and (i == 0 or lower_word[i-1] != "c"):
            error_found = True
            break
        #* Case 2: 'ie' preceded by 'c' -> ERROR
        elif lower_word[i:i+2] == "ie" and (i > 0 and lower_word[i-1] == "c"):
            error_found = True
            break
    
    if error_found:
        print(f"Potential spelling error found in: {word}")    