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

def calculate_slope(x1, y1, x2, y2):
    # Ensure we don't divide by zero
    if x2 - x1 == 0:
        return "Undefined (vertical line)"
    return (y2 - y1) / (x2 - x1)

# Example usage
print(calculate_slope(1, 2, 3, 6)) 
print(calculate_slope(4, 5, 4, 10))

import math

def solve_quadratic_eqn(a, b, c):
    d = b**2 - 4*a*c  # Calculate the discriminant
    if d < 0:
        return "No real roots"
    elif d == 0:
        # One root (double root)
        root = -b / (2 * a)
        return (root,)
    else:
        # Two roots
        root1 = (-b + math.sqrt(d)) / (2 * a)
        root2 = (-b - math.sqrt(d)) / (2 * a)
        return (root1, root2)

# Example usage
print(solve_quadratic_eqn(1, -3, 2))  # Two roots
print(solve_quadratic_eqn(1, 2, 1))   # One root
print(solve_quadratic_eqn(1, 1, 1))   # No real roots


def reverse_list(arr):
    reversed_arr = []
    for i in range(len(arr) - 1, -1, -1):  # Iterate from the last index to the first
        reversed_arr.append(arr[i])
    return reversed_arr

print(reverse_list([1, 2, 3, 4, 5]))  # Example usage


def capitalize_list_items(arr):
    return_arr = []
    for item in arr:
        return_arr.append(item.capitalize())  # Capitalize each string and append it to the new list
    return return_arr

print(capitalize_list_items(["apple", "cat"]))


def add_item(lst, item):
    lst.append(item)  # Add the item to the end of the list
    return lst

# Example usage
food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(add_item(food_staff, 'Meat'))  # ['Potato', 'Tomato', 'Mango', 'Milk', 'Meat']

numbers = [2, 3, 7, 9]
print(add_item(numbers, 5))  # [2, 3, 7, 9, 5]


def remove_item(lst,item):
    if item in lst:
        lst.remove(item)
    else:
        return f" '{item}' not found in the list"
    return lst

food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(remove_item(food_staff, 'Mango')) 

numbers = [2, 3, 7, 9]
print(remove_item(numbers, 3))


def sum_of_numbers(num):
    count = 0
    for i in range(1,num+1):
        count = count+i
    return count
print(sum_of_numbers(5))
print(sum_of_numbers(10))
print(sum_of_numbers(100))

def sum_of_odds(num):
    count = 0
    for i in range(1, num + 1):  # Iterate through all numbers from 1 to num
        if i % 2 != 0:  # Check if the number is odd
            count += i  # Add the odd number to the count
    return count

print(sum_of_odds(10))  # Example usage
def sum_of_odds(num):
    count = 0
    for i in range(1,num+1,2):
        count = count+i
    return count

print(sum_of_odds(10))


def sum_of_even(num):
    count = 0
    for i in range(1,num+1):
        if i%2 == 0:
            count +=i
    return count
print(sum_of_even(10))
