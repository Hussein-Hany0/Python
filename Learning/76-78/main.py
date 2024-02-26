# All Assignments are in : https://elzero.org/python-assignments-lesson-from-76-to-78/

# -1
import random

print(f"Random Number Between 10 And 50 => {random.randint(10 , 50)}")

print(f"Random Even Number Between 2 And 10 => {random.randrange(2 , 10 , 2)}")

print(f"Random Odd Number Between 1 And 9 => {random.randrange(1 , 9 , 2)}")

print(dir(random))


# -2
import my_mod

my_mod.sayHello("Hussein")
my_mod.sayWelcome("Hussein")

# -3
from my_mod import sayWelcome

sayWelcome("Hussein")

# -4
from my_mod import sayWelcome as new_welcome

new_welcome("Hussein")