# initiate a class

class Employee:
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

# create an object of the class
em1 = Employee() # object of the class
# accessing the attributes of the class 
print(em1.id) # accessing the id attribute

print(em1.travel("India")) # calling the method of the class





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
