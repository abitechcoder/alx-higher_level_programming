#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# YOUR CODE HERE
last_digit = number % 10 if number > 0 else ((-number % 10) * -1)
message = "Last digit of {} is {} and".format(number, last_digit)
if last_digit > 5:
    print(message, "is greater than 5")
elif last_digit == 0:
    print(message, "is 0".format(number, last_digit))
else:
    print(message, "is less than 6 and not 0".format(number, last_digit))
