# 1. Create an empty dictionary called dog
dog = {}
print("Initial dog dictionary:", dog)

# Add name, color, breed, legs, age to the dog dictionary
dog["name"] = "Pinky"
dog["color"] = "White"
dog["breed"] = "Golden Retriever"
dog["legs"] = 4
dog["age"] = 3
print("Updated dog dictionary:", dog)

# 2. Create a student dictionary and add multiple keys
student = {
    "first_name": "John",
    "last_name": "Doe",
    "gender": "Male",
    "age": 21,
    "marital_status": "Single",
    "skills": ["Python", "Java"],
    "country": "USA",
    "city": "New York",
    "address": "123 Main Street"
}
print("Student dictionary:", student)

# Get the length of the student dictionary
student_length = len(student)
print("Length of the student dictionary:", student_length)

# Get the value of skills and check its data type
skills = student["skills"]
print("Skills:", skills)
print("Type of skills:", type(skills))  # It should be a list

# Modify the skills values by adding one or two skills
student["skills"].extend(["C++", "JavaScript"])
print("Updated skills:", student["skills"])

# Get the dictionary keys as a list
keys_list = list(student.keys())
print("Dictionary keys:", keys_list)

# Get the dictionary values as a list
values_list = list(student.values())
print("Dictionary values:", values_list)

# Change the dictionary to a list of tuples using items() method
student_items = list(student.items())
print("Dictionary as a list of tuples:", student_items)

# Delete one of the items in the dictionary
del student["marital_status"]
print("After deleting 'marital_status':", student)

# Delete one of the dictionaries
del dog
print("Dog dictionary deleted")

