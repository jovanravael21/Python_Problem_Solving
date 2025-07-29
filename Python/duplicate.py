duplicate_list = [1,1,3,4,5,5,6,6,7]
duplicate_count = 0
new_list = []

for number in duplicate_list:
    if number not in new_list:
        new_list.append(number)
    else:
        duplicate_count += 1
        
print(f"Duplicate: {duplicate_list}")
print(f"New List: {new_list}")
print(f"Duplicate numbers: {duplicate_count}")