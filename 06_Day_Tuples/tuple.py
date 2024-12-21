# Create empty tuple
tpl = ()
print("Empty tuple:", tpl)

# Create tuples for sisters and brothers
sis = ('Sravani', 'Swathi')
bro = ('Nani', 'Manoj')
print("Sisters:", sis)
print("Brothers:", bro)

# Join tuples to form siblings
siblings = sis + bro
print("Siblings:", siblings)

# Count siblings
print("Number of siblings:", len(siblings))

# Add parents to form family_members
parents = ('Srinivas', 'Varalakshmi')
family_members = parents + siblings
print("Family members:", family_members)
-------------------------------------------

fruits = ('banana', 'apple', 'orange')
vegetables = ('carrot', 'ladiesfinger', 'beetroot')
animals = ('wheat', 'grass')

# Print tuples
print(fruits)
print(vegetables)
print(animals)

# Join tuples and convert to list
food_stuff_tp = fruits + vegetables + animals
print(food_stuff_tp)
food_stuff_lt = list(food_stuff_tp)
print(food_stuff_lt)

# Slice out the middle item(s)
length = len(food_stuff_lt)
if length % 2 == 0:
    middle_items = food_stuff_lt[length//2 - 1:length//2 + 1]
else:
    middle_items = [food_stuff_lt[length//2]]
print(middle_items)

# Slice out first 3 and last 3 items
first_3 = food_stuff_lt[0:3]
last_3 = food_stuff_lt[-3:]
print(first_3)
print(last_3)

# Delete the tuple
del food_stuff_tp
---------------------------------------------

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print(nordic_countries)
print("Estonia" in nordic_countries)
print('Iceland' in nordic_countries)
