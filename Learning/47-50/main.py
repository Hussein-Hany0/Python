# All Assignments are in : https://elzero.org/python-assignments-lesson-from-47-to-50/

# -1
num = int(input("Enter a number : ").strip())

if num < 0 : 
    print("Number 0 Is Not Larger Than 0")

while num > 0 : 
    if num != 6 :
        print(num)

    num -= 1

    if num == 0 : 
        print("8 Numbers Printed Successfully.")

print("=" * 100)

# -2
friends = ["Mohamed", "Shady", "ahmed", "eman", "Sherif"]

i = 0

ignoredNames = 0

while i < len(friends) : 
    if friends[i] != friends[i].lower() :
        print(f"\"{friends[i]}\"")
    else :
        ignoredNames += 1

    i += 1
else :
    print(f"Friends Printed And Ignored Names Count Is {ignoredNames}")

print("=" * 100)

# -3
skills = ["HTML", "CSS", "JavaScript", "PHP", "Python"]

while skills:
    print(skills.pop(0))

# -4
my_friends = []

max_friends = 4

while max_friends > 0 :

    name = input("Enter Your Friend Name : ").strip()

    if name == name.upper() : 
        print("Invalid Nmae")
    
    else : 

        max_friends -= 1 # To ignore putting this line in if and else scope

        if name != name.capitalize() : 
            print(f"Friend {name} Added => 1st Letter Become Capital")
            my_friends.append(name.capitalize())
            print(f"Names Left in List Is {max_friends}")

        else :
            print(f"Friend {name} Added") 
            my_friends.append(name.capitalize())
            print(f"Names Left in List Is {max_friends}")