# 1.) Create Variables
# Create variables to store your name, age, and whether you are a student (True/False).
Name = "Jay"
Age = 22
Is_student = True

print(Name)
print(Age)
print(Is_student)

# 2.) Type Checking
# Create a variable and print its type using type() function.
print(type(Name))
print(type(Age))
print(type(Is_student))

# 3.) Basic Operations
# Store two numbers in variables. Add, subtract, multiply, and divide them. Print the results.
a = float(input("Enter the first value: "))
b = float(input("Enter the second value: "))

print("Sum of two numbers: ",a+b)
print("Subtraction of two numbers: ",a-b)
print("Multiplication of two numbers: ",a*b)
print("Divison of two numbers: ",a/b)

# 4.) String Formatting:
# Store your name and age in variables and print a sentence like:
# "My name is John and I am 25 years old."
print("My name is ", Name, "and I am ", Age,"years old.")

# 5.) Swap Two Variables
# Write a Python program to swap the values of two variables (without using a third variable).
a = 10 
b = 20 

print("Before swaaping: ")
print("a = ",a)
print("b = ",b)

a , b = b , a # swap the numbers.

print("After swaaping: ")
print("a = ",a)
print("b = ",b)


#################  Slightly challenging  #######################

# 6.) Temperature Converter

# Write a Python script that takes a temperature in Celsius (e.g. celsius = 30) and converts it to Fahrenheit using the formula: F = [C * (9/5)] + 32 

C = float(input("Enter the temperature in Celsius: "))

F = (C * 9/5) + 32

print("Fahrenheit: ", F)

# 7.) Area of a Circle
# Write a program to calculate the area of a circle given the radius. Area = pi * r * r

import math

R = float(input("Enter the radius: "))

Area = math.pi * R * R 

print("Area: ", Area)

# 8.) Data Type Conversion:
# Convert the following string to an integer and add 10 to it:
num_str = "25"

num_int = int(num_str)

add10 = num_int + 10

print("Result after adding 10: ",add10)
print(type(num_str))
print(type(num_int))

# 9.) Boolean Logic
# Create two boolean variables. Use and, or, and not operators to print different outcomes.
a = True
b = False

print( a and b )
print( a or b)
print(not a)
print(not b)

age = int(input("Enter your age to decide you will get a discount or not: "))
if age <= 18 and Is_student :
   print("Yes, you will get a discount.")
else:
   print("No, you will not get discount.")

# 10.) Mix Data Types
# Create a list with different data types: string, int, float, and boolean. Print each item and its type.
my_mixedList = ["Jay", "Apple", "22", "98.99", True , False ]

print(my_mixedList)


