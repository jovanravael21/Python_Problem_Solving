# Enter your code here. Read input from STDIN. Print output to STDOUT
sample = int(input())
for i in range(sample):
    try:
        number, division = input().split()
        print(int(number) // int(division))
    except (ZeroDivisionError, ValueError) as e:
        print("Error Code:", e)
