# TOPICS: Comments, Escape sequences & print statement. 

# In Python, comments are used to add notes or explanations in your code. These notes are not executed by the program, so they don’t affect how the code runs. Comments are there to help you or others understand what the code does.

# 1. Single-line comment:
# A single-line comment starts with a '#' symbol. Everything after '#' on that line is considered a comment.
# Example: 
#This is a single line comments.
print("Hello world!") # This will print hello world.


# 2. Multi-line comment (or docstring):
# If you want to write a longer comment, you can use triple quotes (''' or """).
# Example: 
'''
This is a multi-line comment.
It can take up multiple lines.
'''

"""
This is a multi-line comment.
It can take up multiple lines.
"""

# Why use comments?
# To explain your code: Comments help explain what your code is doing, so others can understand it.

# To help yourself later: If you come back to your code after some time, comments can remind you what you were thinking.

# To turn off code temporarily: You can use comments to "disable" parts of your code while you're testing or fixing things.


############################  Escape Sequences ######################################
# Escape Sequences: Escape sequences are special codes in Python that help you write certain characters in strings that are usually hard to type directly. They start with a backslash (\), followed by another character. This tells Python to do something special.

# Why do we need them ? 
# Sometimes, you want to include characters like new lines, tabs, or quotes in a string, but you can’t just type them normally because Python might get confused. Escape sequences help you tell Python exactly what you mean.

# Common Escape sequence: 

# 1.) " \n " – It is used for Newline. 
# Makes the text jump to a new line.
# Example: 
print("Hello \n world!")  
# Output: Helllo
        # world

# 2.) " \t " – It is used for Tab sapce.
# Adds space like pressing the "Tab" key.
# Example:
print("Hello \t world!")
#Output: Hello     World

# 3.) " \\ " – It is used for Backslash.
# Allows you to use a single backslash (\) in a string.
# Example: 
print("Hello \\ world!")  # Output: Hello \ world

# 4.) " \' ": It is used to add Single Quote.
# Lets you use a single quote (') inside a string that is surrounded by single quotes.
# Example: 
print(" I\' am learning python. ")  #Output: I'am learning python.

# 5.) " \" ": It is used for add double Quotes.
# Lets you use double quotes (") inside a string that is surrounded by double quotes.
# Example: 
print(" He said, \"Python is fun!\" ") #Output: He said, "Python is fun!"


##############################  Print Statements  ###############################
print("hey", 6 , 7, sep = "~" ) # This will print all three hey, 6 and 7 but add '~' Tilde character between all three characters.
# Output: hey~6~7

print("Hello", end = " ") # end = " " is used to "What to print when this print statement will end". You can write anything here " end = " "    ", and it will be printed. 
print("World")


################  PRACTICE QUESTIONS OF ESCAPE SEQUENCES  ###################

# Question 1: Newline (\n)
# Write a Python program that prints your name on the first line, and your age on the second line.
print(" Name: Jay \n Age: 22 ")

# Question 2: Tab (\t)
# Create a Python program that prints the following text:
# But make sure there is a tab space between "Name:" and "John", and between "Age:" and "25".

print(" Name:\t John \n Age: \t 25 ")

# Question 3: Backslash (\\)
# Write a Python program that prints the following file path:
# C:\Users\John
print(" C:\\Users\\John ")

# Question 4: Single Quote (\')
# Write a Python program that prints the sentence: I'm learning Python!
print(" I\'m learning Python! ")

# Question 5: Double Quote (\")
# Write a Python program that prints the following sentence: He said, "Python is amazing!"
print(" He said, \" Python is amazing \" ")


