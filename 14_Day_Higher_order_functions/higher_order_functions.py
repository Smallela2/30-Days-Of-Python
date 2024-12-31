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


def get_string_lists(input_list):
    return list(filter(lambda item: isinstance(item, str), input_list))

mixed_list = [1, 'hello', 3.14, 'world', True, 'Python']
string_list = get_string_lists(mixed_list)
print(string_list)


from functools import reduce
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sum_numbers = reduce(lambda x, y: x + y, numbers)
print(sum_numbers)


from functools import reduce
from collections import Counter

# 1. Use reduce to concatenate all the countries into a sentence
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
sentence = reduce(
    lambda x, y: f"{x}, {y}" if y != 'Iceland' else f"{x}, and {y}",
    countries
) + " are north European countries."
print(sentence)

# 2. Declare categorize_countries
def categorize_countries(pattern):
    """
    Returns a list of countries with a common pattern.
    """
    return [country for country in countries if pattern in country]

print(categorize_countries('land'))  # ['Finland', 'Iceland']

# 3. Return a dictionary of countries grouped by starting letter
def count_countries_by_letter(countries):
    """
    Creates a dictionary where keys are starting letters and values are counts.
    """
    country_dict = {}
    for country in countries:
        first_letter = country[0].upper()
        country_dict[first_letter] = country_dict.get(first_letter, 0) + 1
    return country_dict

print(count_countries_by_letter(countries))

# 4. Declare get_first_ten_countries
def get_first_ten_countries(countries):
    """
    Returns the first ten countries from the list.
    """
    return countries[:10]

print(get_first_ten_countries(countries))

# 5. Declare get_last_ten_countries
def get_last_ten_countries(countries):
    """
    Returns the last ten countries from the list.
    """
    return countries[-10:]

print(get_last_ten_countries(countries))

# 6. Sort countries by name, capital, population
# Assuming you have imported countries_data.py
from countries_data import countries_data

# Sort by name
sorted_by_name = sorted(countries_data, key=lambda x: x['name'])
# Sort by capital
sorted_by_capital = sorted(countries_data, key=lambda x: x['capital'])
# Sort by population
sorted_by_population = sorted(countries_data, key=lambda x: x['population'], reverse=True)

print("Sorted by name:", [country['name'] for country in sorted_by_name[:5]])
print("Sorted by capital:", [country['capital'] for country in sorted_by_capital[:5]])
print("Sorted by population:", [country['name'] for country in sorted_by_population[:5]])

# 7. Sort out the ten most spoken languages
def most_spoken_languages(countries_data, top_n=10):
    languages = []
    for country in countries_data:
        languages.extend(country['languages'])
    language_counts = Counter(languages)
    return language_counts.most_common(top_n)

print(most_spoken_languages(countries_data))

# 8. Sort out the ten most populated countries
def most_populated_countries(countries_data, top_n=10):
    return sorted(countries_data, key=lambda x: x['population'], reverse=True)[:top_n]

print(most_populated_countries(countries_data))
