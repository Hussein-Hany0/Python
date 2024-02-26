# All Assignments are in : https://elzero.org/python-assignments-lesson-from-33-to-37/

# -1
print(bool(100)) # int
print(bool(100.5)) # float
print(bool("string")) # string
print(bool(True)) # self

print(bool(())) # empty tuple
print(bool([])) # empty list
print(bool({})) # empty dict
print(bool(False)) # self
print(bool(0)) # zero value

print("=" * 100)

# -2
html = 80
css = 60
javascript = 70

print(html > 50 and css > 50 and javascript > 50)

print("=" * 100)

# -3
num_one = 10
num_two = 20
num = 20

print(num > num_one or num > num_two)

print(num > num_one and num > num_two)

print("=" * 100)

# -4
num_1 = 10
num_2 = 20

result = num_1 + num_2

print(result)

result **= 3
print(result)

result %= 26000
print(result)

result /= 5
print(float(result))

result = str(result)
print(type(result))



