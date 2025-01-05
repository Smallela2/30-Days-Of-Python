

### **1. Introduction to `re` Module**
The `re` module in Python provides support for working with Regular Expressions (RegEx). It allows you to search, match, and manipulate text based on patterns.

---

### **2. Core Functions in `re` Module**

#### **a) `re.match()`**
- Checks if the pattern matches at the beginning of the string.
- Returns a match object or `None`.

Example:
```python
import re
result = re.match(r"hello", "hello world")
print(result)  # Output: <re.Match object; span=(0, 5), match='hello'>
```

---

#### **b) `re.search()`**
- Searches for the first occurrence of the pattern anywhere in the string.
- Returns a match object or `None`.

Example:
```python
result = re.search(r"world", "hello world")
print(result)  # Output: <re.Match object; span=(6, 11), match='world'>
```

---

#### **c) `re.findall()`**
- Finds all occurrences of the pattern in the string.
- Returns a list of matches.

Example:
```python
result = re.findall(r"\d", "123abc456")
print(result)  # Output: ['1', '2', '3', '4', '5', '6']
```

---

#### **d) `re.finditer()`**
- Similar to `re.findall()` but returns an iterator of match objects instead of a list.

Example:
```python
matches = re.finditer(r"\d", "123abc456")
for match in matches:
    print(match)  # Outputs match objects for each digit
```

---

#### **e) `re.sub()`**
- Replaces occurrences of a pattern with a replacement string.

Example:
```python
result = re.sub(r"world", "Python", "hello world")
print(result)  # Output: hello Python
```

---

#### **f) `re.split()`**
- Splits a string at each match of the pattern.

Example:
```python
result = re.split(r"\s", "hello world")
print(result)  # Output: ['hello', 'world']
```

---

#### **g) `re.fullmatch()`**
- Checks if the whole string matches the pattern.
- Returns a match object or `None`.

Example:
```python
result = re.fullmatch(r"\d+", "12345")
print(result)  # Output: <re.Match object; span=(0, 5), match='12345'>
```

---

### **3. Match Object Methods**

The match object returned by `re.match()`, `re.search()`, and other methods has several useful methods:

- **`group()`**: Returns the matched string.
- **`start()`**: Returns the start position of the match.
- **`end()`**: Returns the end position of the match.
- **`span()`**: Returns a tuple of the start and end positions.

Example:
```python
match = re.search(r"world", "hello world")
if match:
    print(match.group())  # Output: world
    print(match.start())  # Output: 6
    print(match.end())    # Output: 11
    print(match.span())   # Output: (6, 11)
```

---

### **4. Special Characters and Escape Sequences**

#### **a) `.` (Dot)**
Matches any character except a newline.

#### **b) `\` (Escape Character)**
Escapes special characters or defines sequences like:
- `\d`: Matches digits.
- `\D`: Matches non-digits.
- `\w`: Matches word characters.
- `\W`: Matches non-word characters.
- `\s`: Matches whitespace.
- `\S`: Matches non-whitespace.

---

### **5. Anchors**

#### **a) `^` (Caret)**
Matches the start of a string.

#### **b) `$` (Dollar Sign)**
Matches the end of a string.

Example:
```python
print(re.search(r"^hello", "hello world"))  # Matches
print(re.search(r"world$", "hello world"))  # Matches
```

---

### **6. Character Classes**

#### **a) `[ ]`**
Matches any one of the characters inside the brackets.

#### **b) `[^ ]`**
Matches any character NOT in the brackets.

Example:
```python
print(re.findall(r"[aeiou]", "hello world"))  # Vowels
print(re.findall(r"[^aeiou]", "hello world"))  # Non-vowels
```

---

### **7. Quantifiers**

#### **a) `*`**
Matches 0 or more occurrences.

#### **b) `+`**
Matches 1 or more occurrences.

#### **c) `?`**
Matches 0 or 1 occurrence.

#### **d) `{n}`**
Matches exactly `n` occurrences.

#### **e) `{n,}`**
Matches `n` or more occurrences.

#### **f) `{n,m}`**
Matches between `n` and `m` occurrences.

Example:
```python
print(re.findall(r"a+", "aaabbbaaa"))  # Output: ['aaa', 'aaa']
print(re.findall(r"a{2,4}", "aaabbbaaa"))  # Output: ['aaa', 'aaa']
```

---

### **8. Flags**

- **`re.IGNORECASE` (`re.I`)**: Case-insensitive matching.
- **`re.MULTILINE` (`re.M`)**: Makes `^` and `$` match start/end of each line.
- **`re.DOTALL` (`re.S`)**: Makes `.` match newlines.
- **`re.VERBOSE` (`re.X`)**: Allows comments and better formatting in patterns.

Example:
```python
pattern = r""" 
    \d+   # Match digits
    \s*   # Match whitespace
"""
print(re.findall(pattern, "123 abc", re.VERBOSE))
```

---

### **9. Groups and Capturing**

#### **a) Grouping with `()`**
Groups parts of a pattern.

#### **b) Named Groups with `(?P<name>...)`**
Creates named capturing groups.

#### **c) Accessing Groups**
- Use `group(n)` for groups by index.
- Use `groupdict()` for named groups.

Example:
```python
pattern = r"(\d{3})-(\d{2})-(\d{4})"
match = re.match(pattern, "123-45-6789")
if match:
    print(match.group(1))  # Output: 123
    print(match.groups())  # Output: ('123', '45', '6789')
```

---

### **10. Lookahead and Lookbehind**

#### **a) Positive Lookahead `(?=...)`**
Matches if the pattern inside `()` exists after the current position.

#### **b) Negative Lookahead `(?!...)`**
Matches if the pattern inside `()` does NOT exist after the current position.

#### **c) Positive Lookbehind `(?<=...)`**
Matches if the pattern inside `()` exists before the current position.

#### **d) Negative Lookbehind `(?<!...)`**
Matches if the pattern inside `()` does NOT exist before the current position.

Example:
```python
pattern = r"(?<=\$)\d+"
print(re.findall(pattern, "Price: $100"))  # Output: ['100']
```
