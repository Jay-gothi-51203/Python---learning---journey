# Topic: File Handling in Python.

# File Handling: File handling in Python means working with files—like opening, reading, writing, and closing them—using Python code.


# Why use file handling?
# To store data permanently (not just while the program runs).
# For example:
# Save a user's score in a game
# Store login info
# Read content from a text file


# | Operation | Description                       |
# | --------- | --------------------------------- |
# | `open()`  | Open a file                       |
# | `read()`  | Read data from a file             |
# | `write()` | Write data to a file              |
# | `close()` | Close the file after work is done |


# modes:
# | Mode  | Description                       |
# | ----- | --------------------------------- |
# | `"r"` | Read (default)                    |
# | `"w"` | Write (creates new or overwrites) |
# | `"a"` | Append (adds at the end)          |
# | `"x"` | Create (fails if file exists)     |
# | `"b"` | Binary mode (e.g. for images)     |
# | `"t"` | Text mode (default)               |


# 1.) Opening a File: If the file is exist then it will open it otherwise it will give an error.

# syntax: file = open("filename.txt", "mode")

# example - 1:
# file = open("roadmap.py","r")


print("\n")

# 2.) Reading a File:

# Syntax:
# file = open("filename.txt", "r")
# content = file.read()         # reads the whole file
# line = file.readline()        # reads one line
# lines = file.readlines()      # reads all lines into a list
# file.close()


# file = open("roadmap.py","r")
# content = file.read()
# print(content)
# file.close()

# Other reading methods
# readline() – Reads one line
# readlines() – Reads all lines into a list


print("\n")

# 3.) Writing a File: This will overwrite existing content.

# Creates a new file if it doesn’t exist.
# Overwrites the file if it already exists.
# Deletes all existing content before writing new data.

# Syntax: 
# file = open("filename.txt", "w")
# file.write("Hello World!")
# file.close()


file = open("Myfile.txt","w")

file.write("Hello, There is Python")

file.close()


print("\n")


# 4.) Appending to a File:
# Creates a new file if it doesn’t exist.
# Keeps the existing content.
# Adds new data at the end of the file

# Syntax: 
# file = open("filename.txt", "a")
# file.write("\nNew line added.")
# file.close()


# Example: 
file = open("example.txt","a")

file.write("Hello ")


print("\n")

# 5.) with statements: The with statement is a shortcut for opening a file and automatically closing it after you're done.
# Normally, when you open a file, you need to manually close it like this:

# Syntax:
#  with open("filename", "mode") as file:
    # Do something with the file

# Example: 
with open("example.txt", "r") as file:
    # content = file.read()
    print(file.read())


# 6.) create mode: If the file is not exist it will create it otherwise give an error.

# file = open("jay.txt","x")


with open("sample.txt","a") as file:
    file.write("Jay is awesome")