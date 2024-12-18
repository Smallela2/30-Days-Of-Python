### **1. Variables**
- **Definition**: Variables are used to store data values.  
- **Rules for Naming Variables**:
  - Must start with a letter or an underscore (`_`).
  - Cannot start with a number.
  - Can contain letters, numbers, and underscores.
  - Case-sensitive (`myVar` and `myvar` are different).

**Examples**:  
```python
x = 10            # Integer
name = "Swathi"   # String
_pi = 3.14        # Float
```

---

### **2. Variable Assignment**
- You can assign multiple variables at once:
  ```python
  a, b, c = 5, 10, 15
  print(a, b, c)  # Output: 5 10 15
  ```
- You can assign the same value to multiple variables:
  ```python
  x = y = z = 20
  print(x, y, z)  # Output: 20 20 20
  ```

---

### **3. Data Types in Python**
Python has several built-in data types grouped into categories:

| **Data Type**  | **Examples**              | **Description**                             |
|-----------------|--------------------------|---------------------------------------------|
| **int**        | `10`, `-5`               | Whole numbers, positive or negative.        |
| **float**      | `3.14`, `-2.7`           | Numbers with a decimal point.               |
| **complex**    | `1 + 2j`                 | Complex numbers (real + imaginary parts).   |
| **str**        | `'Hello'`, `"World"`     | Sequence of characters (strings).           |
| **list**       | `[1, 2, 3]`              | Ordered, mutable collection of items.       |
| **tuple**      | `(1, 2, 3)`              | Ordered, immutable collection of items.     |
| **set**        | `{1, 2, 3}`              | Unordered collection of unique items.       |
| **dict**       | `{"key": "value"}`       | Key-value pairs (dictionary).               |
| **bool**       | `True`, `False`          | Logical values (boolean).                   |

---

### **4. Check Data Type**
You can use the `type()` function to check the type of a variable:  
```python
x = 10
print(type(x))  # Output: <class 'int'>
```

---

### **5. Dynamic Typing**
Python is dynamically typed, meaning you don't need to declare the type of a variable—it is inferred automatically:
```python
x = 10           # x is an integer
x = "Hello"      # Now x is a string
print(x)         # Output: Hello
```

---

### **6. Type Conversion**
Convert data from one type to another:
- `int()`: Converts to integer.
- `float()`: Converts to float.
- `str()`: Converts to string.

**Examples**:  
```python
num = "10"
print(int(num))       # Converts string to integer: 10
print(float(num))     # Converts string to float: 10.0
```

---

### **7. Mutable vs Immutable Data Types**
- **Mutable**: Can be changed after creation (e.g., `list`, `dict`, `set`).
- **Immutable**: Cannot be changed after creation (e.g., `int`, `float`, `tuple`, `str`).

**Example**:  
```python
# Mutable example
my_list = [1, 2, 3]
my_list[0] = 10        # Changes the first element
print(my_list)         # Output: [10, 2, 3]

# Immutable example
x = "Hello"
x[0] = "Y"             # Error: strings are immutable
```

---

### **8. Best Practices for Variables**
- Use meaningful names:  
  ```python
  name = "Swathi"       # Clear and descriptive
  x = "Swathi"          # Not recommended
  ```
- Use snake_case for variable names:
  ```python
  first_name = "Swathi"
