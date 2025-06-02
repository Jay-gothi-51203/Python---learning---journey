# Topic: Short hand if else statements

# Short hand if else statements: A shorthand if-else is a way to write an if-else statement in one line.

# Syntax: value_if_true if condition else value_if_false
    

#  Normal if-else example:
# age = 20
# if age >= 18:
#     result = "Adult"
# else:
#     result = "Minor"

# Shorthand version:
age = int(input("Enter the age: "))

print("Age can't be negative.") if age < 0 else print("You are minor.") if age > 0 and age <= 12 else print("You are teenager.") if age >= 13 and age <=19 else print("You are an adult.") if age >= 20 and age <= 60 else print("You are a senior.")

print("You are adult.") if age >= 18 and age < 60 else print("You are minor.") if age < 18 and age >=0 else print("Age can't be negative.") if age < 0 else print("You are senior.")



a = 330
b = 3330

print(f"This is big:{a}") if a > b else print(f"This is big: {b}") if a < b else print("{a} = {b}") 