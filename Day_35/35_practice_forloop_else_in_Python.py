# Practice for loop with else in Python.

# 1.) Find a vowel
# Write a program that checks if a given string contains any vowel (a, e, i, o, u).
# If a vowel is found, print "Vowel found!" and stop searching.
# If no vowels are found, print "No vowels found."

# word = input("Enter the word: ")

# vowel = ["a","e","i","o","u"]

# for char in word:
#     if char in vowel:
#         print("Yes,vowels found.")
#         break
# else:
#     print("No,vowels not found.")


print("\n")

# 2.) Check if all numbers are positive
# Given a list of numbers, check if all are positive.
# If a negative number is found, print "Negative number found!" and stop.
# If all numbers are positive, print "All numbers are positive."

# numbers = [1,2,3,4,5,6,7,8,9,10]

# for num in numbers:
#     if num < 0:
#         print("Negative number found.")
#         break

# else:
#     print("All numbers are positive.")


print("\n")

# 3.) Prime number check
# Write a program that checks if a number is prime.
# Try dividing the number by every integer from 2 up to the number - 1.
# If divisible by any number, print "Not prime" and stop.
# Otherwise, print "Prime number".

# num = int(input("Enter a number: "))

# if num < 2:
#         print(f"{num} is not a prime number.")
#         exit()

# for i in range(2,num):
#     if num % i == 0:
#         print(f"{num} is not a prime number.")
#         break
# else:
#     print(f"{num} is a prime number.")


print("\n")

# 4.) Find a missing number
# Given a list of numbers from 1 to 10, but one number is missing.
# Write a program to find and print the missing number using a for ... else loop.
# If no numbers are missing, print "No numbers missing."

list_numbers = [1,2,3,4,5,7,8,9,10]

correct_number = [1,2,3,4,5,6,7,8,9,10]

for n in correct_number:
    if n not in list_numbers:
        print(f"{n} number is missing.")
        break

else:
    print("No number is missing.")


print("\n")

# 5.) Password checker
# Given a password string, check if it contains at least one digit (0-9).
# If a digit is found, print "Valid password" and stop.
# Otherwise, print "Password must contain a digit."

password = input("Enter your password: ")

number = [0,1,2,3,4,5,6,7,8,9]

for p in password:
    if p.isdigit():
        print("Valid password")
        break
else:
    print("Not valid password")