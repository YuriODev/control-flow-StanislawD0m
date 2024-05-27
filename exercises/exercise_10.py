# Your solution to Exercise 10
# python -m unittest tests/test_exercise_10.py
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
x3 = int(input())
y3 = int(input())
if x1 == x2 and y1 == y3 :
    output = "Yes"
else:
    output = "No"
if x1 == x2 and x1 == x3 and x2 == x3 or y1 == y2 and y1 == y3 and y2 == y3 :
    output = "No"
print(output)