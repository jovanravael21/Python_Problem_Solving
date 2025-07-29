# You are given a spreadsheet that contains a list of N athletes and their details (such as age, height, weight and so on). 
# !: You are required to sort the data based on the K^th attribute and print the final resulting table. 
# * Follow the example given below for better understanding.

"""
The first line contains N and M separated by a space.
The next N lines each contain M elements.
The last line contains K.
"""

"""
INPUT:
5 3
10 2 5
7 1 0
9 9 9
1 23 12
6 5 9
1

OUTPUT:
7 1 0
10 2 5
6 5 9
9 9 9
1 23 12
"""

nm = input().split()
n = int(nm[0])
m = int(nm[1])
arr = []
for _ in range(n):
    arr.append(list(map(int, input().rstrip().split())))
k = int(input())
new_data = sorted(arr, key=lambda x:x[k])
for data in new_data:
    print(*data)