# Topic: if __name__ == "__main__" in Python

# if __name__ == "__main__": It is used to make sure that some code only runs when the Python file is run directly, and not when it is imported into another file.

# import jay

# jay.hello()

# Output: 
# It will print two times: 
# 1.) Hello from jay.
# 2.) Hello from jay.

# 1st is because of jay.hello() we write in this file and the 2nd time is because of function named hello() in jay.py file. that's why it shows two times "Hello from jay". so in order to solve the problem we use this "if __name__ == "__main__" in the file which you import.

# Example - 1:
import jay

jay.hello()

# Output: 
# Hello from jay. 
# Only one time


#  Think of it like this:
# Imagine your Python file is like a TV show.
# If you run the show directly, it plays the main episode.
# But if someone just imports your show (maybe to watch a clip), you don’t want the full episode to start playing automatically!

#  Why use it?
# It keeps code organized.
# It helps avoid running unwanted code when importing files.
# It’s a common Python best practice.