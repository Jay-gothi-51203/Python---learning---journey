# Topic: class and object in Python. 


# 1.) What is a Class in Python?
# A class is like a blueprint or a template.
# Think of it like a blueprint for building a house. The blueprint tells you where the rooms are, but it's not a real house. It's just the plan.
# In Python, a class is a blueprint for creating objects.

# Syntax: 
# class ClassName:
        # def __init__ (self, parameters):
        #  self.attribute1 = value1
        #  self.attribute2 = value2

        # def method_name(self):

# self refers to the current object that is calling the method or accessing variables inside a class.
# self means that object for which method is called.

# Example: 
# class Details():
#     Name = "Jay"
#     Occupation = "AI engineer"
#     Networth = "One cr+"
    
#     def describe(self): # Method or function which show what an object can do.
#         print(f"Hello, My name is { self.Name } and I am { self.Occupation } and I have networth of { self.Networth }.")           
    
# my_details = Details() # Create object name "my_details".

# # Object 1
# my_details.describe() # Calling objcet with objectName.MethodName()

# # Object 2
# a = Details() 
# a.Name = "meet"
# a.Occupation = "Backend developer"
# a.Networth = "50 lakh"

# a.describe()



class Details(): # Class name Details 
    Name = "Jay" # attribute1 or parameters1
    Occupation = "AI engineer" # attribute2 or parameters2
    Salary = "One cr+" # attribute3 or parameters3

    def describe(self): # Method name describe
        print(f"My name is { self.Name } and I am { self.Occupation } and my salary is { self.Salary }.")

# Object - 1
my_details = Details() # create the object 

my_details.describe() # calling object by objectName.MethodName() , It will print the default details


# create 2nd object
b = Details()

b.Name = "Meet"
b.Occupation = "Backend developer"
b.Salary = "50 lakh"

b.describe() # calling the object by objectName.MethodName() 


# create 3rd object
c = Details()

c.Name = "Ronak"
c.Occupation = "Frontend developer"
c.Salary = "30 lakh"

c.describe() # calling the object by ObjectName.MethodName()