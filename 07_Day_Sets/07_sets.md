

### **1. What is a Set?**
A **set** is a collection of unique, unordered, and unindexed elements.

**Example**:
```python
my_set = {1, 2, 3, 3}  # Duplicate '3' is removed
print(my_set)  # Output: {1, 2, 3}
```

---

### **2. Creating a Set**
- Using curly braces `{}`:
  ```python
  my_set = {1, 2, 3}
  ```
- Using `set()` constructor:
  ```python
  empty_set = set()  # Note: {} creates an empty dictionary
  ```

---

### **3. Characteristics of Sets**
- Unordered: No specific order.
- No duplicates: Each element must be unique.
- Mutable: Elements can be added or removed.
- Immutable elements only: Elements must be hashable (e.g., no lists).

---

### **4. Basic Operations**
#### Adding Elements:
```python
my_set = {1, 2}
my_set.add(3)
print(my_set)  # Output: {1, 2, 3}
```

#### Removing Elements:
- **`remove()`** (raises error if not found):
  ```python
  my_set.remove(2)
  ```
- **`discard()`** (no error if not found):
  ```python
  my_set.discard(4)
  ```

---

### **5. Mathematical Set Operations**
#### Union:
Combines all elements from both sets.
```python
A = {1, 2, 3}
B = {3, 4, 5}
print(A | B)  # Output: {1, 2, 3, 4, 5}
```

#### Intersection:
Finds common elements between sets.
```python
print(A & B)  # Output: {3}
```

#### Difference:
Elements in one set but not in the other.
```python
print(A - B)  # Output: {1, 2}
```

#### Symmetric Difference:
Elements in either set but not in both.
```python
print(A ^ B)  # Output: {1, 2, 4, 5}
```

---

### **6. Comparisons**
#### Subset and Superset:
- **Subset**:
  ```python
  A = {1, 2}
  B = {1, 2, 3}
  print(A.issubset(B))  # Output: True
  ```
- **Superset**:
  ```python
  print(B.issuperset(A))  # Output: True
  ```

#### Disjoint:
Check if two sets have no common elements.
```python
C = {4, 5}
print(A.isdisjoint(C))  # Output: True
```

---

### **7. Built-in Methods**
| **Method**              | **Description**                                          |
|--------------------------|----------------------------------------------------------|
| `add(element)`           | Adds an element to the set.                              |
| `update(iterable)`       | Adds multiple elements from an iterable.                 |
| `remove(element)`        | Removes an element; raises error if not found.           |
| `discard(element)`       | Removes an element; no error if not found.               |
| `pop()`                  | Removes and returns a random element.                   |
| `clear()`                | Removes all elements from the set.                       |
| `union(other_set)`       | Returns a new set with all elements from both sets.      |
| `intersection(other_set)`| Returns a new set with common elements.                  |
| `difference(other_set)`  | Returns a new set with elements not in the other set.    |
| `symmetric_difference()` | Returns a new set with elements in either set, not both. |

---

### **8. Frozen Sets**
An immutable version of a set:
```python
frozen = frozenset([1, 2, 3])
print(frozen)  # Output: frozenset({1, 2, 3})
```

---

### **9. Practical Applications**
1. **Remove Duplicates**:
   ```python
   numbers = [1, 2, 2, 3, 4]
   unique_numbers = set(numbers)
   print(unique_numbers)  # Output: {1, 2, 3, 4}
   ```

2. **Membership Testing**:
   ```python
   print(3 in {1, 2, 3})  # Output: True
   ```

3. **Finding Common or Unique Elements**:
   ```python
   students_A = {"John", "Alice"}
   students_B = {"Alice", "Bob"}
   print(students_A & students_B)  # Output: {'Alice'}
   ```

4. **Filtering Using Sets**:
   ```python
   items = [1, 2, 3, 4]
   banned = {2, 4}
   allowed = [item for item in items if item not in banned]
   print(allowed)  # Output: [1, 3]
   ```

---

### **10. Set Comprehension**
A concise way to create sets:
```python
squares = {x**2 for x in range(5)}
print(squares)  # Output: {0, 1, 4, 9, 16}
```

---

### **11. Limitations of Sets**
- Cannot store mutable elements like lists:
  ```python
  my_set = {1, [2, 3]}  # Error: unhashable type: 'list'
  ```

---

### **Example Summary**
```python
A = {1, 2, 3}
B = {3, 4, 5}

# Union
print(A | B)  # {1, 2, 3, 4, 5}

# Intersection
print(A & B)  # {3}

# Difference
print(A - B)  # {1, 2}

# Symmetric Difference
print(A ^ B)  # {1, 2, 4, 5}

# Subset Check
print(A.issubset(B))  # False
```

