# Task
# Given an integer, , perform the following conditional actions:

# If  is odd, print Weird
# If  is even and in the inclusive range of 2 to 5, print Not Weird
# If  is even and in the inclusive range of 6 to 20 , print Weird
# If  is even and greater than 20, print Not Weird

# N range : 1-100
number_input = int(input("Your Number: ").strip())

# * 4:2 = 2; 4%2=0
if number_input % 2 == 0:
    if 2 <= number_input <= 5:
        print("Not Weird")
    elif 6 <= number_input <= 20:
        print("Weird")
    else:
        print("Not Weird")
else:
    print("Weird")