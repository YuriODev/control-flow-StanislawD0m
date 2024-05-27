# Your solution to Exercise 15
# python -m unittest tests/test_exercise_15.py
day = int(input())
month = int(input())
year = int(input())
if month == 9 or month == 4 or month == 6 or month == 11 :
    if day == 30 :
        day = 1
        month = str(month + 1)
    else :
        day += 1
if month == 2 :
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0 :
        if day == 29 :
            day = 1
            month = "3"
        else: 
            day += 1
    else:
        if day == 28 :
            day = 1
            month = "3"
        else: 
            day += 1
if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
    if day == 31 :
        day = 1
        month += 1
    else:
        day += 1
if int(month) > 12 :
    month = 1
    year += 1
print(f"{day}.{month}.{year}")