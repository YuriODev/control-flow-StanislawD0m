# Your solution to Exercise 1    python -m unittest tests/test_exercise_1.py
alex_age = int(input(""))
tatayana_age = int(input(""))
if alex_age < tatayana_age:
    print("Tatyana is the eldest.")
elif tatayana_age < alex_age :
    print("Alex is the eldest.")
else:
    print("Alex and Tatyana are of the same age.")