"""
OOP Complete Guide in Python
===========================
This script is a comprehensive, beginner-friendly guide to Object-Oriented Programming (OOP) in Python. It covers all major OOP concepts, SOLID principles, common design patterns, and real-world examples, with detailed explanations and code. At the end, you'll find an interview preparation section.

This guide is designed for absolute beginners. Each section includes:
- Simple explanations and analogies
- Step-by-step code with detailed comments
- Common mistakes and tips
- Quick recaps
"""

# 1. Introduction to OOP
"""
Object-Oriented Programming (OOP) is a way of writing code that is inspired by how we see and interact with the real world.

Imagine you are building a simulation of a zoo. You have animals, cages, zookeepers, and visitors. Each of these can be represented as an object in your code, with their own properties (attributes) and actions (methods).

Key OOP Principles:
- Encapsulation: Keeping data and the code that works on it together, and hiding the details from the outside.
- Inheritance: Passing down traits and behaviors from one class (parent) to another (child).
- Polymorphism: Using the same interface for different underlying forms (e.g., a dog and a cat both can 'make_sound', but the sound is different).
- Abstraction: Focusing on what an object does instead of how it does it.

Why use OOP?
- Organizes code into reusable, logical structures (like building blocks)
- Makes code easier to maintain, extend, and debug
- Models real-world entities and relationships

Tip: OOP is not the only way to write code, but it is very powerful for large, complex, or real-world-inspired programs.
"""

# Quick Recap:
# OOP lets you organize your code like you organize real-world things: by grouping data and actions together.

# 2. Classes and Objects
"""
A class is like a blueprint or recipe. It defines what an object should be like, but it is not the object itself.
An object is an actual thing created using the class blueprint.

Analogy: Think of a class as the blueprint for a house, and an object as the actual house built from that blueprint.
"""
class Car:
    """A simple Car class."""
    def __init__(self, brand, model):
        # The __init__ method is called the constructor. It runs when you create a new object.
        self.brand = brand  # Attribute: the brand of the car
        self.model = model  # Attribute: the model of the car
    def drive(self):
        # Method: an action the car can perform
        print(f"{self.brand} {self.model} is driving.")

# Creating objects (instances) from the Car class
car1 = Car("Toyota", "Corolla")  # car1 is a Toyota Corolla
car2 = Car("Honda", "Civic")      # car2 is a Honda Civic
car1.drive()  # Output: Toyota Corolla is driving.
car2.drive()  # Output: Honda Civic is driving.

# Common mistake: Forgetting 'self' in method definitions or when accessing attributes inside the class.

# Quick Recap:
# - Class = blueprint
# - Object = actual thing created from the blueprint
# - Use __init__ to set up the object when it's created

# 3. Attributes and Methods
"""
Attributes are like the characteristics of an object (e.g., color, size, age).
Methods are like the actions an object can perform (e.g., run, jump, speak).

There are three types of methods:
- Instance methods: Work with a specific object (use 'self')
- Class methods: Work with the class itself (use 'cls')
- Static methods: Utility functions, not tied to object or class
"""
class Person:
    species = "Homo sapiens"  # Class attribute (shared by all instances)
    def __init__(self, name, age):
        self.name = name      # Instance attribute
        self.age = age        # Instance attribute
    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")
    @classmethod
    def species_info(cls):
        print(f"We are {cls.species}.")
    @staticmethod
    def is_adult(age):
        return age >= 18

p = Person("Alice", 30)
p.greet()  # Output: Hello, my name is Alice and I am 30 years old.
Person.species_info()  # Output: We are Homo sapiens.
print(Person.is_adult(20))  # Output: True

# Tip: Use 'self' to refer to the current object, 'cls' to refer to the class.
# Common mistake: Forgetting to use @classmethod or @staticmethod decorators.

# Quick Recap:
# - Attributes = data
# - Methods = actions
# - Use 'self' for instance methods, 'cls' for class methods

# 4. Encapsulation
"""
Encapsulation means keeping the data (attributes) and the code (methods) that works on the data together in one place (the class).
It also means hiding the internal details from the outside world, so users interact only with what you want them to.

Analogy: Think of a TV remote. You can press buttons (methods), but you don't need to know how the remote works inside (attributes are hidden).
"""
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Private attribute (double underscore makes it harder to access from outside)
    def deposit(self, amount):
        self.__balance += amount
    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient funds.")
    def get_balance(self):
        return self.__balance

acct = BankAccount(1000)
acct.deposit(500)
acct.withdraw(200)
print(acct.get_balance())  # Output: 1300
# print(acct.__balance)  # AttributeError: private

# Tip: Use single underscore _var for protected, double __var for private (name mangling)
# Common mistake: Trying to access private attributes directly

# Quick Recap:
# - Encapsulation = keeping data and code together, hiding details
# - Use underscores to control access

# 5. Inheritance
"""
Inheritance lets you create a new class based on an existing class. The new class (child) gets all the features of the existing class (parent), and you can add or change features.

Analogy: A child inherits traits from their parents, but can also have their own unique traits.

Types of inheritance:
- Single: One parent, one child
- Multiple: Multiple parents
- Multilevel: Parent -> Child -> Grandchild
- Hierarchical: One parent, many children
- Hybrid: Combination
"""
# Single Inheritance
class Animal:
    def speak(self):
        print("Animal speaks")
class Dog(Animal):
    def speak(self):
        print("Dog barks")
d = Dog()
d.speak()  # Output: Dog barks

# Multiple Inheritance
class Swimmer:
    def swim(self):
        print("Swimming...")
class Flyer:
    def fly(self):
        print("Flying...")
class Duck(Swimmer, Flyer):
    pass
duck = Duck()
duck.swim()  # Output: Swimming...
duck.fly()   # Output: Flying...

# Multilevel Inheritance
class A:
    def show(self):
        print("A")
class B(A):
    def show(self):
        print("B")
class C(B):
    pass
c = C()
c.show()  # Output: B

# Hierarchical Inheritance
class Parent:
    def hello(self):
        print("Hello from Parent")
class Child1(Parent):
    pass
class Child2(Parent):
    pass
Child1().hello()  # Output: Hello from Parent
Child2().hello()  # Output: Hello from Parent

# Tip: Use super() to call parent methods from child classes.
# Common mistake: Overriding a method and forgetting to call the parent method if needed.

# Quick Recap:
# - Inheritance = child class gets features from parent class
# - Types: single, multiple, multilevel, hierarchical, hybrid

# 6. Polymorphism
"""
Polymorphism means "many forms". It lets you use the same method name for different types of objects, and each object can do something different.

Analogy: The word "run" means different things for a computer program, a car, and a person, but the action is called the same.

Types:
- Method Overriding: Child class changes the behavior of a parent method
- Duck Typing: "If it walks like a duck and quacks like a duck, it's a duck" (Python cares about what an object can do, not its type)
- Operator Overloading: Changing what operators (+, -, etc.) do for your objects
"""
# Method Overriding
class Bird:
    def make_sound(self):
        print("Some sound")
class Sparrow(Bird):
    def make_sound(self):
        print("Chirp chirp")
Bird().make_sound()      # Output: Some sound
Sparrow().make_sound()   # Output: Chirp chirp

# Duck Typing
class Cat:
    def sound(self):
        print("Meow")
class Dog:
    def sound(self):
        print("Bark")
def animal_sound(animal):
    animal.sound()  # Doesn't care if it's a Cat or Dog, just that it has sound()
animal_sound(Cat())  # Output: Meow
animal_sound(Dog())  # Output: Bark

# Operator Overloading
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __add__(self, other):
        # This lets you use + to add two Vectors
        return Vector(self.x + other.x, self.y + other.y)
    def __str__(self):
        return f"({self.x}, {self.y})"
v1 = Vector(1, 2)
v2 = Vector(3, 4)
print(v1 + v2)  # Output: (4, 6)

# Tip: Use polymorphism to write flexible, reusable code.
# Common mistake: Forgetting to implement required methods in child classes.

# Quick Recap:
# - Polymorphism = same method name, different behavior
# - Python uses duck typing: "If it can do it, it's good enough!"

# 7. Abstraction
"""
Abstraction means hiding the complex details and showing only what is necessary.

Analogy: When you drive a car, you use the steering wheel and pedals, but you don't need to know how the engine works.

In Python, you can use the abc module to create abstract classes (classes that can't be used directly, only inherited from).
"""
from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass  # No implementation here
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius ** 2
# shape = Shape()  # Error: Can't instantiate abstract class
circle = Circle(5)
print(circle.area())  # Output: 78.5

# Tip: Use abstraction to define a common interface for related classes.
# Common mistake: Forgetting to implement all abstract methods in child classes.

# Quick Recap:
# - Abstraction = hiding details, showing only essentials
# - Use abc module for abstract classes

# 8. Magic/Dunder Methods
"""
Magic methods (also called dunder methods) are special methods with double underscores before and after their names (e.g., __init__, __str__).
They let you define how your objects behave with built-in functions and operators.

Examples:
- __init__: Constructor (runs when you create an object)
- __str__: String representation (used by print)
- __add__: Addition operator
- __eq__: Equality operator
"""
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    def __str__(self):
        # Called by print(book)
        return f"{self.title} by {self.author}"
    def __eq__(self, other):
        # Called by book1 == book2
        return self.title == other.title and self.author == other.author
b1 = Book("1984", "Orwell")
b2 = Book("1984", "Orwell")
print(b1)         # Output: 1984 by Orwell
print(b1 == b2)   # Output: True

# Tip: Use magic methods to make your classes work naturally with Python's syntax.
# Common mistake: Misspelling magic method names (must be exact).

# Quick Recap:
# - Magic methods = special double-underscore methods
# - Control how your objects behave with operators and built-ins

# 9. Other OOP Concepts
"""
Composition: Instead of inheriting from a class, you can use objects of other classes as attributes. This is called a "has-a" relationship.

Analogy: A car "has an" engine, but a car is not an engine.

Mixins: Small classes that add extra features to other classes via multiple inheritance.
"""
# Composition Example
class Engine:
    def start(self):
        print("Engine started")
class Car:
    def __init__(self):
        self.engine = Engine()  # Car has an Engine
    def start(self):
        self.engine.start()
car = Car()
car.start()  # Output: Engine started

# Mixin Example
class JsonMixin:
    def to_json(self):
        import json
        return json.dumps(self.__dict__)
class User(JsonMixin):
    def __init__(self, name, age):
        self.name = name
        self.age = age
u = User("Bob", 25)
print(u.to_json())  # Output: {"name": "Bob", "age": 25}

# Tip: Prefer composition over inheritance for flexibility.
# Common mistake: Overusing inheritance when composition is better.

# Quick Recap:
# - Composition = "has-a" relationship
# - Mixins = add features to classes

# 10. SOLID Principles
"""
SOLID is a set of five design principles for writing maintainable OOP code:
- S: Single Responsibility Principle (one class = one job)
- O: Open/Closed Principle (open for extension, closed for modification)
- L: Liskov Substitution Principle (child classes should work as parent classes)
- I: Interface Segregation Principle (many small interfaces > one big one)
- D: Dependency Inversion Principle (depend on abstractions, not concrete classes)

Analogy: Think of SOLID as the rules for building strong, flexible LEGO structures.
"""
# S: Single Responsibility Principle
class ReportGenerator:
    def generate(self):
        print("Generating report...")
class ReportPrinter:
    def print_report(self, report):
        print(f"Printing: {report}")

# O: Open/Closed Principle
class Shape:
    def area(self):
        pass
class Rectangle(Shape):
    def __init__(self, w, h):
        self.w = w
        self.h = h
    def area(self):
        return self.w * self.h
class Circle(Shape):
    def __init__(self, r):
        self.r = r
    def area(self):
        return 3.14 * self.r ** 2
shapes = [Rectangle(2, 3), Circle(5)]
for s in shapes:
    print(s.area())

# L: Liskov Substitution Principle
class Bird:
    def fly(self):
        print("Flying")
class Sparrow(Bird):
    pass
class Ostrich(Bird):
    def fly(self):
        raise NotImplementedError("Ostrich can't fly!")
# Good design: Only let flying birds inherit from Bird

# I: Interface Segregation Principle
class Printer:
    def print_doc(self):
        pass
class Scanner:
    def scan_doc(self):
        pass
class MultiFunctionDevice(Printer, Scanner):
    def print_doc(self):
        print("Printing...")
    def scan_doc(self):
        print("Scanning...")

# D: Dependency Inversion Principle
class Backend:
    def fetch(self):
        return "data"
class Service:
    def __init__(self, backend):
        self.backend = backend
    def get_data(self):
        return self.backend.fetch()
service = Service(Backend())
print(service.get_data())

# Tip: SOLID principles help you write code that is easy to change and extend.
# Common mistake: Ignoring SOLID leads to "spaghetti code" (hard to maintain).

# Quick Recap:
# - SOLID = 5 rules for strong, flexible OOP code

# 11. Common Design Patterns
"""
Design patterns are like reusable solutions to common problems in software design.

Examples:
- Singleton: Only one instance of a class exists
- Factory: Create objects without specifying the exact class
- Observer: Notify many objects when one changes
- Strategy: Change the behavior of an object at runtime
"""
# Singleton Pattern
class Singleton:
    _instance = None
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance
s1 = Singleton()
s2 = Singleton()
print(s1 is s2)  # Output: True

# Factory Pattern
class Dog:
    def speak(self):
        return "Woof!"
class Cat:
    def speak(self):
        return "Meow!"
def animal_factory(animal_type):
    if animal_type == "dog":
        return Dog()
    elif animal_type == "cat":
        return Cat()
    else:
        raise ValueError("Unknown animal type")
pet = animal_factory("dog")
print(pet.speak())  # Output: Woof!

# Observer Pattern
class Subject:
    def __init__(self):
        self._observers = []
    def attach(self, observer):
        self._observers.append(observer)
    def notify(self, msg):
        for obs in self._observers:
            obs.update(msg)
class Observer:
    def update(self, msg):
        print(f"Received: {msg}")
subject = Subject()
obs1 = Observer()
obs2 = Observer()
subject.attach(obs1)
subject.attach(obs2)
subject.notify("Hello observers!")

# Strategy Pattern
class StrategyA:
    def execute(self):
        print("Strategy A")
class StrategyB:
    def execute(self):
        print("Strategy B")
class Context:
    def __init__(self, strategy):
        self.strategy = strategy
    def do_something(self):
        self.strategy.execute()
context = Context(StrategyA())
context.do_something()  # Output: Strategy A
context.strategy = StrategyB()
context.do_something()  # Output: Strategy B

# Tip: Learn design patterns to solve common problems efficiently.
# Common mistake: Overusing patterns when a simple solution works.

# Quick Recap:
# - Design patterns = reusable solutions to common problems

# 12. Real-World OOP Example
"""
Let's model a simple Library System using OOP.
This example brings together all the concepts you've learned so far.
"""
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False
class Library:
    def __init__(self):
        self.books = []
    def add_book(self, book):
        self.books.append(book)
    def borrow_book(self, title):
        for book in self.books:
            if book.title == title and not book.is_borrowed:
                book.is_borrowed = True
                print(f"You borrowed {title}")
                return
        print("Book not available")
    def return_book(self, title):
        for book in self.books:
            if book.title == title and book.is_borrowed:
                book.is_borrowed = False
                print(f"You returned {title}")
                return
        print("Book not found")
library = Library()
library.add_book(Book("1984", "Orwell"))
library.add_book(Book("Python 101", "Smith"))
library.borrow_book("1984")
library.return_book("1984")

# Quick Recap:
# - Real-world OOP brings together all the concepts: classes, objects, methods, attributes, encapsulation, etc.

# 13. Best Practices
"""
- Use meaningful class, method, and variable names
- Keep classes focused (Single Responsibility)
- Use docstrings and comments
- Prefer composition over inheritance when possible
- Avoid deep inheritance hierarchies
- Write unit tests for your classes
- Read and follow the Python style guide (PEP8)
"""

# 14. Interview Preparation
"""
Common OOP Interview Questions:
1. What is OOP? List its main principles.
2. Explain encapsulation with an example.
3. What is inheritance? Types?
4. What is polymorphism? How is it implemented in Python?
5. What is abstraction? How do you achieve it in Python?
6. What are magic/dunder methods?
7. Explain SOLID principles.
8. What is the difference between composition and inheritance?
9. What is a design pattern? Name a few.
10. How would you design a real-world system (e.g., Library, ATM) using OOP?

Prepare to:
- Write code for class hierarchies
- Implement encapsulation, inheritance, and polymorphism
- Use abstract classes and interfaces
- Explain and use design patterns

Tips:
- Practice writing code by hand
- Explain your thought process clearly
- Use examples from this guide to illustrate your answers
"""

# End of OOP Complete Guide 