

#### **What is a Dictionary?**
A dictionary is an unordered collection of items. Each item consists of a key and a value, where keys are unique and immutable (e.g., strings, numbers, tuples), and values can be of any data type.

**Example**:
```python
# Creating a dictionary
my_dict = {"name": "Alice", "age": 25, "city": "New York"}
print(my_dict)  # Output: {'name': 'Alice', 'age': 25, 'city': 'New York'}
```

---

#### **Accessing Values Using Keys**
Use square brackets `[]` or the `get()` method.

**Example**:
```python
print(my_dict["name"])  # Output: Alice
print(my_dict.get("age"))  # Output: 25
```

---

#### **Adding and Updating Items**
Add a new key-value pair or update an existing key.

**Example**:
```python
my_dict["age"] = 30  # Update
my_dict["job"] = "Engineer"  # Add
print(my_dict)  # Output: {'name': 'Alice', 'age': 30, 'city': 'New York', 'job': 'Engineer'}
```

---

#### **Removing Items**
- `pop(key)`: Removes an item by key.
- `popitem()`: Removes the last inserted item (Python 3.7+).
- `del`: Deletes a key or the entire dictionary.

**Example**:
```python
my_dict.pop("city")
print(my_dict)  # Output: {'name': 'Alice', 'age': 30, 'job': 'Engineer'}

my_dict.popitem()
print(my_dict)  # Output: {'name': 'Alice', 'age': 30}

del my_dict["age"]
print(my_dict)  # Output: {'name': 'Alice'}
```

---

#### **Empty a Dictionary**
Use `clear()` to remove all items.

**Example**:
```python
my_dict.clear()
print(my_dict)  # Output: {}
```

---

### **2. Dictionary Methods**

#### **Common Methods**
- `get()`: Retrieve a value with a default if the key doesn’t exist.
- `keys()`: Returns all keys as a view object.
- `values()`: Returns all values as a view object.
- `items()`: Returns all key-value pairs as tuples in a view object.

**Example**:
```python
my_dict = {"name": "Alice", "age": 30, "job": "Engineer"}
print(my_dict.keys())  # Output: dict_keys(['name', 'age', 'job'])
print(my_dict.values())  # Output: dict_values(['Alice', 30, 'Engineer'])
print(my_dict.items())  # Output: dict_items([('name', 'Alice'), ('age', 30), ('job', 'Engineer')])
```

---

#### **setdefault()**
Adds a key with a default value if the key doesn’t exist.

**Example**:
```python
my_dict.setdefault("salary", 50000)
print(my_dict)  # Output: {'name': 'Alice', 'age': 30, 'job': 'Engineer', 'salary': 50000}
```

---

#### **update()**
Merges another dictionary or key-value pairs.

**Example**:
```python
my_dict.update({"city": "New York", "age": 35})
print(my_dict)  # Output: {'name': 'Alice', 'age': 35, 'job': 'Engineer', 'salary': 50000, 'city': 'New York'}
```

---

### **3. Iterating Over Dictionaries**

#### **Keys, Values, and Items**
**Example**:
```python
for key in my_dict:
    print(key)  # Output: name, age, job, salary, city

for value in my_dict.values():
    print(value)  # Output: Alice, 35, Engineer, 50000, New York

for key, value in my_dict.items():
    print(f"{key}: {value}")
# Output:
# name: Alice
# age: 35
# job: Engineer
# salary: 50000
# city: New York
```

---

### **4. Dictionary Comprehensions**

#### **Creating Dictionaries with Conditions**
**Example**:
```python
squares = {x: x**2 for x in range(1, 6)}
print(squares)  # Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
```

---

### **5. Nested Dictionaries**

#### **Creating and Accessing Nested Dictionaries**
**Example**:
```python
nested_dict = {
    "student1": {"name": "Alice", "age": 20},
    "student2": {"name": "Bob", "age": 22}
}

print(nested_dict["student1"]["name"])  # Output: Alice
```

---

### **6. Dictionary Sorting**

#### **Sorting by Keys**
**Example**:
```python
sorted_by_keys = dict(sorted(my_dict.items()))
print(sorted_by_keys)
# Output: {'age': 35, 'city': 'New York', 'job': 'Engineer', 'name': 'Alice', 'salary': 50000}
```

#### **Sorting by Values**
**Example**:
```python
sorted_by_values = dict(sorted(my_dict.items(), key=lambda x: x[1]))
print(sorted_by_values)
# Output: {'name': 'Alice', 'job': 'Engineer', 'city': 'New York', 'age': 35, 'salary': 50000}
```

---

### **7. Specialized Dictionaries**

#### **`defaultdict`**
Provides default values for missing keys.

**Example**:
```python
from collections import defaultdict

dd = defaultdict(int)
dd["a"] += 1
print(dd)  # Output: defaultdict(<class 'int'>, {'a': 1})
```

---

#### **`Counter`**
Counts occurrences of items.

**Example**:
```python
from collections import Counter

counter = Counter(["apple", "banana", "apple", "orange", "banana", "apple"])
print(counter)  # Output: Counter({'apple': 3, 'banana': 2, 'orange': 1})
```

---

#### **Immutable Dictionary**
Use `MappingProxyType` to create a read-only dictionary.

**Example**:
```python
from types import MappingProxyType

immutable_dict = MappingProxyType(my_dict)
print(immutable_dict["name"])  # Output: Alice
# immutable_dict["name"] = "Bob"  # Raises TypeError
```

---

### **8. Merging Dictionaries**

#### **Using `|` Operator (Python 3.9+)**
**Example**:
```python
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}

merged = dict1 | dict2
print(merged)  # Output: {'a': 1, 'b': 3, 'c': 4}
```

---

### **9. Use Cases**

#### **Word Frequency Counter**
**Example**:
```python
text = "apple banana apple orange banana apple"
word_count = {}
for word in text.split():
    word_count[word] = word_count.get(word, 0) + 1

print(word_count)  # Output: {'apple': 3, 'banana': 2, 'orange': 1}
```

#### **Dictionary as a Lookup Table**
**Example**:
```python
lookup = {1: "One", 2: "Two", 3: "Three"}
print(lookup[2])  # Output: Two
```

---

### **10. Conversion Between Dictionaries and Other Data Types**

#### **Dictionary to List of Tuples**
**Example**:
```python
tuple_list = list(my_dict.items())
print(tuple_list)  # Output: [('name', 'Alice'), ('age', 35), ('job', 'Engineer'), ('salary', 50000), ('city', 'New York')]
```

#### **List of Tuples to Dictionary**
**Example**:
```python
new_dict = dict(tuple_list)
print(new_dict)
```

---

### **11. Handling Missing Keys**

#### **Using `get()`**
**Example**:
```python
print(my_dict.get("unknown", "Default Value"))  # Output: Default Value
```

