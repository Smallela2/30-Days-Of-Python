
### **1. What are Classes and Objects?**
- **Class**: A blueprint for creating objects. It defines a set of attributes (variables) and methods (functions) that the objects created from the class will have.
- **Object**: An instance of a class. It is created using the class and has its own attributes and methods.

#### Example:
```python
# Class definition
class Dog:
    pass  # Empty class

# Creating objects
dog1 = Dog()  # dog1 is an object of the Dog class
dog2 = Dog()  # dog2 is another object of the Dog class

print(type(dog1))  # Output: <class '__main__.Dog'>
```

---

### **2. Defining a Class**
A class is defined using the `class` keyword.

#### Example:
```python
class Dog:
    # Class body
    species = "Canine"  # Class attribute

    # Method
    def bark(self):
        print("Woof!")
```

---

### **3. Creating an Object**
Objects are created by calling the class as if it were a function.

#### Example:
```python
# Create an object
my_dog = Dog()

# Accessing attributes and methods
print(my_dog.species)  # Output: Canine
my_dog.bark()          # Output: Woof!
```

---

### **4. Attributes and Methods**
- **Attributes**: Variables that belong to an object or class.
- **Methods**: Functions defined within a class that operate on its objects.

#### Example:
```python
class Dog:
    species = "Canine"  # Class attribute

    def __init__(self, name, age):
        self.name = name  # Instance attribute
        self.age = age    # Instance attribute

    def bark(self):
        print(f"{self.name} says Woof!")

# Creating objects
dog1 = Dog("Buddy", 5)
dog2 = Dog("Lucy", 3)

# Accessing attributes
print(dog1.name, dog1.age)  # Output: Buddy 5
print(dog2.name, dog2.age)  # Output: Lucy 3

# Calling methods
dog1.bark()  # Output: Buddy says Woof!
dog2.bark()  # Output: Lucy says Woof!
```

---

### **5. The `__init__` Method (Constructor)**
- The `__init__` method is a special method used to initialize an object’s attributes during creation.

#### Example:
```python
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Creating an object with parameters
my_dog = Dog("Buddy", 5)
print(my_dog.name, my_dog.age)  # Output: Buddy 5
```

---

### **6. Class vs. Instance Variables**
- **Class Variables**: Shared across all instances of a class.
- **Instance Variables**: Unique to each object.

#### Example:
```python
class Dog:
    species = "Canine"  # Class variable

    def __init__(self, name):
        self.name = name  # Instance variable

dog1 = Dog("Buddy")
dog2 = Dog("Lucy")

print(dog1.species)  # Output: Canine
print(dog2.species)  # Output: Canine
dog1.species = "Wolf"  # Modifying species for dog1 only
print(dog1.species)  # Output: Wolf
print(dog2.species)  # Output: Canine
```

---

### **7. Instance Methods, Class Methods, and Static Methods**
- **Instance Methods**: Operate on instance data.
- **Class Methods**: Operate on class-level data. Defined with `@classmethod`.
- **Static Methods**: Independent of class or instance data. Defined with `@staticmethod`.

#### Example:
```python
class Dog:
    species = "Canine"

    def __init__(self, name):
        self.name = name

    def instance_method(self):
        return f"{self.name} is a {self.species}"

    @classmethod
    def class_method(cls):
        return f"All dogs are {cls.species}"

    @staticmethod
    def static_method():
        return "Dogs are loyal animals"

dog = Dog("Buddy")
print(dog.instance_method())  # Output: Buddy is a Canine
print(Dog.class_method())     # Output: All dogs are Canine
print(Dog.static_method())    # Output: Dogs are loyal animals
```

---

### **8. Inheritance**
Allows a class (child) to inherit attributes and methods from another class (parent).

#### Example:
```python
class Animal:
    def __init__(self, species):
        self.species = species

    def make_sound(self):
        print("Some generic sound")

class Dog(Animal):  # Dog inherits from Animal
    def __init__(self, name, age):
        super().__init__("Canine")
        self.name = name
        self.age = age

    def make_sound(self):
        print("Woof!")

dog = Dog("Buddy", 5)
print(dog.species)  # Output: Canine
dog.make_sound()    # Output: Woof!
```

---

### **9. Encapsulation**
Encapsulation restricts access to some of an object’s components. Use single or double underscores for private attributes.

#### Example:
```python
class Dog:
    def __init__(self, name):
        self.__name = name  # Private attribute

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

dog = Dog("Buddy")
print(dog.get_name())  # Output: Buddy
dog.set_name("Max")
print(dog.get_name())  # Output: Max
```

---

### **10. Polymorphism**
Allows methods to be used in different ways.

#### Example:
```python
class Animal:
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        print("Woof!")

class Cat(Animal):
    def make_sound(self):
        print("Meow!")

animals = [Dog(), Cat()]
for animal in animals:
    animal.make_sound()
# Output: Woof!
#         Meow!
```

---

### **11. Special (Dunder) Methods**
Special methods have double underscores (e.g., `__str__`, `__len__`).

#### Example:
```python
class Dog:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Dog: {self.name}"

dog = Dog("Buddy")
print(dog)  # Output: Dog: Buddy
```

---

### **12. Property Decorators (`@property`)**
Used to control access to instance attributes.

#### Example:
```python
class Dog:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

dog = Dog("Buddy")
print(dog.name)  # Output: Buddy
dog.name = "Max"
print(dog.name)  # Output: Max
```

---

### **13. Abstract Classes and Interfaces**
Abstract classes cannot be instantiated and are used to define methods that must be implemented by subclasses.

#### Example:
```python
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        print("Woof!")

dog = Dog()
dog.make_sound()  # Output: Woof!
```

---

### **14. Method Resolution Order (MRO)**
Determines the order in which methods are inherited in the presence of multiple inheritance.

#### Example:
```python
class A:
    def method(self):
        print("A")

class B(A):
    def method(self):
        print("B")

class C(B):
    pass

obj = C()
obj.method()  # Output: B
```

---

### **15. Metaclasses**
Metaclasses are classes of classes and define how classes behave.

#### Example:
```python
class Meta(type):
    def __new__(cls, name, bases, dct):
        print(f"Creating class {name}")
        return super().__new__(cls, name, bases, dct)

class MyClass(metaclass=Meta):
    pass
```

---

### **16. Object Serialization**
Serialization converts an object to a format that can be saved or transmitted.

#### Example:
```python
import pickle

class Dog:
    def __init__(self, name):
        self.name = name

dog = Dog("Buddy")
serialized = pickle.dumps(dog)
print(serialized)

deserialized = pickle.loads(serialized)
print(deserialized.name)  # Output: Buddy
```
