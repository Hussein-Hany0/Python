# all assignments are in : https://elzero.org/python-assignments-lesson-from-11-to-18/

# -1
name = "hussein"
age = 21
country = "egypt"

print("Hello '%s', How You Doing \\\"\"\" Your age is \"%d\" + And your country is: %s" %(name , age , country))

# -2
print("Hello '%s', How You Doing \\\n\"\"\" Your age is \"%d\" + \nAnd your country is: %s" %(name , age , country))

# -3
fname = "elzero"
print(f"second letter is : {fname[1]}")
print(f"Third letter is : {fname[2]}")
print(f"last letter is : {fname[-1]}")

# -4
print(fname[1:4])
print(fname[0].upper() + fname[2] + fname[-2])
print(fname[-2] + fname[2] + fname[0].upper())

# -5
specialName = "#@#@Elzero#@#@"
print(specialName.strip("#@"))

# -6
num = "9"
print(num.zfill(4))

# -7
nameOne = "osama"
print(nameOne.rjust(20 , "@"))

# -8
name_one = "OSaMa"

print(name_one.swapcase())

# -9
msg = "I Love Python And Although Love Elzero Web School"

print(msg.count("Love"))

# -10
print(fname.index("z")) # fname declared above with value of "elzero"

# -11
newMsg = "I <3 Python And Although <3 Elzero Web School"
print(newMsg.replace("<3" , "Love" , 1))

# -12
print(newMsg.replace("<3" , "Love"))

# -13
print(f"My Name is {name}, And My Age Is {age}, And My Country is {country}")