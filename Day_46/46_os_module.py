# Topic: OS module in Python.

# What is the os module in Python?
# The os module in Python lets your program interact with the operating system — like Windows, Mac, or Linux.
# or 
# os is a built-in module in Python that helps your Python code talk to your computer's files and folders

# Imagine this:
# You are using your computer. You can:
# Open folders
# Create or delete files
# Move to different folders
# See what's inside a folder
# Right?
# Now imagine you want Python to do these things for you — like a robot helper.
# To do that, Python needs a special tool.
# That tool is the os module.


# | Task                 | Code Example                 |
# | -------------------- | ---------------------------- |
# | Get current folder   | `os.getcwd()`                |
# | Change folder        | `os.chdir('path/to/folder')` |
# | List files in folder | `os.listdir()`               |
# | Create a folder      | `os.mkdir('new_folder')`     |
# | Remove a file        | `os.remove('file.txt')`      |
# | Remove a folder      | `os.rmdir('folder_name')`    |
# | Run a system command | `os.system('echo Hello')`    |


# To use it:
# You need to import it first:
# import os

# Then you can call its functions like:
# print(os.getcwd())  # Shows current working directory

# Example - 1:

import os # Import the os module to work with files and folders

# Print the current working directory (the folder where this script is running)
print("Current working directory is:")
print(os.getcwd()) # Shows the full path of the current folder
print("----------------------------------")

# Print the list of files and folders in the current directory
print("Items here:")
print(os.listdir())  # Shows all items (files and folders) in the current directory


print("\n")

# Example - 2:

# import os

# if(not os.path.exists("data")):
#  os.mkdir("data") # It created data folder in the learn_python folder.

# for i in range(1,101):
#     os.mkdir(f"data/Day{i}")

# If the file is already exist it will throw an error but if not exist so it will create data folder and then in that folder it will create Day_1 to Day_100 folders.


# Example - 3: If you want to rename those 100 folders so make like this.

# import os

# for i in range(1,101):
#  os.rename(f"data/Tutorial {i}",f"data/Day - {i}")


# print("\n")

# some real time and regular use os methods.


# 1.) os.getcwd(): Get Current Working Directory
# Shows the folder where your Python script is running.
# Example:
# import os
# print(os.getcwd())


# 2.) os.chdir(path): Changes the current directory to a new one.
# Lets you move to a different folder.
# Example: import os
# os.chdir("C:/Users/MyName/Desktop")
# print(os.getcwd())


# 3.) os.listdir(path='.'):  List Files and Folders
# Shows all files/folders in a folder.

# Example: 
# import os
# print(os.listdir())  # current folder
# print(os.listdir("C:/Users"))  # specific folder


# 4.) os.mkdir('folder_name'): Creates one new folder.
# Save project files in a clean new folder.
# Example: 
# import os
# os.mkdir("NewProject")


# 5.) os.makedirs('folder/subfolder'): Creates folders and subfolders, even if parents don’t exist.
# Organize folders by date or category.
# Example: import os
# os.makedirs("Projects/2025/June/Week1")


# 6.) os.remove('file.txt'): Deletes a file.
# Clean up old or temporary files.
# Example: 
# import os
# os.remove("old_file.txt")  ⚠️ If the file doesn’t exist, it will raise an error.

# import os

# os.remove("addresses.csv")

# this file "addresses.csv" exist before doing that but after that it is gone.


# 7.) os.rmdir('folder_name'): Delete a Folder (must be empty)
# Delete folders after work is finished.
# Example: 
# import os

# os.mkdir("EmptyFolder") # It will create a folder named "EmptyFolder" 

# os.rmdir("EmptyFolder") # It will delete a folder named "EmptyFolder"


# 8.) os.rename('old_name', 'new_name'): Renames a file or folder.
# Rename files to include a date, version, or fix spelling.
# Example: 
# import os
# os.rename("report.txt","final_report.txt")


# 9.) os.path.exists('path'): Checks if a file or folder exists.
# Avoid errors before opening, deleting, or renaming.
# Example:
# import os 

# if os.path.exists("final_report.txt"):
#     print("File found.")
# else:
#     print("File not found")


# 10.) os.system('command'): os.system() is used to run computer commands using Python — just like you're typing in the Command Prompt (Windows) or Terminal (Mac/Linux).

import os

os.system("open -a Photos") #This will open Notepad!

os.system("echo Hello from Python!") # This will print a message in terminal. "Hello from Python!"

os.system("ls") #This shows the list of files in the current folder.

# os.system("clear") # This clears the terminal screen.