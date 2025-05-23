# Topic: Set in Python.

# Set: In Python, a set is a built-in data type that is used to store a collection of unique items.

# Example: Think of it like a bag of things where no item is repeated.

# It can store any type of data type. like int , float, string, booleancetc.
# Key Features of a Set:
# Unordered: The items don’t have a fixed order.
# No duplicates: Each item in a set is unique.
# Changeable: You can add or remove items.

# Syntax: 
# 1.) Using Curly Braces {}: my_set = {item1, item2, item3, ...}

# 2.) Using the set() Function: 
# set_name = set(iterable)
# The iterable can be a list, tuple, string, etc.
# This is useful when you want to convert another data type into a set.

# Example:
# set_name = set([1, 2, 3, 4])   # from a list


# Example:
# Example 1:
my_Set = {1,2,3,4,5}

print(type(my_Set))
print(my_Set)

# Example 2:
your_set = {"Virat kohli","Ms Dhoni","Rohit Sharma","Hardik pandya"}

print(type(your_set))
print(your_set)

# 2.) 
my_set = set([1,2,3,4,5])

print(type(my_set))
print(my_set)

MY_SET = set(["Virat Kohli", "Msdhoni","Rohit sharma","Hardik Pandya"])
print(type(MY_SET))
print(MY_SET)

# Important Notes:
# To create an empty set, you must use set(), because {} creates an empty dictionary, not a set.
harry = set()
print(type(harry))
print(harry)


# How to access set iteams:
MY_SET = set(["Virat Kohli", "Msdhoni","Rohit sharma","Hardik Pandya"])

for iteam in MY_SET:
    print(iteam)
