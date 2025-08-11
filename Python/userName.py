username = input("Enter username: ")

beginningWithLetter = False
noSpacing = False
numAndLetter = False

# * Starts with letter
if username[0].isalpha():
    beginningWithLetter = True

# * No spacing
if not " " in username:
    noSpacing = True

# * Must number & letter only
for character in username:  #TODO: parse each cahracter -> Jovan21
    if character.isalpha() or character.isalnum():
        numAndLetter = True
    else:
        numAndLetter = False
        break  #TODO: break whenever invalid
    

if(beginningWithLetter & noSpacing & numAndLetter):
    print("Username is valid")
else:
    print("Username is not valid")