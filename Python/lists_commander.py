# List Functions
# *Consider a list (list = []). You can perform the following commands:

"""
TODO: 
1. Insert i e: Insert integer  at position i.
2. Print: Print the list.
3. Remove e: Delete the first occurrence of integer e.
4. Append e: Insert integer  at the end of the list.
5. Sort: Sort the list.
6. Pop: Pop the last element from the list.
7. Reverse: Reverse the list.
"""

"""
Sample Input:
12
insert 0 5
insert 1 10
insert 0 6
print
remove 6
append 9
append 1
sort
print
pop
reverse
print

Sample Output:
[6, 5, 10]
[1, 5, 9, 10]
[9, 5, 1]
"""

def command_executer(list_result,command_input,list_input):
    if command_input == "insert":
        list_result.insert(int(list_input[0]),int(list_input[1]))
    elif command_input == "remove":
        list_result.remove(int(list_input[0]))
    elif command_input == "append":
        list_result.append(int(list_input[0]))
    elif command_input == "sort":
        list_result.sort()
    elif command_input == "reverse":
        list_result.reverse()
    elif command_input == "pop":
        list_result.pop()
    else:
        print(list_result)

N = int(input())
number_list = []
for i in range (N):
    command_list = input()
    command, *args = command_list.split()
    command_executer(number_list,command,args)