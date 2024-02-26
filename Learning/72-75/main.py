# # All Assignments are in : https://elzero.org/python-assignments-lesson-from-72-to-75/

# # -1
# # def remove_chars(text) :
# #   return text[1 : -1]

# friends_map = ["AEmanS", "AAhmedS", "DSamehF", "LOsamaL"]

# # cleaned_list = map(remove_chars , friends_map)

# cleaned_list = map(lambda text : text[1: -1] , friends_map)

# for item in cleaned_list :
#   print(item)


# # -2
# # def ends_with_m(text) :
# #   return text[-1] == "m"

# friends_filter = ["Osama", "Wessam", "Amal", "Essam", "Gamal", "Othman"]

# # names = filter(ends_with_m , friends_filter)

# names = filter(lambda text : text[-1] == "m" , friends_filter)

# for name in names : 
#   print(name)


# # -3

# from functools import reduce

# # def multiply_all(x1 , x2) :
# #   return x1 * x2

# nums = [2, 4, 6, 2]

# # total = reduce(multiply_all , nums)

# total = reduce(lambda x1, x2 : x1 * x2 , nums)

# print(total)


# -4
# def is_str_type(text) :
#   return type(text) == str

# skills = ("HTML", "CSS", 10, "PHP", "Python", 20, "JavaScript")

# enumeratedSkills = enumerate(skills , 50)

# for key , value in enumeratedSkills :
#   if type(value) == str :
#     print(f"{key} - {value}")

def is_str_type(pair) :
  return type(pair[1]) == str

skills = ("HTML", "CSS", 10, "PHP", "Python", 20, "JavaScript")

enumeratedSkills = enumerate(skills , 50)

filteredSkills = filter(is_str_type, tuple(enumeratedSkills))

for key , value in filteredSkills :
  if type(value) == str :
    print(f"{key} - {value}")