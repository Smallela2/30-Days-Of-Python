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


def evens_and_odds(num):
    even = 0
    odd = 0
    for i in range(num+1):
        if i%2 == 0:
            even +=1
        else:
            odd +=1
    return f"The number of odds are {odd}.\nThe number of evens are {even}."    
            

print(evens_and_odds(100))

import math
def fact(num):
    my_factorial = math.factorial(num)
    return my_factorial
print(fact(5))

def is_empty(value):
    return not bool(value)  # Check if the value evaluates to False (empty)

# Example usage
print(is_empty([]))        # True (Empty list)
print(is_empty({}))        # True (Empty dictionary)
print(is_empty(""))        # True (Empty string)

from collections import Counter
import math

def calculate_mean(data):
    return sum(data) / len(data) if data else 0

def calculate_median(data):
    n = len(data)
    if n == 0:
        return 0  # Handle empty list
    data_sorted = sorted(data)
    mid = n // 2
    if n % 2 == 0:
        return (data_sorted[mid - 1] + data_sorted[mid]) / 2  # Even length
    else:
        return data_sorted[mid]  # Odd length

def calculate_mode(data):
    if not data:
        return None  # Handle empty list
    count = Counter(data)
    max_freq = max(count.values())
    modes = [key for key, value in count.items() if value == max_freq]
    return modes if len(modes) > 1 else modes[0]  # Return a list if multiple modes exist

def calculate_range(data):
    if not data:
        return 0  # Handle empty list
    return max(data) - min(data)

def calculate_variance(data):
    if len(data) < 2:
        return 0  # Variance is undefined for lists with less than 2 elements
    mean = calculate_mean(data)
    return sum((x - mean) ** 2 for x in data) / len(data)

def calculate_std(data):
    return math.sqrt(calculate_variance(data))  # Standard deviation is the square root of variance

# Example usage
data = [1, 2, 2, 3, 4, 4, 4, 5]

print("Mean:", calculate_mean(data))
print("Median:", calculate_median(data))
print("Mode:", calculate_mode(data))
print("Range:", calculate_range(data))
print("Variance:", calculate_variance(data))
print("Standard Deviation:", calculate_std(data))

print(is_empty(0))         # True (0 is considered empty in Python)
print(is_empty(None))      # True (None is empty)
print(is_empty([1, 2, 3])) # False (Non-empty list)
print(is_empty("hello"))   # False (Non-empty string)
print(is_empty(42))        # False (Non-zero number)
