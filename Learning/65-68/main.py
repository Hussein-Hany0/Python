# All Assignments are in : https://elzero.org/python-assignments-lesson-from-65-to-68/

#-1

file = open(r"D:\Python\65-68\assign.txt" , 'w')

index = 0

while index < 50 :

  file = open(rf"D:\Python\65-68\txt{index + 1}.txt" , 'w')


  index += 1

index = 0

while index < 50 :

  file = open(rf"D:\Python\65-68\txt{index + 1}.txt" , 'w')

  file.write(f"Elzero Web School => {index + 1}\n")

  index += 1


import os # importing operating system module to have ancillary functions

# os.rename(r"D:\Python\65-68\txt25.txt" , r"D:\Python\65-68\special-text.txt")

special_text = open(r"D:\Python\65-68\special-text.txt" , "w")

special_text.truncate(0)

print(os.getcwd()) # get current working directory

print(os.path.abspath(__file__)) # print the path of this file

print(os.path.dirname(os.path.abspath(__file__))) # print the parent dir of file main.py

# -2
txt1 = open(r"D:\Python\65-68\txt1.txt" , "w") # I will change a to w after one execution to not repeat the insertion

index = 0

while index < 50 :
  txt1.write("Appended => Elzero Web School\n")
  index += 1


# -3
  
def find_I_occurences(line) :

  if line.find("l") != -1 or line.find("L") != -1:
    return 1 + find_I_occurences(line[line.find("l") + 1:])

total_lines = 0
total_words = 0
total_chars = 0
I_occurs = 0

txt1 = open(r"D:\Python\65-68\txt1.txt" , "r") # read state


for line in txt1.readlines() :
  total_chars += len(line)
  total_lines += 1
  total_words += len(line.split())

  if line.find("l") != -1 or line.find("L") != -1:
    I_occurs = find_I_occurences(line)

print(f"Total Lines are {total_lines}")
print(f"Total chars are {total_chars}")
print(f"Total words are {total_words}")
print(f"Total I Occurs are {I_occurs}")