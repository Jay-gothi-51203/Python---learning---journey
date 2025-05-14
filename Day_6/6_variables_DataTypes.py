####################  VARIABLES AND DATA TYPE  ####################

####################  VARIABLES   #####################
# In Python, variables are used to store data that you can use and manipulate in your code.

# Think of a variable like a labeled box: you put something in the box (like a number, a string, or even a list), and you give the box a name. Later, you can refer to that name to get what's inside.

# Basic Syntax
# x = 10, here x is a variable that holds the number 10.

# name = "Alice", name holds a string "Alice".

# is_active = True, is_active holds a boolean value True.


# Rules for Naming Variables:
# Can include letters, numbers, and underscores
# Must start with a letter or underscore _
# Are case-sensitive (age and Age are different)



#####################   DATA TYPE   ###########################
# Data type:  A data type is basically the kind of value a variable holds in Python.

# Think of it like this:
# If a variable is a box, then the data type tells us what kind of thing is inside the box—a number, some text, a list of things, etc.

# 1.) Integer (int) : Whole numbers no decimals, like - 98, 99 

x = 9
print("Integer : ", x), print(type(x)) # output: Integer: 9

# 2.) Floating point numbers (Float): numbers with decimals, like - 98.89, 99.99 

y = 98.89
print("Float: ",y), print(type(y)) #output: Float: 98.89, 

# 3.) String: A text in between double quotes(" ") or single quotes (' '), like - "Hello", 'apple', "Jay"
name = "Jay"
print("String: ", name), print(type(name))

# 4.) Boolean (bool): It shows only True / False, On/off, 1/0. 
Is_true = True
Is_false = False
print("Boolean: ", Is_true), print(type(Is_true))

# 5.) List : A list of iteams which you can change it. It uses curly braces {}.
list = [ "apple", "banana", "manago" ] 
print(list), print(type(list))

list_1 = ["apple", 98.89, 99, "Rekha"]
print(list_1), print(type(list_1))

# 6.) Tuple : A list of iteams which you can not change it. It  uses round brackets ().
tuple = ( "apple", "banana", "mango" )
print(tuple), print(type(tuple))

# 7.) Dictionary: It is used to store data in pairs. It uses curly braces {}.
dict = { "Name" : "Jay", "Age": "22", "Gender": "male"}
print(dict), print(type(dict))

# 8.) Set: It is unordered and no duplicates. It uses uses curly braces {}.
set = { 2301031000025, 2301031000035, 2301031000068, 2301031000037 }
print(set)

# 9.) None: It is used to none value to a variable.
D = None
print(D)




