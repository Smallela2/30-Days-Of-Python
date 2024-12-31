
#### **1. Functions as First-Class Citizens**
- In Python, functions are first-class citizens, meaning they can be:
  - Assigned to variables.
  - Passed as arguments to other functions.
  - Returned from other functions.

**Example:**
```python
def greet(name):
    return f"Hello, {name}!"

# Assigning the function to a variable
say_hello = greet
print(say_hello("Alice"))  # Output: Hello, Alice!
```

#### **2. Passing Functions as Arguments**
Higher-order functions can accept other functions as arguments.

**Example:**
```python
def apply_function(f, value):
    return f(value)

def square(x):
    return x ** 2

print(apply_function(square, 5))  # Output: 25
```

#### **3. Returning Functions from Functions**
A function can return another function, often used in closures and decorators.

**Example:**
```python
def multiply_by(factor):
    def multiplier(x):
        return x * factor
    return multiplier

times_two = multiply_by(2)
print(times_two(5))  # Output: 10
```

#### **4. Common Higher-Order Functions**

- **`map()`**: Applies a function to all items in an iterable.

  **Example:**
  ```python
  numbers = [1, 2, 3, 4]
  squared = map(lambda x: x ** 2, numbers)
  print(list(squared))  # Output: [1, 4, 9, 16]
  ```

- **`filter()`**: Filters items in an iterable based on a condition.

  **Example:**
  ```python
  numbers = [1, 2, 3, 4, 5, 6]
  even_numbers = filter(lambda x: x % 2 == 0, numbers)
  print(list(even_numbers))  # Output: [2, 4, 6]
  ```

- **`reduce()`**: Applies a binary function cumulatively to the items of an iterable to reduce it to a single value. (From `functools`)

  **Example:**
  ```python
  from functools import reduce
  numbers = [1, 2, 3, 4]
  product = reduce(lambda x, y: x * y, numbers)
  print(product)  # Output: 24
  ```

#### **5. Decorators**
A decorator is a higher-order function that takes a function as an argument and returns a new function that enhances or modifies the original function.

**Example:**
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
```

**Output:**
```
Before function call
Hello!
After function call
```

#### **6. Function Composition**
Function composition is the process of combining multiple functions where the output of one function is the input to another.

**Example:**
```python
def add(x):
    return x + 2

def multiply(x):
    return x * 3

def compose(f, g):
    return lambda x: f(g(x))

composed = compose(add, multiply)
print(composed(5))  # Output: 17 (5 * 3 + 2)
```

#### **7. Currying**
Currying is the technique of turning a function that takes multiple arguments into a series of functions, each taking a single argument.

**Example:**
```python
def curried_add(x):
    def add_y(y):
        return x + y
    return add_y

add_5 = curried_add(5)
print(add_5(3))  # Output: 8
```

#### **8. Lambda Functions**
Lambda functions are anonymous functions defined using the `lambda` keyword, commonly used in higher-order functions like `map()`, `filter()`, and `reduce()`.

**Syntax:**
```python
lambda arguments: expression
```

**Example:**
```python
numbers = [1, 2, 3, 4]
squared = map(lambda x: x ** 2, numbers)
print(list(squared))  # Output: [1, 4, 9, 16]
```

#### **9. Partial Functions**
Partial functions allow you to fix a certain number of arguments of a function, generating a new function that accepts fewer arguments.

**Example:**
```python
from functools import partial

def multiply(x, y):
    return x * y

double = partial(multiply, 2)
print(double(5))  # Output: 10
```

#### **10. Closures**
A closure occurs when a function retains access to the variables from its enclosing scope even after the outer function has finished executing.

**Example:**
```python
def outer_function(x):
    def inner_function(y):
        return x + y
    return inner_function

add_five = outer_function(5)
print(add_five(3))  # Output: 8
```

#### **11. Functools `wraps()`**
In decorators, `functools.wraps()` helps preserve the original function's metadata, such as its name and docstring, when it's wrapped by a decorator.

**Example:**
```python
from functools import wraps

def decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Before function call")
        result = func(*args, **kwargs)
        print("After function call")
        return result
    return wrapper

@decorator
def say_hello():
    """Says hello to the world."""
    print("Hello!")

print(say_hello.__name__)  # Output: say_hello
print(say_hello.__doc__)   # Output: Says hello to the world.
```

#### **12. Comprehensions with Higher-Order Functions**
List, set, and dictionary comprehensions are concise alternatives to `map()` and `filter()`.

- **Example (using `map()`):**
  ```python
  numbers = [1, 2, 3, 4]
  squared = [x ** 2 for x in numbers]
  print(squared)  # Output: [1, 4, 9, 16]
  ```

- **Example (using `filter()`):**
  ```python
  numbers = [1, 2, 3, 4, 5, 6]
  even_numbers = [x for x in numbers if x % 2 == 0]
  print(even_numbers)  # Output: [2, 4, 6]
  ```

#### **13. Lazy Evaluation**
Some higher-order functions like `map()`, `filter()`, and `zip()` return iterators, which are lazily evaluated. They compute values only when needed, improving performance with large datasets.

**Example:**
```python
numbers = range(1, 1000000)
squared = map(lambda x: x ** 2, numbers)
# No computation yet
print(next(squared))  # Output: 1 (computes the first value)
```

#### **14. Chaining Higher-Order Functions**
You can combine multiple higher-order functions in a chain for more complex transformations.

**Example:**
```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
squared_even_numbers = map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, numbers))
print(list(squared_even_numbers))  # Output: [4, 16, 36, 64]
```

### **Summary of Key Points:**
- **First-Class Functions**: Functions can be passed as arguments, returned from other functions, or assigned to variables.
- **Higher-Order Functions**: Functions like `map()`, `filter()`, `reduce()`, decorators, and composition that accept or return functions.
- **Advanced Concepts**:
  - **Lambda Functions**: Anonymous functions used with higher-order functions.
  - **Partial Functions**: Functions that fix some arguments of another function.
  - **Closures**: Functions that "remember" variables from their enclosing scope.
  - **Functools `wraps()`**: Used in decorators to preserve metadata.
  - **Lazy Evaluation**: Delayed computation of values, useful for large datasets.
  - **Chaining Functions**: Combining multiple higher-order functions for complex transformations.


