# Topic: While loop

# While loop: A while loop is used to repeat a block of code as long as a condition is true.

# Syntax: 
# initialitation like,
#  num = 1
# while condition:
    # code to repeat
    # i+=1 or i-=1 increment or decrement 

# Example:
num = 1
while num<=5:
    print(num)
    num += 1



###############################  Practice Question  #################################
# 1.) Print numbers from 1 to 10:  Use a while loop to print numbers from 1 to 10.
i = 1

while i<= 10:
    print(i)
    i += 1

#####################################

# 2.) Sum of first N natural numbers: Ask the user for a number N, and find the sum of all numbers from 1 to N using a while loop.
N = int(input("Enter the value of n: "))
sum = 0
i = 1

while i<=N:
    sum += i
    i += 1

print("sum is: ",sum)

#####################################

# 3.) Reverese a number: 10 to 1.
number = 10

while number >= 1:
    print(number)
    number -=1

################################
# 4. Guess the number game : Create a simple number guessing game. Set a secret number, and let the user guess until they get it right.

j = 5

k = int(input("Guess the number: "))

while k != j:
    if k < j:
        print("You are too low.")
        break
        
    elif k > j:
        print("You are too high.")
        break

if k == j:
    print("You guess it corrrect.")

#####################################
# 5.) Print hello world whatever the user want.

t = int(input("Enter the number how many time you want to print: "))

i = 1

while i<=t:
    print("Hello world!")
    i+=1


