# Topic: Inheroitence in Python. 


# Inheritence: Inheritance means that one class (called the child or subclass) can use the code from another class (called the parent or superclass).

# It’s like a child inheriting traits (like eye color or height) from a parent — but in programming, it's about inheriting functions and variables.

# Why use inheritance?
# To reuse code (Don’t repeat yourself!)
# To make your code cleaner and more organized
# To make your program easier to extend

class Animal: # Parent class
    def speak(self):
        print("Animal speaks.")
    
class Dog(Animal): # Child class
    def speak(self):
        print("Dog barks.")

class Cat(Animal): # Child class
    def speak(self):
        print("Cat meows.")


# Create object named my_dog and my_cat
my_dog = Dog()
my_cat = Cat()

# calling the object by objectName.MethodName()
my_dog.speak() 
my_cat.speak()