# Your solution to Exercise 17
# python -m unittest tests/test_exercise_17.py
ticket = input("Enter the ticket number: ")
sum1 = (int(ticket) % 1000000 // 100000) + (int(ticket) % 100000 // 10000) + (int(ticket) % 10000 // 1000)
sum2 = (int(ticket) % 1000 // 100) + (int(ticket) % 100 // 10) + (int(ticket) % 10)
if sum1 == sum2 :
    print("Happy")
else: 
    print("Ordinary")