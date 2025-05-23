# Topic: Recursion

# Recursion: A function calling itself to solve a smaller version of a problem.

# It’s like breaking a big problem into smaller problems—until it becomes so small it's easy to solve.


# Every recursive function must have:

# 1.) A base case – when to stop.
# The base case is like a stopping point.
# It tells the function: “Stop calling yourself now.”
# 🔁 Without a base case, the function would call itself forever (infinite loop), which would crash your program!

# 2.) A recursive case – where the function calls itself.
# The recursive case is the part where the function calls itself again—but with a smaller or simpler problem.
# So the function is saying: "I can’t solve this yet, let me call myself again with a smaller value."

# Syntax:
# def function_name(parameters):
#     if base_case_condition:
#         return or print base_case_result  # stop recursion
#     else:
#         return or print function_name(modified_parameters)  # recursive call


# Example: 
def countdown(n): #make function name "countdown"
    if n == 0:      # base case
        print("Done!") # it will stop here

    else:
        print(n)
        countdown(n-1) #recursive case

countdown(3) #Function calling 

# How They Work Together: Let’s say you call countdown(3):
# First call: n = 3 → Not base case → prints 3 → calls countdown(2)
# Second call: n = 2 → Not base case → prints 2 → calls countdown(1)
# Third call: n = 1 → Not base case → prints 1 → calls countdown(0)
# Fourth call: n = 0 → YES! base case → prints “Done!” → stops


#################
# Factorial means 5 = 5 * 4 * 3 * 2 * 1 = 120

def factorial(n):
    if n == 0 or n == 1: # base case and if user give 0 and 1 as number it will print below line.
        return 1
    
    else:
        return n * factorial(n - 1) # Recursive case
    

num = int(input("Enter the number: "))

print(f"Factorial of {num} is : ",factorial(num))


# sum of natural numbers from 1 to n
def sum(n):
    if n == 1: #Base case: stop here
        return 1
            
    else:
        return n +  sum(n-1) #recursive case: 
        
num = int(input("Enter the number: "))

print(sum(num))
