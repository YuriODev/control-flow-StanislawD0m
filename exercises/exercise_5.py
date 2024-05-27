# Your solution to Exercise 5
#  python -m unittest tests/test_exercise_5.py
a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))
output = "No roots."
if a == 0 and b == 0 and c == 0:
    output = "Infinite roots."
elif a == 0:
    if b != 0:
        output = f"{-c / b}"
elif b == 0:
    if c != 0:
        root1 = (-c / a) ** 0.5
        root2 = -(-c / a) ** 0.5
        output = f"{root1} and {root2}"
    else:
        output = "0"
else:
    d = b ** 2 - 4 * a * c
    if d > 0:
        root1 = (-b + d ** 0.5) / (2 * a)
        root2 = (-b - d ** 0.5) / (2 * a)
        output = f"{root1} and {root2}"
    elif d == 0:
        root = -b / (2 * a)
        output = f"{root}"
print(output)

