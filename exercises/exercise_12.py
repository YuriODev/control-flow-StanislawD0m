# Your solution to Exercise 12
num = int(input("Enter a 4 digit number: "))
dig1 = num % 10000 // 1000
dig2 = num % 1000 // 100
dig3 = num % 100 // 10
dig4 = num % 10
dig1 = "*" if dig1 % 2 == 0 else str(dig1)
dig2 = "*" if dig2 % 2 == 0 else str(dig2)
dig3 = "*" if dig3 % 2 == 0 else str(dig3)
dig4 = "*" if dig4 % 2 == 0 else str(dig4)
print(dig1 + dig2 + dig3 + dig4)