def palindromeNumber(x):
    reverseNum = str(x[::-1])
    if x == reverseNum :
        return True
    else:
        return False
inputUser = input("Enter Your Value: ")
print(palindromeNumber(inputUser))