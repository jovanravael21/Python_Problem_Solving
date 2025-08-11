while True:
    word = input("Enter a word: \n")
    if word.lower() == "quiet":
        print("End program")
        break
    if "ei" in word:
       if "cei" not in word:
           print(f"Potential spelling error found in: {word}")
           print("Enter a word: ")
           
           break
 