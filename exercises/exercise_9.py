# Your solution to Exercise 9
#  python -m unittest tests/test_exercise_9.py
dig3 = int(input("Enter a three digit number: "))
sum = (dig3 % 1000 // 100)+ (dig3 % 10)
if sum == dig3 % 100 // 10 :
    print("=")
elif  sum > dig3 % 100 // 10 :
    print(">")
else :
    print("<")