"""
  This module is used only for solving assignments of elzero python course 
  from vid 86 till vid 89
"""

# All Assignments are in : https://elzero.org/python-assignments-lesson-from-86-to-89/

# -1
my_list = ["E", "Z", "R", 1, 2, 3]
my_tuple = ("L", "E", "O")
my_data = []

final_string = ""

for data in zip(my_list, my_tuple):
  final_string += data[0]
  final_string += data[1]

print(final_string) # Elzero

# -2
my_list1 = ["E", "L", "Z", "E", "R", "O", 1, 2]
my_tuple = ("E", "Z", "R", 1, 2, "E", "R", "O")
my_list2 = ("L", "E", "O", 1, 2, "E", "R", "O")
my_data = []

final_string = ""

for item1, item2, item3 in zip(my_list1, my_tuple, my_list2):
  if type(item1) == str :
    final_string += item1

print(final_string)

# -3
from PIL import Image

myImage = Image.open("D:\Python\86-89\elzero-pillow.png")

myOffset = (400 , 0 , 800 , 400)

croppedImage = myImage.crop(myOffset)

croppedImage.convert("L").show()

halfImage = myImage.crop((0 , 400 , 1200 , 800))

halfImage.rotate(180).convert("L").show()

# -4
def say_hello_to(name):
  """
  "parameter(someone) => Person Name"
  "Function To Say Hello To Anyone"
  """
  print(f"Hello {name}")

print(say_hello_to("Osama")) # "Hello Osama"

print(say_hello_to.__doc__)
print(help(say_hello_to))

# -5
myFriends = ["Ahmed", "Osama", "Sayed"]

def say_hello(some_peoples) -> list:
    ''' This function iterate over the list and return each name with hello message'''
    for some_one in some_peoples:
        print(f"Hello {some_one}")

say_hello(myFriends)
