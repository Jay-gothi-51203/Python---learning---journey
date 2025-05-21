# Topic: Docstring and PEP - 8 
# (frequently asked in the interview)

# Docstring: Python docstrings are the string literals that appear right after the definition of a function, method, class, or module.

#  A docstring (short for documentation string) is a special kind of comment in Python that you write to explain what your code does.

# It's written using triple quotes (""" ... """ or ''' ... ''').
# You can read a function’s docstring using this: print(greet.__doc__)
# It helps you and others understand your code when you come back to it later.

# Example: 
def square(a):
    '''Takes in a as number and return the square of a'''
    return a*a

a = int(input("Enter the number: "))

print(f"square of {a} is: {square(a)}")
#Output: square of 5 is: 25

print(square.__doc__) 
#Output: Takes in a as number and return the square of a


# Why use docstrings?
# Helps you remember what your code is supposed to do.
# Makes your code easier for others to read.
# Tools like IDEs and documentation generators can show these docstrings automatically.


# |      Feature           |        Comments          |               Docstrings                    |
# | ---------------------- | ------------------------ | ------------------------------------------- |
# |  What is it?           | Notes for the programmer | Description of a function/class/module      |
# |  Why use it?           | To explain code          | To explain what the function or class does  |
# |  How to write?         | Starts with `#`          | Written inside triple quotes `""" ... """`  |
# |  Where used?           | Anywhere in the code     | At the beginning of a function/class/module |
# |  Read/Used by Python?  | No, Python ignores it    | Yes, saved as part of the code              |
# |  Can be accessed?      | No                       | Yes, using `. __doc__`                      |

