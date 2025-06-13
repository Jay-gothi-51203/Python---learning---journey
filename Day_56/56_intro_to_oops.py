# Topic: Oops in Python. 


# Object-Oriented Programming (OOP) is a way of writing programs using objects and classes.
# OOP means writing your code in a way that works with objects — just like real things in the world.

# It helps you:
# Organize code better
# Reuse code easily
# Make big programs easier to manage


# Think of a car:
# A car has things or features like (color, brand, model)
# A car can do things like (start, stop, move)

# In the same way, in OOP:
# Features = Properties (also called attributes)
# Things it does = Methods (also called functions)


# Key Concepts of OOPs: 

# 1.) class: it is like blueprint or template.
# Example: Imagine a class Car. It tells what a car has (color, model) and what it can do (drive, stop).
class Car:

    def __init__(self, model, color): # constructor which automatically called when new objcet of a class is created.
        self.model = model
        self.color = color

    def drive(self):
        print(f"I have {self.model} and it's color is {self.color}.")


# 2.) objcet: An object is a real thing made using the class.
# Example: You can create many car objects from the Car class

my_car = Car("Range Rover SV", "black") # Create object name my_car 

my_car.drive() 


# 3.) constructor (__init__) : This is a special function used to initialize (start) the object with some values.
# It runs automatically when you make a new object. It sets the values like brand and color
# self → It means "this object"
# It is used inside the class to refer to the current object.

# example: 
# class Car:
#     def __init__(self, color, model):
#         self.color = color
#         self.model = model


# 4.) Methods: These are functions inside the class. They define what the object can do.
# example: it is like a car can drive, stop, honk 

# class Car:

#     def __init__(self, model, color):
#         self.model = model
#         self.color = color
    
#     def drive(self): # This is a method. 
#         print(f"I have {self.model} and it's color is {self.color}")

# my_car = Car("Range rover autobiography","black")

# my_car.drive()


# 4 pillars of oops: 
# 1.) Encapsulation – Keeping data safe inside the object
# 2.) Inheritance – One class can use things from another class
# 3.) Polymorphism – One name, many forms
# 4.) Abstraction – Hiding unnecessary details
