# Your solution to Exercise 8
#python -m unittest tests/test_exercise_8.py
dig3 = int(input("Enter a three digit number: "))
n = int(input("Enter a digit: "))
if n == dig3 % 1000 // 100 or n == dig3 % 100 // 10 or n == dig3 % 10 :
    print("True")
else :
    print("False")