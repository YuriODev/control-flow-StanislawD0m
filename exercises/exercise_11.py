# Your solution to Exercise 11
# python -m unittest tests/test_exercise_11.py
year = int(input("Enter the year: "))
output = "Ordinary year."
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0 :
    output = "Leap year."
print(output)