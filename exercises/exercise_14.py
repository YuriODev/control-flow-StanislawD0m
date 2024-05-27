# Your solution to Exercise 14
#python -m unittest tests/test_exercise_14.py
num = int(input("Enter a 4 digit number: "))
dig1 = num % 10000 // 1000
dig2 = num % 1000 // 100
dig3 = num % 100 // 10
dig4 = num % 10
output = False
if dig1 == dig4 and dig2 == dig3 :
    output = True
print(output)