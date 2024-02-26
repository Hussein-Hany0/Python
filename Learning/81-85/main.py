# All Assignments are in : https://elzero.org/python-assignments-lesson-from-81-to-85/

# -1
def reverse_string(my_string):
  index = len(my_string) - 1

  while index >= 0 :
    yield my_string[index]
    index -= 1

# Reverse The String
for c in reverse_string("Elzero"):
  print(c)


# -2
def myDecorator(func) :
  def msg_and_sep() : # message and seprator
    print("Sugar Added From Decorators")
    func()
    print("#" * 20)

  return msg_and_sep

@myDecorator
def make_tea():
  print("Tea Created")

@myDecorator
def make_coffe():
  print("Coffe Created")

make_tea()
make_coffe()