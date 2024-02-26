# All Assignments are in : https://elzero.org/python-assignments-lesson-from-38-to-40/

# -1
name = input("Enter your name : ").strip().capitalize()

print(f"Hello {name}, Happy To See You Here.")

print("=" * 100)

# -2
age = int(input("Enter Your Age : "))

if age < 16 : 
    print("Hello Your Age Is Under 16, Some Articles Is Not Suitable For You")
else : 
    print(f"Hello Your Age Is {age}, All Articles Is Suitable For You")

print("=" * 100)

# -3
first_name = input("Enter your first name : ").strip().capitalize()
second_name = input("Enter your second name : ").strip().capitalize()

print(f"Hello {first_name} {second_name:.1}.")

print("=" * 100)

# -4
email = input("Enter your Email : ").strip().lower()

print(f"Your Name is {email[:email.index('@')]}")

print(f"Email service Provider is {email[email.index('@') + 1 : email.index('.')]}")

print(f"Email service Provider is {email[email.index('.') + 1 :]}")


