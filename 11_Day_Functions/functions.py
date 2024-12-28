def add_two_numbers(num1,num2):
    sum = num1+num2
    return sum
print(add_two_numbers(2,3))

import math
def area_of_a_circle(r):
    circle = math.pi *r*r
    return circle
print(area_of_a_circle(1))

def add_all_nums(*args):
    total = 0
    for num in args:
        if not isinstance(num, (int, float)):  # Check if the argument is a number
            return "All arguments must be numbers!"
        total += num
    return total

print(add_all_nums(2, 3, 4, 5))  # Valid input
print(add_all_nums(2, '3', 4, 5))  # Invalid input (string in arguments)
print(type(add_all_nums()))  # Type of the returned result

def convert_celsius_to_fahrenheit(C):
    F = (C*9/5)+32
    return F
print(convert_celsius_to_fahrenheit(1))

def check_season(month):
    month = month.capitalize()
    Autumn = ["September", "October", "November"]
    Winter = ["December", "January", "February"]
    Spring = ["March", "April", "May"]
    Summer = ["June", "July", "August"]
    if month in Autumn:
        return "Autumn"
    elif month in Spring:
        return "Spring"
    elif month in Winter:
        return "Winter"
    elif month in Summer:
        return "Summer"
    else:
        return "Invalid Month"
print(check_season("march"))
