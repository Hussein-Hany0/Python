# # All Assignments are in : https://elzero.org/python-assignments-lesson-from-69-to-71/

# # -1

# values = (0, 1, 2)

# if any(values):

#   my_var = 0 # 1 will be zero and 2 will be zero : (0 , 0 , 0)

# my_list = [True, 1,  1, ["A", "B"], 10.5, my_var]

# if all(my_list[:4]) or all(my_list[:6]) or all(my_list[:]):

#   print("Good")

# else:

#   print("Bad")


# # -2
# v = 40

# my_range = list(range(v)) 

# print(sum(my_range, v) + pow(v, v, v))  # 820

# # -3

# n = 20

# l = list(range(n))

# if round(sum(l) / n) == max(0, 3, 10, 2, -100, -23, 9): # max is 10

#   print("Good")

# # Output => Good
  
# -4
def my_all(iterable) : 
  
  index = 0 

  while index < len(iterable) :
    if not iterable[index] :
      return False
    
    elif index == len(iterable) -1 :
      return True
    
    index += 1


def my_any(iterable) : 
  
  index = 0 

  while index < len(iterable) :
    if iterable[index] :
      return True
    
    elif index == len(iterable) - 1 :
      return False 
    
    index += 1
    

def my_min(iterable) :

  min = iterable[0]

  for i in iterable :
    if i < min :
      min = i

  return min

def my_max(iterable) :

  max = iterable[0]

  for i in iterable :
    if i > max :
      max = i

  return max

# my_all
print(my_all([1, 2, 3])) # True
print(my_all([1, 2, 3, []])) # False

# my_any
print(my_any([0, 1, [], False])) # True
print(my_any([(), 0, False])) # False


# my_min
print(my_min([10, 100, -20, -100, 50])) # -100
print(my_min((10, 100, -20, -100, 50))) # -100

# my_max
print(my_max([10, 100, -20, -100, 50, 700])) # 700
print(my_max((10, 100, -20, -100, 50, 700))) # 700