numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
lst = [i for i in numbers if i<=0]
print(lst)


list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
flatten_list = [number for row in list_of_lists  for number in row]
lst = [number for row in flatten_list  for number in row]
print(lst)


lst = [(i,1,i,i*i,i*i*i,i*i*i*i,i*i*i*i*i) for i in range(0,11)]
print(lst)


countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

# Flatten and transform the data
result = [
    [country.upper(), country[:3].upper(), capital.upper()]
    for sublist in countries
    for country, capital in sublist
]

print(result)


countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]


result = [
    {'country': country.upper(), 'city': city.upper()}
    for sublist in countries
    for country, city in sublist
]

print(result)


result = [
    f"{first} {last}" 
    for sublist in names 
    for first, last in sublist
]

print(result)


# Lambda to calculate slope
slope = lambda x1, y1, x2, y2: (y2 - y1) / (x2 - x1) if x2 != x1 else 'Undefined (vertical line)'

# Lambda to calculate y-intercept
y_intercept = lambda x1, y1, m: y1 - m * x1

# Example usage
x1, y1 = 1, 2
x2, y2 = 3, 6

m = slope(x1, y1, x2, y2)  # Calculate slope
c = y_intercept(x1, y1, m) if isinstance(m, (int, float)) else 'N/A'  # Calculate y-intercept if slope is defined

print(f"Slope: {m}")
print(f"Y-Intercept: {c}")

