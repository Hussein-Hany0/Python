# All Assignments are in : https://elzero.org/python-assignments-lesson-from-56-to-59/

# -1
def calculate(num1 , num2 , sign = "add") :
  
  if sign.lower() == "add" or sign.lower() == "a" : 
    return num1 + num2
  
  elif sign.lower() == "subtract" or sign.lower() == "s" : 
    return num1 - num2
  
  elif sign.lower() == "multiply" or sign.lower() == "m" : 
    return num1 * num2
  
  else :
    print("No Such Signs Are Available")


print(calculate(10, 20)) # 30
print(calculate(10, 20, "AdD")) # 30
print(calculate(10, 20, "a")) # 30
print(calculate(10, 20, "A")) # 30

print(calculate(10, 20, "S")) # -10
print(calculate(10, 20, "subTRACT")) # -10

print(calculate(10, 20, "Multiply")) # 200
print(calculate(10, 20, "m")) # 200


# -2
def addition(*nums) : 

  total = 0

  for number in nums :

    if number == 10 :
      continue

    elif number == 5 :
      total -= 5

    else :
      total += number

  return total

print(addition(10, 20, 30, 10, 15)) # 65
print(addition(10, 20, 30, 10, 15, 5, 100)) # 160


# -3
def show_skills(name , *skills) :
  if skills == () : # *skills is in tuple form , an empty tuple is ()
    print(f"Hello {name} You Have No Skills")

  else :
    print(f"Hello {name} Your Skills are : ")

    for skill in skills :
      print(f"--{skill}")


show_skills("Osama", "HTML", "CSS", "JS", "Python")


# -4
def say_hello(name = "Unknown", age = "Unknown", country = "Unknown") :
  
  return f"Hello {name}, Your Age is {age} and Your Country is {country}" 

print(say_hello("Osama", 38, "Egypt"))

print(say_hello())