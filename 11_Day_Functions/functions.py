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
