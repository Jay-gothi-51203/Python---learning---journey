# Topic: Finally keyword

# finally keyword: The finally block is used with try-except statements in Python. It contains code that will always run, no matter what—whether an error happened or not.

# Why use finally?
# You use finally when you have something that must happen, like:
# Closing a file
# Releasing a resource (like a database connection)
# Printing a message at the end


# Syntax: 
# try:
    # Code that might cause an error
# except SomeError:
    # Code that runs if an error happens
# finally:
    # Code that always runs, no matter what


# Example - 1:
try:
    a = 10
    b = 0

    result = a/b

except:
    print("Oops,can not divide by zero.")

else:
    print("Result: ",result)

finally:
    print("Thank you for use.")


print("\n")

# Example - 2:
def funct1():
    try:
        result = a/b
    except:
        return "Oops, can't divide by zero."
    else:
        return "Result: ",result
    finally:
        return "Thank you for using."


a = int(input("Enter the first value: "))
b = int(input("Enter the second value: "))

print(funct1())

# finally always runs, no matter what.
# It's great for cleanup actions.
# It works with try and except.


#  Where is finally used in real life?
# 1.) Closing a file
# → After reading or writing a file, you must close it.

# 2.) Closing a database connection
# → After using a database, always close the connection.

# 3.) Unlocking something (like a lock)
# → If your program locks something, it should unlock it—even if there's an error.

# 4.) Closing an internet connection
# → If you're connected to a website or API, close the connection when you're done.

# 5.) Deleting temporary files
# → If your program creates temporary files, clean them up at the end.

# 6.) Writing logs or saving progress
# → Save progress or write a message, even if something goes wrong.

# 7.) Turning off hardware (like a camera or printer)
# → Always turn off devices after use.

# 8.) Stopping a background task
# → If something is running in the background, stop it when done.

# 9.) Freeing memory
# → If your program uses a lot of memory, clean it up after use.

# 10.) Showing a final message
# → Show a message like "Done!" or "Goodbye!" no matter what happened.



