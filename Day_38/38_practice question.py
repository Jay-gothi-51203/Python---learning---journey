# Topic: Practice questions of raise custom errors in Python.

# ✅ 1. Negative Age Error: Write a function set_age(age) that:
# Raises a custom error NegativeAgeError if age is less than 0.

class NegativeAgeErroe(Exception):
    pass

def set_age(age):
    if age < 0:
        raise NegativeAgeErroe ("Age can not be negative.")
    else:
        print(f"{age} is valid age.")

age = int(input("Enter your age: "))

set_age(age)


print("\n")

# 2.) Password Too Short: Write a function set_password(password) that:
# Raises a custom error PasswordTooShortError if the password is less than 6 characters long.

class PasswordTooShortError(Exception):
    pass

def set_password(password):
    if len(password) < 6:
        raise PasswordTooShortError("Password must be at least 6 characters long.")
    else: 
        print("Right password.")

password = input("Enter your password: ")

set_password(password)


print("\n")

# 3.) Even Number Only
# Write a function accept_even_number(n) that:
# Raises a custom error NotEvenNumberError if the number is odd.

class NotEvenNumberError(Exception):
    pass

def accept_even_number(n):
    if n % 2 == 0:
        print(f"That's right,{n} is even number.")
    else:
        raise NotEvenNumberError(f"{n} is odd number.")

n = int(input("Enter the number: "))

accept_even_number(n)


print("\n")

# 4.) Divide with Custom Error
# Write a function safe_divide(a, b) that:
# Raises a custom error DivideByZeroError if b == 0
# Otherwise, returns the division result

class DivideByZeroError(Exception):
    pass


def safe_divide(a, b):
    if b != 0:
        print("Result: ",a/b)
    else:
        raise DivideByZeroError("can't divide by zero.")

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))


safe_divide(a,b)


print("\n")

# 5.)  ATM Withdrawal Limit
# Create a function withdraw(amount) that:
# Only allows withdrawing amounts between 100 and 10,000
# Raise custom errors for:
# AmountTooLowError if below 100
# AmountTooHighError if above 10,000


class AmountTooLowError(Exception):
    pass

class AmountTooHighError(Exception):
    pass

def withdraw(amount):
    if amount < 100:
        raise AmountTooLowError("It's too low amount,you can withdraw amuont more than 100 ruppes like 200, 300,etc")

    elif amount > 10000:
        raise AmountTooHighError("It's too high amount,you can withdraw amount less than 10000 ruppes like 9000,8000, etc.")
    else:
        print(f"You withdraw {amount} ruppes from this ATM.")
        print("Thank You for using this ATM. Have a nice day.")

    
amount = int(input("Enter the amount you want to withdraw: "))

withdraw(amount)