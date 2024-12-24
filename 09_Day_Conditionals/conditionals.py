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



