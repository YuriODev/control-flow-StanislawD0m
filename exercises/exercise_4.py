# Your solution to Exercise 4
#   python -m unittest tests/test_exercise_4.py
grade = int(input())
if grade >= 1 and grade <= 3 : 
    print("initial level")
elif grade <= 6 :
    print("average level")
elif grade <= 9 :
    print("sufficient level")
elif grade <= 12 :
    print("high level")
else:
    print("level is absent")