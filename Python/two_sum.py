# Two Sum Function
def twoSum(numsList, target):
    newList = []
    numsItem = len(numsList)

    for i in range (numsItem):
        if numsList[i] != "," :
            newList.append(int(numsList[i]))
            i += 1
 
    listItem = len(newList)
    for a in range (listItem):
        for b in range (listItem):
            if newList[a] + newList[b] == target:
                return f"[{newList[a]}, {newList[b]}]"
            elif newList[a] + newList[b] != target:
                b += 1
            elif b == listItem :
                a += 1
                b = 0
            else:
                return "We can not find the right answer"

# Input Data
userList = list(input("List: "))
while True:
    try:
        userTarget = int(input("Target: "))
        break
    except ValueError:
        print("Error: You need to enter a number")
        continue

print(twoSum(userList,userTarget))