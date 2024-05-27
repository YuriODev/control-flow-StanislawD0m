# Your solution to Exercise 6
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
point_A = x1**2 + y1**2
point_B = x2**2 + y2**2
if point_A > point_B :
    print("A is further from the origin.")
elif point_B > point_A :
    print("B is further from the origin.")
else :
    print("A and B are at the same distance from the origin. ")