### 1. **Introduction to Strings**
- A string is a sequence of characters enclosed in single (`'`) or double (`"`) quotes.
- Strings are immutable (cannot be changed after creation).
  
### 2. **Basic String Operations**
- **Concatenation**: Combining strings using `+`.
  ```python
  s1 = "Hello"
  s2 = "World"
  print(s1 + " " + s2)  # Output: Hello World
  ```
- **Repetition**: Repeating strings using `*`.
  ```python
  print("Python" * 3)  # Output: PythonPythonPython
  ```

### 3. **String Indexing and Slicing**
- **Indexing**: Access characters using their position (starting at `0`).
  ```python
  s = "Python"
  print(s[0])  # Output: P
  print(s[-1])  # Output: n
  ```
- **Slicing**: Extract substrings using `start:end:step`.
  ```python
  print(s[1:4])  # Output: yth
  print(s[:3])   # Output: Pyt
  print(s[::-1]) # Output: nohtyP (reversed string)
  ```

### 4. **String Methods**
- **Case Methods**:
  - `upper()`, `lower()`, `capitalize()`, `title()`, `swapcase()`.
- **Search Methods**:
  - `find(substring)`, `index(substring)`, `rfind(substring)`.
- **Check Methods**:
  - `startswith(substring)`, `endswith(substring)`.
  - `isalpha()`, `isdigit()`, `isalnum()`, `isspace()`.
- **Replace and Split**:
  - `replace(old, new)`, `split(separator)`, `join(iterable)`.
  ```python
  text = "Coding For All"
  print(text.upper())  # CODING FOR ALL
  print(text.find("For"))  # 7
  print(text.replace("Coding", "Programming"))  # Programming For All
  ```

### 5. **Escape Sequences**
- Use `\` to include special characters.
  - `\n` (new line), `\t` (tab), `\\` (backslash), `\'` (single quote), `\"` (double quote).
  ```python
  print("Line1\nLine2")  # Output:
  # Line1
  # Line2
  ```

### 6. **String Formatting**
- **f-strings**: Embed variables directly.
  ```python
  name = "Swathi"
  age = 21
  print(f"Hello, {name}! You are {age} years old.")
  ```
- **format() Method**:
  ```python
  print("Hello, {}!".format("World"))
  ```

### 7. **Common String Problems**
1. **Acronym Creation**:
   ```python
   text = "Python For Everyone"
   acronym = "".join([word[0] for word in text.split()])
   print(acronym)  # PFE
   ```
2. **Removing Extra Spaces**:
   ```python
   s = "   Hello World   "
   print(s.strip())  # Output: Hello World
   ```
3. **Reversing Strings**:
   ```python
   s = "Python"
   print(s[::-1])  # Output: nohtyP
   ```

### 8. **Advanced Concepts**
- **String Immutability**:
  - Strings cannot be modified in place.
  ```python
  s = "Python"
  s[0] = "J"  # Error
  ```
- **Joining Lists into Strings**:
  ```python
  libraries = ["Django", "Flask", "Pyramid"]
  print(" - ".join(libraries))  # Django - Flask - Pyramid

