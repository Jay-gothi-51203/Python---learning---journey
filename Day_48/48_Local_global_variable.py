# Topic: Local and Global variable in Python. 

# 1.) Local Variable: A local variable is a variable that is created inside a function and can only be used inside that function.

def greet():
    name = "Anushka" #local variable
    print("Hello, "+ name)

greet() #calling the function

# print("Hello,"+name) #If you are trying to use local variable outside then it will show error like name is not defined.

# You can use message inside the greet() function.
# You cannot use message outside the function.


print("\n")


# 2.) Global Variable: A global variable is a variable that is created outside all functions and can be used everywhere in the code.

Name = "Virat" #global variable

def Greet():
    print("Hello"+Name)

Greet() # calling the function
print("Hello,"+Name) # you can use global variable outside function.

# name can be used inside and outside the function.


print("\n")


# 3.) What is the global keyword?
# The global keyword in Python is used inside a function to tell Python that you want to use (and change) a variable that was created outside the function.

# Why do we need it?
# By default, if you change a variable inside a function, Python thinks you’re creating a new local variable, not changing the one outside.
# The global keyword tells Python:
# "No, I'm not making a new one. I want to use and change the one outside!"


x = 10 # Global Variable

def my_function():
    global x # now we use global keyword to change and use the value of x.
    x = 4 # change the  value of x.
    y = 5 # Local variable 
    print("Local variable: ",y)

print("Gloabl variable before changing: ",x) # print the global variable before changing 

my_function() # calling the function

print("Gloabl variable after changing: ",x) #Print the global variable after changing