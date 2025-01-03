# level-1
# question-1
age = int(input("Enter your age:"))
if age >= 18:
    print("You are old enough to learn to drive.")
else:
    print(f"You need {18-age} more years to learn to drive.")

# question_2
my_age = 21  # Assume my age is 21
your_age = int(input("Enter your age: "))

if your_age > my_age:
    difference = your_age - my_age
    if difference == 1:
        print("You are 1 year older than me.")
    else:
        print(f"You are {difference} years older than me.")
elif your_age < my_age:
    difference = my_age - your_age
    if difference == 1:
        print("You are 1 year younger than me.")
    else:
        print(f"You are {difference} years younger than me.")
else:
    print("We are the same age!")

# question-3
a = int(input("Enter number one :"))
b = int(input("Enter number two :"))
if a > b:
    print(f"{a} is greater than {b}")
elif a < b:
    print(f"{a} is smaller than {b}")
else:
    print(f"{a} is equal to {b}")

# Level-2
# question-1
score = int(input("Enter a score : "))
if (90 <= score <= 100):
    print("A")
elif (70 <= score <= 89):
    print("B")
elif (60 <= score <= 69):
    print("C")
elif (50 <= score <= 59):
    print("D")
elif (0 <= score <= 49):
    print("F")
else:
    print("invalid score.")

#question-2
month = input("Enter a year : ").strip().capitalize()
if month in ["September", "October", "November"]:
    print("season is Autumn")
elif month in ["December", "January", "February"]:
    print(" season is Winter")
elif month in ["March", "April", "May"]:
    print("season is Spring")
elif month in ["June", "July", "August"]:
    print("season is Summer")
else:
    print("Invalid month")

# question-3
fruits = ['banana', 'orange', 'mango', 'lemon']
fruit = input("Enter a fruit :").strip().lower()
if fruit in fruits:
    print('That fruit already exist in the list')
else:
    fruits.append(fruit)
    print(fruits)


# level -3
# question-1
person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }
if "skills" in person :
    skills = person['skills']
    middle_skill = skills[len(skills) // 2]
    print(f"The middle skill is: {middle_skill}")

if 'skills' in person:
    has_python = 'Python' in person['skills']
    print(f"Has Python skill: {has_python}")

if 'skills' in person:
    skills = person['skills']
    if set(skills) == {'JavaScript', 'React'}:
        print("He is a front end developer")
    elif {'Node', 'Python', 'MongoDB'}.issubset(skills):
        print("He is a backend developer")
    elif {'React', 'Node', 'MongoDB'}.issubset(skills):
        print("He is a fullstack developer")
    else:
        print("unknown title")

if person.get('is_marred') and person.get('country') == 'Finland':
    full_name = f"{person['first_name']} {person['last_name']}"
    print(f"{full_name} lives in Finland. He is married.")

