# All Assignments are in : https://elzero.org/python-assignments-lesson-from-41-to-46/

# -1
num1 = int(input("Enter The first number : ").strip())

num2 = int(input("Enter The second number : ").strip())

operation = input("Enter the type of operation : ").strip()

if operation == "+" : 
    print(f"{num1} {operation} {num2} = {num1 + num2}")
elif operation == "*" : 
    print(f"{num1} {operation} {num2} = {num1 * num2}")
elif operation == "-" : 
    print(f"{num1} {operation} {num2} = {num1 - num2}")
elif operation == "/" : 
    print(f"{num1} {operation} {num2} = {num1 / num2}")
elif operation == "%" : 
    print(f"{num1} {operation} {num2} = {num1 % num2}")
else : 
    print("You've choosed a wrong operator")

# -2
age = 17

print("App Is Suitable For You" if age > 16 else "App Is Not Suitable For You")

# -3
personAge = int(input("Enter The Age : ").strip())

months = personAge * 12
weeks = months * 4
days = personAge * 365
hours = days * 24
seconds = hours * 60

if personAge > 10 and personAge < 100 :
    print(f"You Live For {months} Months")
    print(f"You Live For {weeks} weeks")
    print(f"You Live For {days} days")
    print(f"You Live For {hours} hours")
    print(f"You Live For {seconds} seconds")

else :
    print("Your Age is out of range")

# -4
country = input("Input Your Country : ").strip().capitalize()
countries = ["Egypt", "Palestine", "Syria", "Yemen", "KSA", "USA", "Bahrain", "England"]
price = 100
discount = 30

if country in countries : 
    print(f"Your Country {country} For Discount And The Price After Discount Is $70")
else :
    print("Your Country Not Eligible For Discount And The Price Is $100")
