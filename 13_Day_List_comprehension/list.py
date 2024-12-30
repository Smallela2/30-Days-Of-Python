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
