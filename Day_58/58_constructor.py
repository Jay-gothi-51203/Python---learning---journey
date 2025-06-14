# Topic: Constructor in Python. 


# Constructor: A constructor in Python is a special function that automatically runs when you create an object from a class.

# It's used to set up (initialize) the object with some default values or settings.

# Types of constructor:
# 1.) Default constructor: it wil not take any parameters. 
#        def __init__(self):
     
# 2.) Parameterized constructor: It will take parameters. 
#         def __init__(self, attribute1, attribute2)
#         self.attribute1 = value1
#         self.attribute2 = value2

# Syntax: def __init__(self, attribute1, attribute2):
            #   self.attribute1 = value1
            #   self.attribute2 = value2

# It is automatically called when a new object of a class is created. 

# Example - 1:
class Person:
    def __init__(self, name, occu, salary): # Parameterized constructor
        self.name = name
        self.occu = occu
        self.salary = salary

    # def __init__(self): # This is default constructor. 
    #     print("Thank you")

    def detail(self):
        print(f"My name is {self.name} and I am {self.occu} and my salary is {self.salary}.")

# Create object named "p1" and gives values 
p1 = Person("Jaykumar Gothi", "AI engineer", 90000000) # create object 1#

p1.detail() # calling object by objectName.MethodName()