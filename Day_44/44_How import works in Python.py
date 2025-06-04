# Topic: How to import works in Python.

# import: import is a way to bring code from another file (or module) into your current Python file, so you don’t have to write everything from scratch.


# Think of it like this:
# Imagine Python has a big toolbox. Some tools are already built-in, and others you or someone else can create. The import keyword lets you open the toolbox and use a specific tool (code) from it.

# Example - 1:
import math
print(math.sqrt(16)) #Output: 4.0

# math is a module that comes with Python.
# math.sqrt(16) uses the sqrt (square root) function from that module.
# Output: 4.0

 
# Example - 2:
import math
result = math.sqrt(9)
print(result) 

# Example - 3:
from math import sqrt, pi
result = sqrt(9) * pi
print(result)


print("\n")


# as keyword:  What is as used for in import?
# When you import something in Python, you can use the as keyword to give it a nickname.
# This nickname can be shorter or easier to remember.

# import numpy as np
# numpy is the real name.
# np is the nickname.
# Now you can use np instead of typing numpy every time.

# Example - 1:
import numpy as np

numbers = np.array([1, 2, 3])
print(numbers)


# Example - 2:
from math import sqrt as square_root

print(square_root(16))  # Output: 4.0


print("\n")


# dir function: What is dir() in Python?
# The dir() function shows you a list of things (names) inside an object, module, or even the current program.
# Think of it like opening a toolbox to see what tools are inside.

# Example - 1:
import math
print(dir(math))

print("\n")

# Example - 2:
text = "hello"
print(dir(text))
