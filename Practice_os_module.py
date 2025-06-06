# Topic: Practice OS module in Python


# 1.) List All Files and Folders
# Write a script that lists all files and folders in the current working directory.
import os

print("List of files and folders: ",os.listdir())


print("\n")

# 2.) Get Current Working Directory
# Print the current working directory using os.getcwd().
import os

print("currentdirectory is: ",os.getcwd())


print("\n")

# 3.) Change Directory
# Change to a specified directory using os.chdir(), and print the new current working directory.
import os

# os.chdir("C:/Users/MyName/Desktop")
# print("Changed directory to:", os.getcwd())



print("\n")

# 4.) Check Path Existence
# Ask the user to input a path and check if it exists using os.path.exists().
import os

if os.path.exists("Day_46"):
    print("File found!")
else:
    print("File not found!")


print("\n")

# 5.) Create a New Directory
# Create a directory named "PracticeOS" in the current working directory using os.mkdir().

import os

# os.mkdir("PracticeOS")


print("\n")

# 6.) Rename a File or Folder
# Rename an existing file or directory to a new name using os.rename().
import os

# os.rename("PracticeOS","Practice OS")


print("\n")

# 7.) Delete a File and Directory
# Safely delete a file with os.remove() and a directory with os.rmdir() (handle cases where the file/directory doesn't exist).
import os

os.remove("data")