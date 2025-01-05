

### **1. Regular Expressions**
Regular Expressions are patterns used to match character combinations in strings. They allow us to search, edit, or manipulate text based on defined patterns.

---

### **2. The `re` Module**
The `re` module in Python provides functionalities to work with Regular Expressions. It includes methods for matching, searching, replacing, and splitting strings.

To use it:
```python
import re
```

---

### **3. Methods in `re` Module**

#### **a) `re.match()`**
Checks for a match only at the beginning of the string.
```python
import re
pattern = r"hello"
result = re.match(pattern, "hello world")
print(result)  # Output: <re.Match object; span=(0, 5), match='hello'>
```

#### **b) `re.search()`**
Searches for the pattern throughout the string and returns the first match.
```python
pattern = r"world"
result = re.search(pattern, "hello world")
print(result)  # Output: <re.Match object; span=(6, 11), match='world'>
```

#### **c) `re.findall()`**
Finds all occurrences of the pattern in the string.
```python
pattern = r"o"
result = re.findall(pattern, "hello world")
print(result)  # Output: ['o', 'o']
```

#### **d) `re.sub()`**
Replaces occurrences of the pattern with a given string.
```python
pattern = r"world"
result = re.sub(pattern, "Python", "hello world")
print(result)  # Output: hello Python
```

#### **e) `re.split()`**
Splits the string at every match of the pattern.
```python
pattern = r"\s"
result = re.split(pattern, "hello world")
print(result)  # Output: ['hello', 'world']
```

---

### **4. Writing RegEx Patterns**

#### **a) Square Bracket `[ ]`**
Defines a set of characters to match.
```python
pattern = r"[aeiou]"
result = re.findall(pattern, "hello world")
print(result)  # Output: ['e', 'o', 'o']
```

#### **b) Escape Character `\`**
Used to escape special characters.
```python
pattern = r"\."
result = re.search(pattern, "www.example.com")
print(result)  # Output: <re.Match object; span=(3, 4), match='.'>
```

#### **c) One or More Times `+`**
Matches one or more occurrences of the preceding character.
```python
pattern = r"a+"
result = re.findall(pattern, "aaaabbb")
print(result)  # Output: ['aaaa']
```

#### **d) Period `.`**
Matches any single character except a newline.
```python
pattern = r"h.llo"
result = re.search(pattern, "hello")
print(result)  # Output: <re.Match object; span=(0, 5), match='hello'>
```

#### **e) Zero or More Times `*`**
Matches zero or more occurrences of the preceding character.
```python
pattern = r"ho*"
result = re.findall(pattern, "ho hoooo h")
print(result)  # Output: ['ho', 'hoooo', 'h']
```

#### **f) Zero or One Time `?`**
Matches zero or one occurrence of the preceding character.
```python
pattern = r"colou?r"
result = re.findall(pattern, "color colour")
print(result)  # Output: ['color', 'colour']
```

#### **g) Quantifier `{n, m}`**
Matches a specific number of occurrences.
- `{n}`: Exactly `n` times
- `{n,}`: At least `n` times
- `{n, m}`: Between `n` and `m` times
```python
pattern = r"a{2,4}"
result = re.findall(pattern, "aaa aaaaa")
print(result)  # Output: ['aaa', 'aaaa']
```

---

### **5. `^` (Caret)**
Indicates the start of a string or negation inside square brackets.

#### **a) Start of a String**
```python
pattern = r"^hello"
result = re.match(pattern, "hello world")
print(result)  # Output: <re.Match object; span=(0, 5), match='hello'>
```

#### **b) Negation Inside Square Brackets**
`[^abc]` matches any character except `a`, `b`, or `c`.
```python
pattern = r"[^aeiou]"
result = re.findall(pattern, "hello world")
print(result)  # Output: ['h', 'l', 'l', ' ', 'w', 'r', 'l', 'd']
```

