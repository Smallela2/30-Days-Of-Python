
## **1. Basic Syntax: `if`, `elif`, and `else`**

Conditionals execute code based on whether a condition is `True` or `False`.

### Example:
```python
age = 20
if age >= 18:
    print("You are an adult.")
elif age > 12:
    print("You are a teenager.")
else:
    print("You are a child.")
```

### Output:
```
You are an adult.
```

---

## **2. Comparison Operators**

Used to compare values in conditionals:
- `==` : Equal to
- `!=` : Not equal to
- `<` : Less than
- `>` : Greater than
- `<=` : Less than or equal to
- `>=` : Greater than or equal to

### Example:
```python
x, y = 5, 10
if x < y:
    print("x is less than y")
else:
    print("x is greater than or equal to y")
```

### Output:
```
x is less than y
```

---

## **3. Logical Operators**

- `and`: Returns `True` if all conditions are true.
- `or`: Returns `True` if at least one condition is true.
- `not`: Reverses the truth value.

### Example:
```python
x = 15
if x > 10 and x < 20:
    print("x is between 10 and 20")
if not (x < 10):
    print("x is not less than 10")
```

### Output:
```
x is between 10 and 20
x is not less than 10
```

---

## **4. Nested Conditionals**

Conditionals inside other conditionals.

### Example:
```python
num = 15
if num > 0:
    if num % 2 == 0:
        print("Positive even number")
    else:
        print("Positive odd number")
else:
    print("Negative number")
```

### Output:
```
Positive odd number
```

---

## **5. Ternary Conditional (One-Liner `if` Statement)**

Compact syntax for simple conditionals.

### Example:
```python
age = 17
message = "Adult" if age >= 18 else "Minor"
print(message)
```

### Output:
```
Minor
```

---

## **6. Membership Operators in Conditionals**

- `in`: Checks if an element is in a sequence.
- `not in`: Checks if an element is not in a sequence.

### Example:
```python
fruits = ["apple", "banana", "cherry"]
if "banana" in fruits:
    print("Banana is in the list")
```

### Output:
```
Banana is in the list
```

---

## **7. `pass` in Conditionals**

Used as a placeholder for incomplete code blocks.

### Example:
```python
x = 10
if x > 5:
    pass  # Code to be added later
else:
    print("x is 5 or less")
```

---

## **8. Chained Conditionals**

Combine multiple conditions without using logical operators.

### Example:
```python
x = 10
if 5 < x < 15:
    print("x is between 5 and 15")
```

### Output:
```
x is between 5 and 15
```

---

## **9. Conditionals in Loops**

Use conditionals inside loops to filter or process data.

### Example:
```python
nums = [1, 2, 3, 4, 5]
for num in nums:
    if num % 2 == 0:
        print(f"{num} is even")
```

### Output:
```
2 is even
4 is even
```

---

## **10. List Comprehensions with Conditionals**

Short and efficient syntax for filtering or transforming lists.

### Example:
```python
nums = [1, 2, 3, 4, 5]
even_nums = [num for num in nums if num % 2 == 0]
print(even_nums)
```

### Output:
```
[2, 4]
```

---

## **11. Using Dictionaries as a Switch-Case Alternative**

Simulate a `switch-case` using dictionaries.

### Example:
```python
def get_day(num):
    days = {1: "Monday", 2: "Tuesday", 3: "Wednesday"}
    return days.get(num, "Invalid day")

print(get_day(1))  # Output: Monday
print(get_day(4))  # Output: Invalid day
```

---

## **12. Conditionals with Functions**

Encapsulate logic in functions.

### Example:
```python
def is_even(num):
    return "Even" if num % 2 == 0 else "Odd"

print(is_even(10))  # Output: Even
print(is_even(7))   # Output: Odd
```

---

## **13. Error Handling with Conditionals**

Validate inputs using conditionals before processing.

### Example:
```python
try:
    num = int(input("Enter a number: "))
    if num > 0:
        print("Positive number")
    else:
        print("Non-positive number")
except ValueError:
    print("Invalid input")
```

### Output:
```
Enter a number: abc
Invalid input
```

---

## **14. Best Practices for Conditionals**

- **Avoid deep nesting:** Refactor long nested conditionals into functions.
- **Use meaningful variable names:** Make your conditions self-explanatory.
- **Short-circuit conditions:** Combine conditions logically to minimize checks.

### Example:
```python
# Bad Practice
if user != "admin":
    if status == "active":
        print("Access granted")

# Refactored
if user == "admin" and status == "active":
    print("Access granted")
```



