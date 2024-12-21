## 1. What are Tuples?
Tuples are immutable, ordered collections of elements in Python. Unlike lists, tuples cannot be modified after creation. They are defined using parentheses `()`.

### Example:
```python
my_tuple = (1, 2, 3, 4)
print(my_tuple)  # Output: (1, 2, 3, 4)
```

---

## 2. Tuple Methods
Since tuples are immutable, they have limited methods:

### **`count()`**
- Counts how many times a specific value occurs in a tuple.

```python
t = (1, 2, 2, 3, 4, 2)
print(t.count(2))  # Output: 3
```

### **`index()`**
- Returns the first index of a specific value.

```python
t = (10, 20, 30, 40, 50)
print(t.index(30))  # Output: 2
```

---

## 3. Unpacking Tuples
Unpacking lets you assign tuple elements to variables in one step.

### Example:
```python
person = ("John", 25, "Engineer")

# Unpacking the tuple
name, age, profession = person
print(name)       # Output: John
print(age)        # Output: 25
print(profession) # Output: Engineer
```

### Using `*` to Collect Remaining Items:
```python
numbers = (1, 2, 3, 4, 5)

# Unpacking with *
first, *middle, last = numbers
print(first)   # Output: 1
print(middle)  # Output: [2, 3, 4]
print(last)    # Output: 5
```

---

## 4. Nested Tuples
Tuples can contain other tuples (or lists).

### Example:
```python
nested_tuple = ((1, 2), (3, 4), (5, 6))
print(nested_tuple[1])       # Output: (3, 4)
print(nested_tuple[1][0])    # Output: 3
```

---

## 5. Tuples as Dictionary Keys
Tuples can be used as keys in dictionaries because they are immutable.

### Example:
```python
locations = {
    (40.7128, -74.0060): "New York",
    (34.0522, -118.2437): "Los Angeles"
}
print(locations[(40.7128, -74.0060)])  # Output: New York
```

---

## 6. Returning Multiple Values from Functions
Tuples are often used to return multiple values from a function.

### Example:
```python
def rectangle_properties(length, width):
    area = length * width
    perimeter = 2 * (length + width)
    return area, perimeter

# Using the function
area, perimeter = rectangle_properties(5, 10)
print("Area:", area)         # Output: Area: 50
print("Perimeter:", perimeter)  # Output: Perimeter: 30
```

---

## 7. Immutability of Tuples
Tuples cannot be changed after creation. However, if a tuple contains mutable objects (like lists), the objects inside can be changed.

### Example:
```python
t = (1, 2, [3, 4])
t[2][0] = 100  # Modifying the list inside the tuple
print(t)  # Output: (1, 2, [100, 4])
```

---

## 8. Performance and Use Cases
- **Performance:** Tuples are faster than lists for iteration and access.
- **Use Cases:** Tuples are ideal for fixed collections, such as coordinates, RGB values, or database rows.

---

## Examples and Use Cases

### Example 1: Returning Multiple Values
```python
def calculate_statistics(numbers):
    total = sum(numbers)
    average = total / len(numbers)
    maximum = max(numbers)
    minimum = min(numbers)
    return total, average, maximum, minimum

stats = calculate_statistics([10, 20, 30, 40, 50])
print("Total:", stats[0])    # Output: Total: 150
print("Average:", stats[1])  # Output: Average: 30.0
print("Maximum:", stats[2])  # Output: Maximum: 50
print("Minimum:", stats[3])  # Output: Minimum: 10
```

### Example 2: Tuple Packing and Unpacking
```python
dimensions = (1920, 1080)  # Tuple packing
width, height = dimensions  # Tuple unpacking
print("Width:", width)      # Output: Width: 1920
print("Height:", height)    # Output: Height: 1080
```

---

## Practice Exercises

### Exercise 1: Tuple Manipulation
1. Create a tuple of 5 numbers.
2. Find the sum of all numbers in the tuple.
3. Check if a specific number exists in the tuple.

### Exercise 2: Tuple and List Conversion
1. Convert a tuple into a list.
2. Add a new element to the list.
3. Convert the list back into a tuple.

### Exercise 3: Nested Tuples
1. Create a nested tuple with two levels of data.
2. Access elements from the inner tuple.

### Exercise 4: Sorting a Tuple
Write a program to sort a tuple of integers.

### Exercise 5: Tuple Indexing
1. Create a tuple of 6 strings.
2. Access the first, middle, and last elements.



### **Advanced Tuple Topics**
1. **Tuple Methods:**
   - **`count()`**: Returns the number of occurrences of a specified value in a tuple.
     ```python
     tp = (1, 2, 2, 3, 4, 2)
     print(tp.count(2))  # Output: 3
     ```
   - **`index()`**: Returns the first index of a specified value.
     ```python
     tp = (1, 2, 3, 4, 5)
     print(tp.index(4))  # Output: 3
     ```

---

2. **Unpacking Tuples:**
   - Assigning tuple elements to variables.
     ```python
     tp = (1, 2, 3)
     a, b, c = tp
     print(a, b, c)  # Output: 1 2 3
     ```

   - Using `*` to unpack remaining elements.
     ```python
     tp = (1, 2, 3, 4, 5)
     a, *rest, c = tp
     print(a, rest, c)  # Output: 1 [2, 3, 4] 5
     ```

---

3. **Tuple Slicing:**
   - Extracting a portion of the tuple using slicing.
     ```python
     tp = (1, 2, 3, 4, 5)
     print(tp[1:4])  # Output: (2, 3, 4)
     ```

---

4. **Nested Tuples:**
   - Accessing and manipulating data within nested tuples.
     ```python
     nested_tp = ((1, 2), (3, 4), (5, 6))
     print(nested_tp[1][0])  # Output: 3
     ```

---

5. **Iterating Through Tuples:**
   - Using loops to iterate over tuple elements.
     ```python
     tp = (1, 2, 3, 4)
     for item in tp:
         print(item)
     ```

---

6. **Tuples vs Lists:**
   - **Immutable:** Tuples cannot be changed after creation, while lists are mutable.
   - **Performance:** Tuples are generally faster than lists.
   - **Use Case:** Use tuples when data should not be modified.

---

7. **Tuple Comprehensions (Using Generator Expressions):**
   - Although tuples don’t support comprehensions directly, you can use a generator expression to create a tuple.
     ```python
     tp = tuple(x**2 for x in range(5))
     print(tp)  # Output: (0, 1, 4, 9, 16)
     ```

---

8. **Tuples with Functions:**
   - Returning multiple values from a function using a tuple.
     ```python
     def min_max(nums):
         return min(nums), max(nums)

     result = min_max([1, 2, 3, 4, 5])
     print(result)  # Output: (1, 5)
     ```

---

9. **Tuples in Sets and Dictionaries:**
   - Tuples can be used as keys in dictionaries or as elements in sets because they are hashable.
     ```python
     tp = (1, 2)
     my_dict = {tp: "value"}
     print(my_dict[(1, 2)])  # Output: value
     ```

---

10. **Tuples for Fixed-Size Data:**
    - Use tuples when the size of the data is constant, like coordinates, RGB values, or database records.

---

### **Specialized Topics**
1. **Comparing Tuples:**
   - Tuples are compared element by element.
     ```python
     print((1, 2) < (1, 3))  # Output: True
     ```

2. **Zip and Tuples:**
   - Combining two or more sequences into a tuple using `zip()`.
     ```python
     names = ('Alice', 'Bob')
     scores = (85, 90)
     combined = tuple(zip(names, scores))
     print(combined)  # Output: (('Alice', 85), ('Bob', 90))
     ```

3. **Tuples with Enumerate:**
   - Enumerating a sequence to get index and value as a tuple.
     ```python
     tp = ('a', 'b', 'c')
     for index, value in enumerate(tp):
         print(index, value)
     ```

4. **Memory Usage of Tuples:**
   - Tuples consume less memory than lists, making them more efficient for large datasets.

---

