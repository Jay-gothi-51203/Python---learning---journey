# Topic: is vs == in Python. 

# 1.) "==" : Checks if values are the same
# This checks if two variables have the same value.

# Example - 1:
a = 5
b = 5

print(f"{a} equal to {b}: ",a == b)
# Output: True 
print(f"{a} is {b}: {a is b}")  # Output: True 


# Example - 2:
a = [1, 2, 3, 4, 5]

b = [1, 2, 3, 4, 5]

print(f"{a} equal to {b}:",a == b) 
# Output: True


print("\n")

####################################


# 2.) is : Checks if they are the same object in memory
# This checks if two variables point to the exact same object (same memory location).

# Example - 1:
a = 5
b = a

print(f" {a} is {b}:",a is b)

# Example - 2:
a = [1, 2, 3, 4, 5]

b = a

print(f"{a} is {b}: ",a is b) # Output: True because both point to the same object

print(a == b) # Output: False → different objects, even if values are same