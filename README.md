# Object-Oriented Python Assignment

An advanced Python assignment demonstrating comprehensive understanding of Object-Oriented Programming (OOP) principles, design patterns, and best practices through practical implementation examples.

## Project Overview

This assignment showcases mastery of OOP concepts including encapsulation, inheritance, polymorphism, and abstraction. The project features well-designed classes, proper use of special methods, and practical applications of advanced Python features.

## Tech Stack

- **Python** - 100%

## OOP Concepts Covered

### 1. Classes and Objects
```python
class Student:
    def __init__(self, name, student_id, gpa):
        self.name = name
        self.student_id = student_id
        self.gpa = gpa
    
    def __str__(self):
        return f"Student: {self.name} (ID: {self.student_id})"
```

### 2. Encapsulation
- Private attributes (name mangling with `__`)
- Protected attributes (single underscore `_`)
- Getter and setter methods
- Property decorators

```python
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance
    
    @property
    def balance(self):
        return self.__balance
    
    @balance.setter
    def balance(self, amount):
        if amount > 0:
            self.__balance = amount
```

### 3. Inheritance
```python
class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"
```

### 4. Polymorphism
```python
def animal_sound(animal):
    print(animal.speak())

dog = Dog()
cat = Cat()
animal_sound(dog)  # Output: Woof!
animal_sound(cat)  # Output: Meow!
```

### 5. Abstraction
```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius ** 2
```

### 6. Special Methods
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):  # String representation
        return f"{self.name}, {self.age} years old"
    
    def __repr__(self):  # Official representation
        return f"Person('{self.name}', {self.age})"
    
    def __eq__(self, other):  # Equality comparison
        return self.name == other.name and self.age == other.age
    
    def __lt__(self, other):  # Less than comparison
        return self.age < other.age
    
    def __len__(self):  # Length
        return len(self.name)
    
    def __call__(self):  # Make instance callable
        return f"Hello, I'm {self.name}"
```

## Project Structure

```
Object-Oriented-Python-Assignment/
├── main.py
├── README.md
├── requirements.txt
├── src/
│   ├── __init__.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── animal.py
│   │   ├── student.py
│   │   ├── employee.py
│   │   └── vehicle.py
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── decorators.py
│   │   └── validators.py
│   └── managers/
│       ├── __init__.py
│       └── database.py
└── tests/
    ├── __init__.py
    ├── test_models.py
    └── test_inheritance.py
```

## Core Examples

### Example 1: Vehicle Management System

```python
class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.__mileage = 0
    
    def drive(self, distance):
        self.__mileage += distance
    
    @property
    def mileage(self):
        return self.__mileage
    
    def __str__(self):
        return f"{self.year} {self.brand} {self.model}"

class Car(Vehicle):
    def __init__(self, brand, model, year, num_doors):
        super().__init__(brand, model, year)
        self.num_doors = num_doors

class Motorcycle(Vehicle):
    def __init__(self, brand, model, year, has_sidecar):
        super().__init__(brand, model, year)
        self.has_sidecar = has_sidecar
```

### Example 2: Banking System

```python
class Account:
    def __init__(self, owner, account_number, balance=0):
        self.owner = owner
        self._account_number = account_number
        self.__balance = balance
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return True
        return False
    
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            return True
        return False
    
    @property
    def balance(self):
        return self.__balance

class SavingsAccount(Account):
    def __init__(self, owner, account_number, balance=0, interest_rate=0.02):
        super().__init__(owner, account_number, balance)
        self.interest_rate = interest_rate
    
    def apply_interest(self):
        interest = self.balance * self.interest_rate
        self.deposit(interest)
```

### Example 3: Student Management

```python
class Student:
    def __init__(self, name, student_id, major):
        self.name = name
        self.student_id = student_id
        self.major = major
        self._grades = []
    
    def add_grade(self, grade):
        if 0 <= grade <= 100:
            self._grades.append(grade)
    
    @property
    def gpa(self):
        if not self._grades:
            return 0
        return sum(self._grades) / len(self._grades)
    
    def __str__(self):
        return f"{self.name} ({self.student_id}) - {self.major}"
    
    def __lt__(self, other):
        return self.gpa < other.gpa
```

## Design Patterns Implemented

### 1. Singleton Pattern
```python
class Database:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Database, cls).__new__(cls)
        return cls._instance
```

### 2. Factory Pattern
```python
class ShapeFactory:
    @staticmethod
    def create_shape(shape_type, **kwargs):
        if shape_type == "circle":
            return Circle(kwargs.get("radius"))
        elif shape_type == "square":
            return Square(kwargs.get("side"))
```

### 3. Observer Pattern
```python
class Subject:
    def __init__(self):
        self._observers = []
    
    def attach(self, observer):
        self._observers.append(observer)
    
    def notify(self):
        for observer in self._observers:
            observer.update(self)
```

## Features

- ✅ Multiple inheritance examples
- ✅ Proper use of super()
- ✅ Encapsulation with property decorators
- ✅ Abstract base classes (ABC)
- ✅ Custom exception handling
- ✅ Magic methods implementation
- ✅ Class and static methods
- ✅ Operator overloading
- ✅ Comprehensive documentation
- ✅ Type hints and annotations

## Getting Started

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/prellwitzdarian/Object-Oriented-Python-Assignment.git
cd Object-Oriented-Python-Assignment
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run examples:
```bash
python main.py
```

## Running Examples

Each example can be run independently:

```bash
# Run vehicle example
python examples/vehicle_example.py

# Run banking example
python examples/banking_example.py

# Run student example
python examples/student_example.py
```

## Testing

Run tests to verify implementation:

```bash
pytest tests/
```

Run specific test file:
```bash
pytest tests/test_models.py -v
```

Run with coverage:
```bash
pytest --cov=src tests/
```

## Key Features Demonstrated

### Type Hints
```python
def process_student(student: Student) -> float:
    return student.gpa
```

### Decorators
```python
@property
def name(self):
    return self._name

@classmethod
def create_from_dict(cls, data):
    return cls(**data)

@staticmethod
def validate_email(email):
    return '@' in email
```

### Context Managers
```python
class FileManager:
    def __init__(self, filename):
        self.filename = filename
        self.file = None
    
    def __enter__(self):
        self.file = open(self.filename, 'r')
        return self.file
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()

# Usage:
with FileManager('data.txt') as f:
    data = f.read()
```

### Operator Overloading
```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
```

## Learning Outcomes

This project demonstrates proficiency in:
- Class design and organization
- Inheritance hierarchies
- Polymorphism and method overriding
- Encapsulation and data hiding
- Abstraction with ABC
- Special methods and magic methods
- Property decorators
- Class methods and static methods
- Composition vs. inheritance
- Exception handling
- Type hints and annotations
- Design patterns
- Code organization and modularity
- Testing and validation
- Documentation

## Best Practices Implemented

- ✅ Single Responsibility Principle
- ✅ DRY (Don't Repeat Yourself)
- ✅ SOLID principles
- ✅ Proper naming conventions
- ✅ Comprehensive docstrings
- ✅ Type annotations
- ✅ Error handling
- ✅ Code organization
- ✅ Documentation
- ✅ Testing coverage

## Common Pitfalls Avoided

- ❌ Not using `super()` in subclasses
- ❌ Mutable default arguments
- ❌ Modifying instance attributes directly
- ❌ Poor class naming
- ❌ Circular imports
- ❌ Missing docstrings
- ❌ Inadequate error handling

## Resources

- [Python Official OOP Tutorial](https://docs.python.org/3/tutorial/classes.html)
- [Real Python - OOP](https://realpython.com/object-oriented-programming-oop-in-python-3/)
- [SOLID Principles](https://en.wikipedia.org/wiki/SOLID)
- [Design Patterns in Python](https://refactoring.guru/design-patterns/python)

## Future Enhancements

- [ ] Add more design patterns
- [ ] Implement GUI for examples
- [ ] Create web-based demo
- [ ] Add performance benchmarks
- [ ] Expand test coverage
- [ ] Add type checking with mypy

## License

This project is provided as-is for educational purposes.

## Author

Created by Darian Prellwitz

---

**Last Updated:** May 2026
