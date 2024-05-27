# Your solution to Exercise 3
#python -m unittest tests/test_exercise_3.py
num = int(input())
if num == 0 :
    print("Green")
elif num >= 1 and num <= 10 :
    colour = "Black" if num % 2 == 0 else "Red"
    print(colour)
elif num <= 18 :
    colour = "Red" if num % 2 == 0 else "Black"
    print(colour)
elif num <= 28 :
    colour = "Black" if num % 2 == 0 else "Red"
    print(colour)
elif num <= 36 :
    colour = "Red" if num % 2 == 0 else "Black"
    print(colour)
else:
    print("The bet will not play!")