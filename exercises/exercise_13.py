# Your solution to Exercise 13
#python -m unittest tests/test_exercise_13.py
num = int(input("Enter a 4 digit number: "))
dig1 = num % 10000 // 1000
dig2 = num % 1000 // 100
dig3 = num % 100 // 10
dig4 = num % 10
if dig1 == dig2 or dig1 == dig3 or dig1 == dig4 or dig2 == dig3 or dig2 == dig4 or dig3 == dig4:
    output = False
else: 
    output = True
print(output)