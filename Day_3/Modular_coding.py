# initiate a class

class Employee:
    # getters and setters
    def get_id(self):
        return self.id
    def set_id(self, id):
        self.id = id


    def __init__(self): # costructor 
        # attributes are variables that belong to the class
        print("Constructor is called")
        self.id = 101
        self.name = "Nawaz"
        self.age = 25
        self.salary = 50000   
        print("Attributes are initialized")

    # method of the class
    def travel(self, destination):
        print("Method is called manually")
        print(f"Employee is travelling to {destination}")

    # static method
    @staticmethod
    def static_method():
        print("Static method is called")
    
    # class method
    @classmethod
    def class_method(cls):
        print("Class method is called") 


# create an object of the class
em1 = Employee() # object of the class

print(em1.travel("India")) # calling the method of the class
# accessing the attributes of the class 



print(em1.id) # accessing the id attribute
print(em1.get_id()) # accessing the id attribute using the getter


em1.set_id(102) # setting the id attribute using the setter
print(em1.id) # accessing the id attribute
print(em1.get_id()) # accessing the id attribute using the getter

#static method calling
Employee.static_method()
em1.static_method()

#encapsulation example
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance
    def get_balance(self):
        return self.__balance
    def set_balance(self, balance):
        self.__balance = balance

account = BankAccount(1000)
print(account.get_balance())
account.set_balance(2000)
print(account.get_balance())

#Explanation of encapsulation:
"""Encapsulation is a mechanism that allows us to hide the implementation details of a class from the outside world.
It is used to protect the data of a class from being accessed or modified by the outside world.
In the above example, the balance attribute is private and cannot be accessed or modified by the outside world.
We can only access it using the get_balance and set_balance methods.
This is how encapsulation is used to protect the data of a class from being accessed or modified by the outside world.      
"""

#Inheritance
class SavingsAccount(BankAccount):
    def __init__(self, balance, interest_rate):
        super().__init__(balance)
        self.__interest_rate = interest_rate
    def get_interest_rate(self):
        return self.__interest_rate
    def set_interest_rate(self, interest_rate):
        self.__interest_rate = interest_rate

savings_account = SavingsAccount(1000, 0.05)
print(savings_account.get_balance())
print(savings_account.get_interest_rate())

#Explanation of inheritance:
"""Inheritance is a mechanism that allows a class to inherit the attributes and methods of another class.
The class that inherits the attributes and methods is called the child class, and the class that is inherited from is called the parent class.
The child class can access the attributes and methods of the parent class.
In the above example, the SavingsAccount class inherits the attributes and methods of the BankAccount class.
The SavingsAccount class can access the attributes and methods of the BankAccount class.
"""


#polymorphism
class Animal:
    def make_sound(self):
        print("Animal makes a sound")
class Dog(Animal):
    def make_sound(self):
        print("Dog barks")
class Cat(Animal):
    def make_sound(self):
        print("Cat meows")
dog = Dog()
cat = Cat()
dog.make_sound()
cat.make_sound()

#Explanation of polymorphism:
"""Polymorphism is a mechanism that allows us to use the same interface to work with different data types.
In the above example, the make_sound method is used to make the sound of the animal.
The Dog and Cat classes inherit the make_sound method from the Animal class.
The Dog and Cat classes can make the sound of the animal.
"""


#Abstraction
class Animal:
    def make_sound(self):
        print("Animal makes a sound")
class Dog(Animal):
    def make_sound(self):
        print("Dog barks")
class Cat(Animal):
    def make_sound(self):
        print("Cat meows")
dog = Dog()
cat = Cat()
dog.make_sound()
cat.make_sound()

#Explanation of abstraction:
"""Abstraction is a mechanism that allows us to hide the implementation details of a class from the outside world.
It is used to protect the data of a class from being accessed or modified by the outside world.
In the above example, the make_sound method is used to make the sound of the animal.
The Dog and Cat classes inherit the make_sound method from the Animal class.
The Dog and Cat classes can make the sound of the animal.
"""



# interview questions:
"""
1. What is a class?
A class is a blueprint of an object. It defines the attributes and methods that an object can
have.
2. What is an object?
An object is an instance of a class. It is created using the class and can access the
attributes and methods of the class.
3. What is a constructor?
A constructor is a special method that is called when an object is created. It is used to
initialize the attributes of the class.
4. What is self?
Self is a reference to the current object. It is used to access the attributes and methods of
the class.
5. What is an attribute?
An attribute is a variable that belongs to the class. It is used to store the state of theobject.
6. What is a method?    
A method is a function that belongs to the class. It is used to define the behavior of theobject.
7. How can we access the attributes and methods of a class?
We can access the attributes and methods of a class using the object. We can use the dot
operator to access the attributes and methods of the class.
8. Can we create multiple objects of the same class?
Yes, we can create multiple objects of the same class. Each object will have its own
attributes and methods.
9. Can we modify the attributes of a class using the object?
Yes, we can modify the attributes of a class using the object. We can use the dot operator
to access the attributes and modify them.
10. Can we call the methods of a class using the object?
Yes, we can call the methods of a class using the object. We can use the dot operator tocall the methods of the class.
11. Can we create multiple classes in a single file?
"""

"""important points:
when we create an object of the class, the constructor is called automatically. 
because the constructor is called when the object is created, we can use it to initialize the attributes of the class.example: when we create an object of the class, the id, name, age and salary attributes are initialized.
when we run facebook or instagram, the constructor is called automatically and the attributes are initialized like the username, password, email, etc."""

"""Any data type in python is also a class. 
For example, int, str, list, dict, etc. are all classes in python.
object of list class is created when we create a list.
object of dict class is created when we create a dictionary.
example:
my_list = [1, 2, 3] # object of list class is created
my_dict = {"name": "Nawaz", "age": 25} # object of dict class is created"""

"""Open source contribution using oop, in python when we write 
a = 'x'
b = 'y'
print(a + b) 

# it returns xy but i algebraically it is not correct. correct should be return x+y.
# so we can create a class and override the __add__ method to return x+y
class MyString(str):
    def __add__(self, other):
        return f"{self} + {other}"
a = MyString('x')
b = MyString('y')
print(a + b)  # it will return x + y
# this is how we can contribute to open source projects using OOP in python.
# we can also create a class for a list and override the __add__ method to return the sum of the two lists.
class MyList(list):
    def __add__(self, other):
        return [x + y for x, y in zip(self, other)]
        a = MyList([1, 2, 3])
        b = MyList([4, 5, 6])
        print(a + b)  # it will return [5, 7, 9     
        # this is how we can contribute to open source projects using OOP in python.
        # we can also create a class for a dictionary and override the __add__ method to return the sum of the two dictionaries.
class MyDict(dict):
    def __add__(self, other):
        return {k: self.get(k, 0) + other.get(k, 0) for k in set(self) | set(other)}
        a = MyDict({'a': 1, 'b': 2})
        b = MyDict({'b': 3, 'c': 4})
        print(a + b)  # it will return {'a': 1, 'b: 5, 'c': 4}  
# this is how we can contribute to open source projects using OOP in python.
"""


# function vs method:
"""A function is a block of code that performs a specific task. It can be called from anywhere in
the program. A method is a function that belongs to a class. It can only be calledusing an object of the class.
A function is defined using the def keyword, while a method is defined inside a class. A function can       
take any number of arguments, while a method can take only one argument, which is self. A function can return any value, while a method can return only one value, which is the object itself.  
A function can be called without creating an object of the class, while a method can only be called using an object of the class. A function can be defined outside a class, while a method can only be defined inside a class. A function can be used to perform any task, while a method is used to define the behavior of an object.
""" 
# what are magic methods?
"""Magic methods are special methods that are defined in a class. They are used to define the behavior of an object. They are also known as dunder methods, because they are defined using double underscores before and after the method name. For example, __init__ is a magic method that
is used to initialize the attributes of a class. Other examples of magic methods are __str__, __repr__, __add__, __sub__, __mul__, __truediv__, __floordiv__, __mod__, __pow__, __lt__, __le__, __eq__, __ne__, __gt__, and __ge__.
Magic methods are used to define the behavior of an object when it is used with operators, such as +, -, *, /, //, %, **, <, <=, ==, !=, >, and >=. For example, if we want to define the behavior of an object when it is used with the + operator, we can define the __add__ magic method in the class. 
When we use the + operator with an object of that class, the __add__ method is called automatically.    
Magic methods are used to define the behavior of an object when it is used with built-in functions, such as len(), str(), repr(), and type(). For example, if we want to define the behavior of an object when it is used with the len() function, we can define the __len__ magic method in the class. When we use the len() function with an object of that class, the __len__ method is called automatically.
"""

# what is inheritance?
"""Inheritance is a mechanism that allows a class to inherit the attributes and methods of another class. The class that inherits the attributes and methods is called the child class, and the class that is inherited from is called the parent class. The child class can access the attributes and methods of the parent class.
Inheritance is used to create a new class that is a modified version of an existing class. For example, if we want to create a new class that is a modified version of the Employee class, we can create a new class called Manager that inherits the attributes and methods of the Employee class. The Manager class can have additional attributes and methods that are specific to the Manager class.
    """