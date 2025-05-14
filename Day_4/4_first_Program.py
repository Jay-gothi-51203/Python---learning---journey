# Write First Python Program. 

# The print() function is used to show something on the screen.
print("Hello world!")

# You can print:

# 1.) Text: You can write text inside print() function. 
# Example: 
print("Hello Jaykumar Gothi")    #Output: Hello Jaykumar Gothi 

# 2.) Numbers: You can write Numbers inside print() function.
# Example: 
print(5+4)   #Output: 9

# 3.) Variables: You can write variables inside print() function. 
name = "Jay"
print(name)  #Output: Jay

# 4.) Multiple things together: You can write multiple things together. variable name and any other text but write a text in double quotes which you want to display.
# Example: 
name = "Jay"
age = 22

print("Name:", name, "Age:", age)  #Output: Name: Jay , Age: 221
# here Name: and Age: will be displayed that's why we write them in double quotes and also you can write variable names in print() function but don't write in double quotes. 

# What is Script ? -- Script is just a python file that contains  code you want to run. It is usually ends with '.py'. Example: Day04.py, hello.py, etc.

###################    PRACTICE QUESTION    ######################

# 1.) Print your name: 
print("Jay")

# 2.) Print multiple lines:
print("Hello")
print("Welcome to Python")
print("Enjoy coding!") 

# 3.) Print a quote.
# ➤ Print the following sentence using proper quotation marks:
# "Python is fun," she said.

print(' "Python is fun,"she said. ')

# NOTE: if you want to print a line with quotes("") then, use firstly single quotes('') and write a line inside single quotes. like print(' "Hey jay!", How are you ? ') 


# 4.) Print a pattern.
# ➤ Use print statements to make this pattern:
print("*")
print("**")
print("***")
print("****")

# 5.) Print numbers and words.
print("I have 2 apples and 3 bananas.")

# 6.) Print using escape characters.
# Escape characters: in Python are special symbols that allow you to include characters in a string that would otherwise be difficult to type or would have a special meaning.

# The escape character is a backslash (\), and it is used to "escape" the normal behavior of characters. Some common escape sequences are:

# \n - New line: Starts a new line.
# \t - Tab: Adds a tab space (a small indentation).
# \" - Double quote: Allows you to include a double quote inside a string.
# \\ - Backslash: Lets you include a backslash.
print("Name: John \nAge: 25\nLocation: Earth") 

# 7.) Print with tab spaces.
# ➤ Print:  Python\tis\tawesome
# \t is used for tab space.
print("Python\tis\tawesome")

# 8.) Print emojis or special characters: You will use its Unicode escape sequence. 
# How to use unicode: \u and followed by its unicode like \u2764 for heart. 
# ➤ Print this using Unicode:
# I love Python ❤️
print("I love Python \u2764\uFE0F") 
print("This will show you grinning face with smiling eyes.  \U0001F601")