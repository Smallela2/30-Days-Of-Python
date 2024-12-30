

### **List Comprehension**

List comprehension is a concise way to create lists in Python. It provides a clear and readable way to generate a new list by applying an expression to each item in an iterable.

---

#### **1. Syntax**

```python
[expression for item in iterable if condition]
```

- **`expression`**: Operation or transformation applied to each item.
- **`item`**: The variable representing the current element of the iterable.
- **`iterable`**: A sequence, such as a list, tuple, or range.
- **`condition`** *(optional)*: Filters the items to include in the list.

---

#### **2. Basic Examples**

**Without Condition:**
```python
# Create a list of squares
squares = [x ** 2 for x in range(5)]
print(squares)  # Output: [0, 1, 4, 9, 16]
```

**With Condition:**
```python
# Create a list of even numbers
evens = [x for x in range(10) if x % 2 == 0]
print(evens)  # Output: [0, 2, 4, 6, 8]
```

---

#### **3. Nested Loops in List Comprehension**

You can use multiple loops in list comprehension.

```python
# Cartesian product
pairs = [(x, y) for x in [1, 2, 3] for y in [4, 5, 6]]
print(pairs)  # Output: [(1, 4), (1, 5), (1, 6), (2, 4), (2, 5), (2, 6), (3, 4), (3, 5), (3, 6)]
```

---

#### **4. Advanced Examples**

**Using Functions:**
```python
# Apply a function to each item
def double(x):
    return x * 2

doubles = [double(x) for x in range(5)]
print(doubles)  # Output: [0, 2, 4, 6, 8]
```

**With Condition and Transformation:**
```python
# Square only odd numbers
squared_odds = [x ** 2 for x in range(10) if x % 2 != 0]
print(squared_odds)  # Output: [1, 9, 25, 49, 81]
```

---

### **Lambda Functions**

Lambda functions are anonymous (unnamed) functions in Python. They are commonly used for short, single-expression functions.

---

#### **1. Syntax**

```python
lambda arguments: expression
```

- **`arguments`**: The input parameters.
- **`expression`**: A single expression evaluated and returned.

---

#### **2. Basic Examples**

**Single Argument:**
```python
# Square of a number
square = lambda x: x ** 2
print(square(4))  # Output: 16
```

**Multiple Arguments:**
```python
# Sum of two numbers
add = lambda x, y: x + y
print(add(3, 5))  # Output: 8
```

**Conditional Expression:**
```python
# Check if a number is even
is_even = lambda x: "Even" if x % 2 == 0 else "Odd"
print(is_even(5))  # Output: Odd
```

---

#### **3. Common Use Cases**

**With `map`:**
Apply a function to each item in an iterable.

```python
nums = [1, 2, 3, 4]
squared = list(map(lambda x: x ** 2, nums))
print(squared)  # Output: [1, 4, 9, 16]
```

**With `filter`:**
Filter items based on a condition.

```python
nums = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda x: x % 2 == 0, nums))
print(evens)  # Output: [2, 4, 6]
```

**With `reduce`:**
Reduce a list to a single value.

```python
from functools import reduce

nums = [1, 2, 3, 4]
product = reduce(lambda x, y: x * y, nums)
print(product)  # Output: 24
```

---

### **Comparison: List Comprehension vs Lambda Functions**

| Feature                  | List Comprehension                              | Lambda Functions                              |
|--------------------------|------------------------------------------------|----------------------------------------------|
| **Purpose**              | Generate new lists concisely.                  | Create short, anonymous functions.           |
| **Syntax**               | `[expression for item in iterable if condition]`| `lambda arguments: expression`               |
| **Use Case**             | Data transformation, filtering, or mapping.    | Inline operations with `map`, `filter`, etc. |
| **Readability**          | More readable for creating lists.              | Simple for one-liner operations.             |

---

### **Key Points to Remember**

1. **List Comprehension**:
   - Best for generating or transforming lists.
   - Readable and efficient for most use cases.

2. **Lambda Functions**:
   - Great for temporary or inline functions.
   - Can be combined with higher-order functions like `map`, `filter`, and `reduce`.

