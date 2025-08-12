while True:
    word = input("Enter a word: \n")
    if word.lower() == "quit":
        print("End program")
        break

    if "ie" in word: # * Problem is needs to be "ie" not "ei"
        if "cie" not in word:
           print(f"Potential spelling error found in: {word}")  
           # * I deleted the input for enter a word
           # * You only need to use one input only because if it's not a spelling mistake
           # * It will loop again until 
           break
 