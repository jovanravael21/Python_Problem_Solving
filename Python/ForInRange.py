lowerBound = int(input("Enter Lower Bound: "))
upperBound = int(input("Enter Upper Bound: "))
divisor = int(input("Enter Divisor: "))

isValid = True
if not lowerBound <= upperBound:
    isValid = False

if not divisor > 0:
    isValid = False

if divisor > upperBound:
    isValid = False

if isValid:
    for i in range(lowerBound,upperBound+1):
        if i % divisor == 0:
            print(i)