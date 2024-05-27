# Your solution to Exercise 7
#python -m unittest tests/test_exercise_7.py
num1 = float(input())
num2 = float(input())
operation = input()
if operation == "+" :
    output = num1 + num2
elif operation == "-" :
    output = (num1 - num2) / 1
elif operation == "/" :
    if num2 == 0 :
        output = "Division by 0!"
    else :
        output = num1 / num2
elif operation == "*" :
    output = num1 * num2
elif operation == "mod" :
    output = num1 % num2
elif operation == "pow" :
    output = num1 ** num2
print(output)