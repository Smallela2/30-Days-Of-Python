

### 1. **`SyntaxError`**
Occurs when Python detects an error in the syntax of your code.

- **Cause:** Invalid Python syntax.
- **Example:**
  ```python
  if True
      print("Missing colon")  # SyntaxError: invalid syntax
  ```

- **Solution:** Correct the syntax to follow Python's rules.
  ```python
  if True:
      print("Missing colon fixed")
  ```

---

### 2. **`NameError`**
Occurs when a variable or function name is not defined.

- **Cause:** Using a variable or function before defining it or misspelling it.
- **Example:**
  ```python
  print(value)  # NameError: name 'value' is not defined
  ```

- **Solution:** Define the variable or correct the spelling.
  ```python
  value = 10
  print(value)  # Output: 10
  ```

---

### 3. **`IndexError`**
Occurs when trying to access an element outside the valid range of an index.

- **Cause:** Using an index that is out of bounds.
- **Example:**
  ```python
  lst = [1, 2, 3]
  print(lst[5])  # IndexError: list index out of range
  ```

- **Solution:** Ensure the index is within the range of the list.
  ```python
  print(lst[-1])  # Output: 3 (last element of the list)
  ```

---

### 4. **`ModuleNotFoundError`**
Occurs when Python cannot find the module you're trying to import.

- **Cause:** Typo in the module name or the module is not installed.
- **Example:**
  ```python
  import non_existent_module  # ModuleNotFoundError
  ```

- **Solution:** Check the module name or install it using `pip`.
  ```bash
  pip install some_module
  ```

---

### 5. **`AttributeError`**
Occurs when trying to access an attribute or method that doesn't exist.

- **Cause:** Accessing an attribute not defined for an object.
- **Example:**
  ```python
  lst = [1, 2, 3]
  lst.append(4)
  lst.add(5)  # AttributeError: 'list' object has no attribute 'add'
  ```

- **Solution:** Use a valid method or attribute.
  ```python
  lst.append(5)  # Correct way to add an element to a list
  ```

---

### 6. **`KeyError`**
Occurs when trying to access a key that doesn't exist in a dictionary.

- **Cause:** Using a non-existent key in a dictionary.
- **Example:**
  ```python
  d = {"name": "Alice"}
  print(d["age"])  # KeyError: 'age'
  ```

- **Solution:** Use `.get()` or check if the key exists.
  ```python
  print(d.get("age", "Key not found"))  # Output: Key not found
  ```

---

### 7. **`TypeError`**
Occurs when an operation or function is applied to an object of inappropriate type.

- **Cause:** Mismatched data types.
- **Example:**
  ```python
  print("5" + 5)  # TypeError: can only concatenate str (not "int") to str
  ```

- **Solution:** Convert the data type to match.
  ```python
  print(int("5") + 5)  # Output: 10
  ```

---

### 8. **`ImportError`**
Occurs when an import statement fails to find a module or its attribute.

- **Cause:** Module exists, but an attribute or submodule is missing.
- **Example:**
  ```python
  from math import cube  # ImportError: cannot import name 'cube'
  ```

- **Solution:** Check the module documentation for available attributes.
  ```python
  from math import sqrt
  print(sqrt(16))  # Output: 4.0
  ```

---

### 9. **`ValueError`**
Occurs when a function gets an argument of the right type but inappropriate value.

- **Cause:** Invalid argument value.
- **Example:**
  ```python
  int("abc")  # ValueError: invalid literal for int() with base 10
  ```

- **Solution:** Provide a valid value.
  ```python
  print(int("123"))  # Output: 123
  ```

---

### 10. **`ZeroDivisionError`**
Occurs when dividing a number by zero.

- **Cause:** Division or modulo operation by zero.
- **Example:**
  ```python
  result = 10 / 0  # ZeroDivisionError: division by zero
  ```

- **Solution:** Check the denominator before division.
  ```python
  denominator = 0
  if denominator != 0:
      result = 10 / denominator
  else:
      print("Cannot divide by zero")
  ```

---

### **Summary Table**

| **Error**              | **Cause**                                                 | **Example**                                  |
|-------------------------|-----------------------------------------------------------|----------------------------------------------|
| `SyntaxError`           | Invalid syntax                                            | `if True print("Hello")`                     |
| `NameError`             | Variable/function not defined                             | `print(undeclared_var)`                      |
| `IndexError`            | Index out of range                                        | `lst[10]`                                    |
| `ModuleNotFoundError`   | Module not found                                          | `import non_existent_module`                |
| `AttributeError`        | Attribute or method does not exist                        | `lst.add(5)`                                 |
| `KeyError`              | Non-existent dictionary key                               | `d["invalid_key"]`                           |
| `TypeError`             | Inappropriate operation for the object type              | `"5" + 5`                                    |
| `ImportError`           | Importing a missing module/attribute                      | `from math import cube`                      |
| `ValueError`            | Argument has correct type but invalid value               | `int("abc")`                                 |
| `ZeroDivisionError`     | Division/modulo by zero                                   | `10 / 0`                                     |


