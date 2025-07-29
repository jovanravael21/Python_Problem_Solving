# Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given m scores. 
# Store them in a list and find the score of the runner-up.

n = int(input())
arr = map(int, input().split())
new_list = []

for items in arr:
    if items not in new_list:
        new_list.append(items)

highest_rank = sorted(new_list,reverse=True) #TODO: Sort the list in descending order.
# * The highest score is the first element of the list.
print(highest_rank[1])