# Topic: for_loop_with_else_in_Python.

# What is a for loop with else?
# A for loop goes through each item in a sequence (like a list), one by one.

# An else block after a for loop runs only if the loop finishes normally, meaning it didn’t stop early by a break statement.

# If a loop successfully finished then the else cause will not print, if loop break then the else cause will print.

# How does it work?
# The for loop runs and checks each item.
# If you use break inside the loop to stop it early, the else part will NOT run.
# If the loop goes through all items without break, then the else part runs.

# Syntax: 
# for item in sequence:
#     # do something with item
#     if some_condition:
#         break  # optional: stops the loop early
# else:
#     # do this if the loop completed without hitting break

# Example: 
numbers = [1,3,5,7,9]

for num in numbers:
    if num % 2 == 0:
        print("even numnber: ",num)
        break
else:
    print("No, even number found in this list.")


# Example:
j = 0
while j<7:
    print(j)
    j+=1
    if j == 4:
     break
else:
    print("out of loop")