# Given the names and grades for each student in a class of N students
# * store them in a nested list and print the name(s) of any student(s) having the second lowest grade.
# ! If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.

number_students = int(input())
nested_list = []
score_list = []
for a in range(number_students):
    name = input()
    score = float(input())
    nested_list.append([name,score])
    score_list.append(score)

ordered_score = []
for items in score_list:
    if items not in ordered_score:
        ordered_score.append(items)
ordered_score = sorted(ordered_score)


ordered_list = sorted(nested_list,key=lambda x:x[1])
second_lowest = sorted(list(filter(lambda x:x[1]==ordered_score[1],ordered_list)))

for a in range(len(second_lowest)):
    print(second_lowest[a][0])