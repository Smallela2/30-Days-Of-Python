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
