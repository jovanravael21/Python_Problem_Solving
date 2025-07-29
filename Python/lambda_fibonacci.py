# You have to generate a list of the first N fibonacci numbers, 0 being the first number.
# *  Then, apply the map function and a lambda expression to cube each fibonacci number and print the list.

"""
TODO: Concept
1. The map() function applies a function to every member of an iterable and returns the result. 
2. It takes two parameters: first, the function that is to be applied and secondly, the iterables.
3. Let's say you are given a list of names, and you have to print a list that contains the length of each name.

SAMPLE INPUT:
5

SAMPLE OUTPUT:
[0,1,1,8,27]
"""

# TODO: Fibonacci Number Generator
def fibonacci(n):
    fibonacci_list = []
    for i in range (n):
        if i < 2:
            fibonacci_list.append(i)
        else:
            fibonacci_number = fibonacci_list[i-1]+fibonacci_list[i-2]
            fibonacci_list.append(fibonacci_number)
    return fibonacci_list

n = int(input())

# TODO: Generating the cube for each elements in the Fibonacci
cube = list(map(lambda x:x**3, fibonacci(n)))
print(cube)