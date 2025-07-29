# * Let's learn about list comprehensions! 
# * You are given three integers x,y and z  representing the dimensions of a cuboid along with an integer. 
# TODO: Print a list of all possible coordinates given by (i,j,k) on a 3D grid where the sum of i+j+k is not equal to n
"""
TODO:
x = 1
y = 1
z = 2
n = 3

[[0,0,0],[0,0,1],[0,0,2],[0,1,0],[0,1,1],[1,0,0],[1,0,1],[1,1,0],[1,1,2]]
"""
x = int(input("X = "))
y = int(input("Y = "))
z = int(input("Z = "))
n = int(input("n = "))
list_result = []

for a in range (x+1):
    for b in range (y+1):
        for c in range (z+1):
            if (a+b+c) != n:
                list_result.append([a,b,c])

print(list_result)