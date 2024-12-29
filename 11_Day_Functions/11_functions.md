
### **What is a Function?**
A function is a reusable block of code that performs a specific task. Functions can take inputs (parameters) and return outputs.

#### Example:
```python
def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))  # Output: Hello, Alice!
```

---

### **Defining and Calling Functions**
- Use `def` to define a function.
- Call the function by using its name followed by parentheses.

#### Example:
```python
def add(a, b):
    return a + b

print(add(2, 3))  # Output: 5
```

---

### **Default Parameters**
Functions can have default values for parameters.

#### Example:
```python
def greet(name="Guest"):
    return f"Hello, {name}!"

print(greet())  # Output: Hello, Guest!
print(greet("Alice"))  # Output: Hello, Alice!
```

---

### **Return Statement**
The `return` statement sends a result back to the caller.

#### Example:
```python
def square(number):
    return number * number

print(square(4))  # Output: 16
```

---

## **2. Variable Scope**
- **Local Scope**: Variables defined inside a function.
- **Global Scope**: Variables defined outside any function.
- Use the `global` keyword to modify global variables inside a function.

#### Example:
```python
x = 10

def modify_global():
    global x
    x = 20

modify_global()
print(x)  # Output: 20
```

---

## **3. Types of Arguments**
### **Positional Arguments**
Arguments are passed in order.

#### Example:
```python
def add(a, b):
    return a + b

print(add(3, 4))  # Output: 7
```

---

### **Keyword Arguments**
Arguments are passed by name.

#### Example:
```python
def introduce(name, age):
    return f"My name is {name}, and I'm {age} years old."

print(introduce(age=25, name="Alice"))
# Output: My name is Alice, and I'm 25 years old.
```

---

### **Arbitrary Arguments (`*args`)**
Used to pass a variable number of positional arguments.

#### Example:
```python
def add_all(*args):
    return sum(args)

print(add_all(1, 2, 3, 4))  # Output: 10
```

---

### **Arbitrary Keyword Arguments (`**kwargs`)**
Used to pass a variable number of keyword arguments.

#### Example:
```python
def show_details(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

show_details(name="Alice", age=25, location="NYC")
```

---

## **4. Lambda Functions**
Anonymous, single-line functions defined using the `lambda` keyword.

#### Example:
```python
square = lambda x: x * x
print(square(5))  # Output: 25
```

---

## **5. Higher-Order Functions**
Functions that take other functions as arguments or return them.

#### Example: `map`
```python
nums = [1, 2, 3]
squares = map(lambda x: x ** 2, nums)
print(list(squares))  # Output: [1, 4, 9]
```

#### Example: `filter`
```python
nums = [1, 2, 3, 4]
evens = filter(lambda x: x % 2 == 0, nums)
print(list(evens))  # Output: [2, 4]
```

---

## **6. Recursive Functions**
Functions that call themselves to solve problems iteratively.

#### Example:
```python
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))  # Output: 120
```

---

## **7. Decorators**
Functions that modify the behavior of other functions.

#### Example:
```python
def decorator(func):
    def wrapper():
        print("Before function call")
        func()
        print("After function call")
    return wrapper

@decorator
def say_hello():
    print("Hello!")

say_hello()
# Output:
# Before function call
# Hello!
# After function call
```

---

## **8. Generators**
Functions that yield values one at a time using `yield`.

#### Example:
```python
def count_up_to(n):
    count = 1
    while count <= n:
        yield count
        count += 1

for num in count_up_to(5):
    print(num)
```

---

## **9. Closures**
A closure is a function that remembers the variables from its enclosing scope.

#### Example:
```python
def make_multiplier(x):
    def multiplier(y):
        return x * y
    return multiplier

double = make_multiplier(2)
print(double(5))  # Output: 10
```

---

## **10. Function Annotations**
Provide metadata about function parameters and return values.

#### Example:
```python
def add(a: int, b: int) -> int:
    return a + b

print(add(2, 3))  # Output: 5
```

---

## **11. Partial Functions**
Create new functions by fixing some arguments of an existing function.

#### Example:
```python
from functools import partial

def power(base, exponent):
    return base ** exponent

square = partial(power, exponent=2)
print(square(4))  # Output: 16
```

---

## **12. Asynchronous Functions**
Use `async` and `await` for asynchronous programming.

#### Example:
```python
import asyncio

async def greet():
    print("Hello!")
    await asyncio.sleep(1)
    print("Goodbye!")

asyncio.run(greet())
```

---

## **13. Introspection**
Access function metadata using attributes like `__name__` and `__doc__`.

#### Example:
```python
def sample_function():
    """This is a sample function."""
    pass

print(sample_function.__doc__)  # Output: This is a sample function.
```

