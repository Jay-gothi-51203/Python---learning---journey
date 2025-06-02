# Topic: Practice question.

# 1.) Check if a number is even or odd:
print("The program is to find whether a number is even or odd.")

number = int(input("Enter the number: "))

print(f"{number} is even.") if number % 2 == 0 else print(f"{number} is odd.")

print("\n")

# 2.) Find the greater of two numbers:
print("The program is to find the greater of two number.")

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

print(f"{a} is greater than {b}.") if a > b else print(f"{b} is greater than {a}.") if a < b else print(f"{a} is equal to {b}")
# print if_condition else print if_condition else print.

print("\n")

# 3.) Check if someone passed or failed
print("The program is to find the greater of two number.")

marks = int(input("Enter the marks: "))

print("")