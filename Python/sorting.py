original_list = [3,4,5,2,1,6]
for a in range (0,len(original_list)):
    for b in range (a+1,len(original_list)):
        if original_list[a] > original_list[b]:
            original_list[a],original_list[b] = original_list[b],original_list[a]
print(original_list)