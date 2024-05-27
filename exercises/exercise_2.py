# Your solution to Exercise 2      python -m unittest tests/test_exercise_2.py
age = int(input("Enter your age: "))
if age <= 1 :
    print("You are an infant.")
elif age < 13 :
    print("You are a child.")
elif age < 20 :
    print("You are a teenager.")
else:
    print("You are an adult.")