# The provided code stub reads an integer, n , from STDIN. For all non-negative integers i < n -> i^2, print i.

# Example
# The list of non-negative integers that are less than  is. 
# Print the square of each number on a separate line.

number_input = int(input("Enter Your Number: ").strip())
for i in range (0,number_input):
    print(i**2)