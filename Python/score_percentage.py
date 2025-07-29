# Find Score Percentage
# * The provided code stub will read in a dictionary containing key/value pairs of name:[marks] for a list of students. 
# TODO: Print the average of the marks array for the student name provided, showing 2 places after the decimal.

"""
# TODO
student marks
alpha: [20,30,40]
beta: [30,50,70]
query_name = beta
result = (30+50+70)/3 = 50.0
"""

number_student = int(input())
student_marks = {}
for a in range(number_student):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input()

average_score = format(sum(student_marks[query_name])/3,".2f")
print(average_score)


