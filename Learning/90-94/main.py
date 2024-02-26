# All Assignments are in : https://elzero.org/python-assignments-lesson-from-90-to-94/

#-1
NUM = input("Add Your Number ")

try :

  if not int(NUM) and int(NUM) != 0:
    raise ValueError

  if len(NUM) > 1:
    raise IndexError
    
  elif int(NUM) == 0 :
    raise Exception

except ValueError:
  print("Exception: Only Numbers Allowed")

except IndexError: 
  print("IndexError: Only One Character Allowed")

except :
  print("EXception: Number Must Be Larger Than 0")

else : 
  print(f"The number is {NUM}") 


# -2
LETTER = input("Add Letter From A to Z : ")
try :

  if LETTER.lower() == LETTER:
    raise ValueError

  if len(LETTER) > 1:
    raise IndexError

except ValueError:
  print("The Letter Not In A - Z")

except IndexError: 
  print("You Must Write One Character Only")

else : 
  print(f"You Typed {LETTER}")

# -3
def calculate(num1, num2) -> tuple[int , int]: # put them in tuple 
  return num1 + num2

print(calculate(20, 30))