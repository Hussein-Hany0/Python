# All Assignments are in : https://elzero.org/python-assignments-lesson-from-51-to-55/

# -1 
my_nums = [15, 81, 5, 17, 20, 21, 13]

my_nums.sort(reverse=True)

mark = 1

for number in my_nums :
    if number % 5 == 0 : 
        print(f"#{mark} => {number}")
        mark += 1

else : 
    print("All Numbers Printed")

# -2
myRange = range(1,21)

ignoredNumbers = [6 , 8 , 12]

for number in myRange : 
    if number not in ignoredNumbers :
        print(str(number).zfill(2))

else : 
    print("All Numbers Are Printed")


# -3
my_ranks = {
    'Math': 'A',
    "Science": 'B',
    'Drawing': 'A',
    'Sports': 'C'
}

totalRanks = 0

for subject in my_ranks :

    if my_ranks[subject] == 'A' :
        print(f"My Rank in {subject} Is {my_ranks[subject]} And This Equal 100 Points")
        totalRanks += 100

    elif my_ranks[subject] == 'B' :
        print(f"My Rank in {subject} Is {my_ranks[subject]} And This Equal 80 Points")
        totalRanks += 80

    elif my_ranks[subject] == 'C' :
        print(f"My Rank in {subject} Is {my_ranks[subject]} And This Equal 40 Points")
        totalRanks += 40


else :
    print(f"Total Ranks = {totalRanks}")

# -4
students = {
    "Ahmed": {
        "Math": "A",
        "Science": "D",
        "Draw": "B",
        "Sports": "C",
        "Thinking": "A"
    },
    "Sayed": {
        "Math": "B",
        "Science": "B",
        "Draw": "B",
        "Sports": "D",
        "Thinking": "A"
    },
    "Mahmoud": {
        "Math": "D",
        "Science": "A",
        "Draw": "A",
        "Sports": "B",
        "Thinking": "B"
    }
}

for name in students :

    print("\"" + "-" * 30 + "\"")

    print(f"\"-- Student Name => {name}\"")

    print("\"" + "-" * 30 + "\"")

    totalRank = 0

    for subject in students[name] :
        if students[name][subject] == 'A' :
            print(f"\"- {subject} => 100 Points\"")
            totalRank += 100

        elif students[name][subject] == 'B' :
            print(f"\"- {subject} => 80 Points\"")
            totalRank += 80

        elif students[name][subject] == 'C' :
            print(f"\"- {subject} => 40 Points\"")
            totalRank += 40

        elif students[name][subject] == 'D' :
            print(f"\"- {subject} => 20 Points\"")
            totalRank += 20
        
    print(f"\"Total Points For {name} Is {totalRank}")

    totalRank = 0
