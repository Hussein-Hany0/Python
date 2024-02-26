# All Assignments are in : https://elzero.org/python-assignments-lesson-from-21-to-23/

# -1
friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]

print(friends[0]) # positive index => zero-based
print(friends[-5]) # negative index => -1-based
print(friends[4])
print(friends[-1])

# -2
print(friends[0::2]) # even items
print(friends[1::2]) # odd items

# -3
print(friends[1:4])
print(friends[-2:])

# -4
friends[3:5] = ["Elzero" , "Elzero"]
print(friends)
#-5
friends.append("salem") # ['Osama', 'Ahmed', 'Sayed', 'Elzero', 'Elzero', 'salem']

friends.insert(0 , "nasser") # ['nasser', 'Osama', 'Ahmed', 'Sayed', 'Elzero', 'Elzero', 'salem']

# -6
friends.pop(0) # ["Osama" ,"Ahmed", "Sayed", "Salem"]
friends.pop(0) # ["Ahmed", "Sayed", "Salem"]
friends.pop() # ["Ahmed", "Sayed"]
print(friends)

# -7
employees = ["Samah", "Eman"]
school = ["Ramy", "Shady"]

friends.extend(employees)
friends.extend(school)

print(friends)

# -8
friends.sort(reverse=False) # can't perform sort in print function because sort is in-place 
print(friends)
friends.sort(reverse=True)
print(friends)

# -9
lenght = len(friends)
print(lenght)

# -10
technologies = ["Html", "CSS", "JS", "Python", ["Django", "Flask", "Web"]]

print(technologies[-1][0])
print(technologies[-1][-1])