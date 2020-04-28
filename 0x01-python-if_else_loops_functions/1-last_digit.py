#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    n = -((-1 * number) % 10)
else:
    n = number % 10
if n > 5:
    print("Last digit of {:d} is {} and is greater than {}\ "
          .format(number, n, 5, 0))
elif n == 0:
    print("las digit of {} is {} and is {}".format(number, n, 0))
else:
    print("las digit of {} is {} and is less than {} and not {}\ "
          .format(number, n, 6, 0))
