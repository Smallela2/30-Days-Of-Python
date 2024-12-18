### **What are Operators?**
Operators are symbols in Python used to perform operations on variables and values. For example: `+`, `-`, `*`, and `/`.

---

### **1. Arithmetic Operators**
Used for mathematical calculations.

| Operator | Description            | Example        | Output |
|----------|------------------------|----------------|--------|
| `+`      | Addition               | `5 + 3`        | `8`    |
| `-`      | Subtraction            | `5 - 3`        | `2`    |
| `*`      | Multiplication         | `5 * 3`        | `15`   |
| `/`      | Division (float)       | `5 / 2`        | `2.5`  |
| `//`     | Floor Division         | `5 // 2`       | `2`    |
| `%`      | Modulus (Remainder)    | `5 % 2`        | `1`    |
| `**`     | Exponentiation (Power) | `2 ** 3`       | `8`    |

**Example Code:**
```python
a = 10
b = 3

print(a + b)  # Addition
print(a - b)  # Subtraction
print(a * b)  # Multiplication
print(a / b)  # Division
print(a // b) # Floor Division
print(a % b)  # Modulus
print(a ** b) # Exponentiation
```

---

### **2. Comparison (Relational) Operators**
Used to compare two values. They return `True` or `False`.

| Operator | Description                  | Example      | Output |
|----------|------------------------------|--------------|--------|
| `==`     | Equal to                    | `5 == 5`     | `True` |
| `!=`     | Not equal to                | `5 != 3`     | `True` |
| `>`      | Greater than                | `5 > 3`      | `True` |
| `<`      | Less than                   | `5 < 3`      | `False`|
| `>=`     | Greater than or equal to    | `5 >= 3`     | `True` |
| `<=`     | Less than or equal to       | `5 <= 5`     | `True` |

**Example Code:**
```python
x = 7
y = 10

print(x == y)  # Equal to
print(x != y)  # Not equal to
print(x > y)   # Greater than
print(x < y)   # Less than
print(x >= y)  # Greater than or equal to
print(x <= y)  # Less than or equal to
```

---

### **3. Logical Operators**
Used to combine conditional statements.

| Operator | Description        | Example          | Output |
|----------|--------------------|------------------|--------|
| `and`    | Logical AND        | `True and False` | `False`|
| `or`     | Logical OR         | `True or False`  | `True` |
| `not`    | Logical NOT        | `not True`       | `False`|

**Example Code:**
```python
a = True
b = False

print(a and b)  # Logical AND
print(a or b)   # Logical OR
print(not a)    # Logical NOT
```

---

### **4. Assignment Operators**
Used to assign values to variables.

| Operator | Description              | Example   | Equivalent To |
|----------|--------------------------|-----------|---------------|
| `=`      | Assign                  | `x = 5`   | `x = 5`       |
| `+=`     | Add and assign           | `x += 5`  | `x = x + 5`   |
| `-=`     | Subtract and assign      | `x -= 5`  | `x = x - 5`   |
| `*=`     | Multiply and assign      | `x *= 5`  | `x = x * 5`   |
| `/=`     | Divide and assign        | `x /= 5`  | `x = x / 5`   |
| `//=`    | Floor divide and assign  | `x //= 5` | `x = x // 5`  |
| `%=`     | Modulus and assign       | `x %= 5`  | `x = x % 5`   |
| `**=`    | Exponent and assign      | `x **= 5` | `x = x ** 5`  |

**Example Code:**
```python
x = 10
x += 5  # Same as x = x + 5
print(x)

x *= 2  # Same as x = x * 2
print(x)
```

---

### **5. Bitwise Operators**
Used for operations at the binary level.

| Operator | Description               | Example   | Output |
|----------|---------------------------|-----------|--------|
| `&`      | AND                      | `5 & 3`   | `1`    |
| `|`      | OR                       | `5 | 3`   | `7`    |
| `^`      | XOR                      | `5 ^ 3`   | `6`    |
| `~`      | NOT                      | `~5`      | `-6`   |
| `<<`     | Left shift               | `5 << 1`  | `10`   |
| `>>`     | Right shift              | `5 >> 1`  | `2`    |

**Example Code:**
```python
a = 5  # Binary: 0101
b = 3  # Binary: 0011

print(a & b)  # AND
print(a | b)  # OR
print(a ^ b)  # XOR
print(~a)     # NOT
print(a << 1) # Left shift
print(a >> 1) # Right shift
```

---

### **6. Membership Operators**
Used to test if a value is in a sequence.

| Operator | Description             | Example            | Output |
|----------|-------------------------|--------------------|--------|
| `in`     | Value is in sequence    | `"a" in "apple"`   | `True` |
| `not in` | Value is not in sequence| `"b" not in "apple"`| `True`|

**Example Code:**
```python
fruits = ["apple", "banana", "cherry"]

print("apple" in fruits)    # True
print("grape" not in fruits) # True
```

---

### **7. Identity Operators**
Used to compare memory locations of two objects.

| Operator | Description             | Example    | Output |
|----------|-------------------------|------------|--------|
| `is`     | Same memory location    | `a is b`   | `True` |
| `is not` | Different memory location| `a is not b` | `True`|

**Example Code:**
```python
x = [1, 2, 3]
y = [1, 2, 3]
z = x

print(x is z)       # True (z is the same object as x)
print(x is y)       # False (x and y are different objects)
print(x == y)       # True (x and y have the same values)
```

---

### Summary:
- **Arithmetic**: Basic math (`+`, `-`, `*`, `/`, etc.).
- **Comparison**: Compare values (`==`, `!=`, `>`, `<`, etc.).
- **Logical**: Combine conditions (`and`, `or`, `not`).
- **Assignment**: Assign values (`=`, `+=`, `-=`).
- **Bitwise**: Work with binary values (`&`, `|`, `^`, `~`).
- **Membership**: Test for inclusion (`in`, `not in`).
- **Identity**: Test memory location (`is`, `is not`).
