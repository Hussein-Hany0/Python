# All Assignments are in : https://elzero.org/python-assignments-lesson-from-24-to-25/

# -1
names = "hussein",
print(names)
print(type(names))

# -2
friends = ("Osama", "Ahmed", "Sayed")

first, second , third = friends

first = "Elzero"

friends = (first , second , third)

print(friends)

print(type(friends))

print(len(friends))

# -3
nums = (1, 2, 3)
letters = ("A", "B", "C")

compo = nums + letters

print(compo)
print(len(compo))

# -4
my_tuple = (1, 2, 3, 4)

a , b , _ , c = my_tuple  # _ to ignore the third item

print(f"{a} {b} {c}")