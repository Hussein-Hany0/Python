# All Assignments are in : https://elzero.org/python-assignments-lesson-from-26-to-32/

# -1 
my_list = [1, 2, 3, 3, 4, 5, 1]

unique_list = list(set(my_list))

print(unique_list)

print(type(unique_list))

print(unique_list[0:4])


# -2
nums = {1, 2, 3}
letters = {"A", "B", "C"}

fCompo = nums.union(letters)
sCompo = nums | letters
nums.update(letters)
thCompo = nums

print(fCompo)
print(sCompo)
print(thCompo)

# -3
my_set = {1, 2, 3}
letters = {"A", "B", "C"}

print(my_set)
my_set.clear()
print(my_set)

my_set.add("A")
my_set.add("B")
print(my_set)

my_set.discard("C") # in case of remove : this will throw an error

# -4
set_one = {1, 2, 3}
set_two = {1, 2, 3, 4, 5, 6}

print(set_one.issubset(set_two))

# -5
skills = {
    "One" : {
        "Name" : "HTML",
        "Progress" : "80%"
    },
    "Two" : {
        "Name" : "CSS",
        "Progress" : "80%"
    },
    "Three" : {
        "Name" : "Python",
        "Progress" : "30%"
    }
}

print(f"{skills['One']['Name']} Progress is {skills['One']['Progress']}")
print(f"{skills['Two']['Name']} Progress is {skills['Two']['Progress']}")
print(f"{skills['Three']['Name']} Progress is {skills['Three']['Progress']}")

skills.update({"Four" : {"Name" : "AI" , "Progress" : "20%"}})

print(f"{skills['Four']['Name']} Progress is {skills['Four']['Progress']}")