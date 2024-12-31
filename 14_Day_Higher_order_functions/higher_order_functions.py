countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for country in countries:
    print(country)
for name in names:
    print(name)
for number in numbers:
    print(number)


countries =['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
countries_uppercase = list(map(lambda country: country.upper(), countries))

print(countries_uppercase)


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
square_numbers = list(map(lambda x: x*x,numbers))
print(square_numbers)


names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
upper_names = list(map(lambda name: name.upper(),names))
print(upper_names)


countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
def country(name):
    if "land" in name:
        return True
    return False

names = filter(country,countries)
print(list(names))


countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
def country(name):
    if len(name) == 6:
        return True
    return False

names = filter(country,countries)
print(list(names))


countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']

filtered_countries = filter(lambda name: len(name) >= 6, countries)
print(list(filtered_countries))


countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
def country(name):
    if name.startswith('E'):
        return True
    return False

names = filter(country,countries)
print(list(names))


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Filter: Keep only even numbers
even_numbers = filter(lambda num: num % 2 == 0, numbers)

# Map: Square each number
squared_numbers = map(lambda num: num**2, even_numbers)

# Reduce: Sum up all the squared numbers
sum_of_squares = reduce(lambda x, y: x + y, squared_numbers)

# Print intermediate results and final result
print("Filtered (Even Numbers):", list(filter(lambda num: num % 2 == 0, numbers)))
print("Mapped (Squares):", list(map(lambda num: num**2, filter(lambda num: num % 2 == 0, numbers))))
print("Reduced (Sum of Squares):", sum_of_squares)

