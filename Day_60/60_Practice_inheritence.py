# Topic: Practice of inheritence.


# 1.) Basic Inheritance
# Create a class Person with attributes name and age, and a method greet().
# Then, create a class Student that inherits from Person and adds a new attribute student_id.

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def greet(self):
#         print(f"The name of the person is: {self.name} and his age is {self.age}.")     

# class Student(Person):
#     def __init__(self, name, age, student_id):
#         super().__init__(name, age)
#         self.student_id = student_id

#     def greet(self):
#         print(f"Hi, I'm {self.name} age {self.age} and my student ID is {self.student_id}")


# my_person = Person("Jay",20)
# my_student = Student("meet",21,25)

# my_person.greet()
# my_student.greet()


print("\n")
#########################################
# 2.) Zoo Animals (Basic Inheritance)
# Create a base class Animal with attributes like name and species.
# Then create two subclasses: Lion and Parrot, each with their own specific method (e.g., roar() for Lion, speak() for Parrot).

# class Animal:
#     def __init__(self, name, species):
#         self.name = name
#         self.species = species
    
#     def speak(self):
#         print("Animal makes sound.")

# class Lion(Animal):
#     def speak(self):
#         print("Lion roars.")

# class Parrot(Animal):
#     def speak(self):
#         print("parrot speaks.")


# my_lion = Lion("Simba", "Panthera leo")
# my_parrot = Parrot("Polly", "Amazon")


# my_lion.speak()
# my_parrot.speak()

print("\n")
#######################################
# 3.) Create a class Vehicle with:
# An attribute max_speed.
# A method display_info() that prints "Vehicle with max speed of {max_speed} km/h".

# class Vehicle: # creating class with the name of "Vehical":
#     def __init__(self, brand, model, max_speed): # Constructor with max_speed attributes.
#         self.brand = brand
#         self.model = model
#         self.max_speed = max_speed

#     def display_info(self): # method name display_info which display or print the information.
#         print(f"I am driving {self.brand} {self.model} and The Vehicle with max speed of {self.max_speed} km/h.") # it will print the statements.
        

# # Create object with my_vehical 
# my_vehicle = Vehicle("Range Rover","Autobiography SV", 300)

# my_vehicle.display_info() # calling the object by ObjectName.MethodName()

print("\n")
#########################################
# 4.) Constructor Inheritance
# Create a class Person with a constructor that takes name and prints it.
# Now create a class Student that inherits from Person and adds a roll_number.
# Use super() to call the parent constructor from the child class.

# class Person:
#     def __init__(self, name):
#         self.name = name
#         print(f"Person Name: {self.name}")
    
# class Student(Person):
#     def __init__(self, name, roll_no):
#         super().__init__(name)
#         self.roll_no = roll_no
#         print(f"Roll No: {self.roll_no}")
    
# my_student = Student("Alice", 20)


print("\n")
#######################################
# 5.)Add Behavior in Child Class
# Create a base class Vehicle with a method start().
# Create a derived class Car that adds a method open_trunk().
# Create a Car object and call both methods.

class Vehicle:
    def start(self):
        print("vehicle start.")

class Car(Vehicle):
    def open_trunk(self):
        print("Open trunk.")

car = Car()

car.start()
car.open_trunk()


print("\n")
############################################
# 6.) Using super() in Method Overriding
# Create a class Employee with a method work() that prints "Employee works".
# Create a class Manager that overrides work() and also calls the base class’s work() method using super().

class Employee:
    def work(self):
        print("Employee works.")

class Manager(Employee):
    def work(self):
        super().work()
        print("Manager supervise.")


man = Manager()

man.work()


print("\n")
###########################################
# 7.)Inheritance with Default Values
# Create a class Shape with a constructor taking a color parameter, defaulting to 'red'.
# Inherit it into a class Circle that adds a radius parameter.
# Create an object and display the color and radius.

class Shape:
    def __init__(self, color = "red"):
        self.color = color

class Circle(Shape):
    def __init__(self,radius, color="red", ):
        super().__init__(color)
        self.radius = radius

    def display_info(self):
        print(f"Radius: {self.radius}")
        print(f"Color: {self.color}")


my_shape = Shape()
my_circle = Circle(5)

my_circle.display_info()


print("\n")
#############################################
# 8.) Mini Project – Library System
# Create a class Book with attributes title, author, and a method display_info().
# Create a class EBook that inherits from Book and adds a new attribute file_size.
# Override display_info() to include file size in the output.

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    
    def display_info(self):
        print(f"Book title: {self.title}")
        print(f"Book author: {self.author}")
    
class Ebook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = file_size

    def display_info(self):
        super().display_info()
        print(f"File size: {self.file_size} MB.")


my_book = Book('"I am richest person in the world" ','"Jay"')
my_ebook = Ebook('"I am richest person in the world" ','"Jay"',50)

my_book.display_info()
my_ebook.display_info()
        