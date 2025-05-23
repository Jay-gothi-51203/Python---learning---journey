# Topic: Calculator by using function in Python.

# Function to perform calculation based on the given operation
def calculator(a, b, operation):
    # Check which operation to perform
    if operation == "+":  # Addition case
        return f"Addition of {a} and {b} is: {a + b}"
    
    elif operation == "-":  # Subtraction case
        return f"Subtraction of {a} and {b} is: {a - b}"
    
    elif operation == "*":  # Multiplication case
        return f"Multiplication of {a} and {b} is: {a * b}"
    
    elif operation == "/":  # Division case
        if b != 0:  # Prevent division by zero
            return f"Division of {a} and {b} is: {a / b}"
        else:
            return "Cannot divide by zero."  # Error message for division by zero
    
    elif operation == "%": # Modulo case
        return f"Modulo of {a} and {b} is: {a%b}" 
    
    elif operation == "**": # Exponentiation case
        return f"{a} raised the power of {b}: {a**b}"
    else:
        return "Invalid operation. Please choose +, -, *, /, %, **."  # Handle unexpected input


try:

    # Ask the user to enter the first number
    a = float(input("Enter the first value: "))

    # Ask the user to enter the second number
    b = float(input("Enter the second value: "))

    # Ask the user to enter the operation
    operation = input("Enter the operation (+, -, *, /, %, **): ")
    # Call the calculator function with the user's inputs and print the result
    print(calculator(a, b, operation))

except ValueError:
    print("Invalid input. Please enter numeric values.")


