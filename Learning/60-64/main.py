# All Assignments are in : https://elzero.org/python-assignments-lesson-from-60-to-64/

# -1 

def get_score(**subjects) :

  for subject_key , subject_value in subjects.items() :

    print(f"--{subject_key} => {subject_value}")

get_score(Math=90, Science=80, Language=70)


# -2
def get_people_scores(name = "" , **skills) :
  
  if name == "" and skills != {}: # skills is dict , {} is an empty dict
    
    for skill_key , skill_value in skills.items() :
      print(f"--{skill_key} => {skill_value}")

  elif name != "" and skills == {}:
    print(f"Hello {name} You Have No Scores To Show")

  else :
    print(f"Hello {name} This Is Your Score Table:")

    for skill_key , skill_value in skills.items() :
      print(f"--{skill_key} => {skill_value}")


get_people_scores("Ahmed")
get_people_scores(Logic=70, Problems=60)
get_people_scores("Mahmoud", Logic=70, Problems=60)
get_people_scores("Osama", Math=90, Science=80, Language=70)


# -3
def get_the_scores(name = "", **skills) :
  
    if name == "" and skills != {}: # skills is dict , {} is an empty dict
      for skill_key , skill_value in skills.items() :
        print(f"--{skill_key} => {skill_value}")

    elif name != "" and skills == {}:
      print(f"Hello {name} You Have No Scores To Show")

    else :
      print(f"Hello {name} This Is Your Score Table:")
      for skill_key , skill_value in skills.items() :
        print(f"--{skill_key} => {skill_value}")



scores_list = {
  "Math" : 90,
  "Science" : 80,
  "Language" : 70
}


get_the_scores("Osama", **scores_list)
get_the_scores("Osama")
get_the_scores(**scores_list)