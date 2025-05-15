# Topic: For loop.

# For loop: A for loop is a way to repeat a set of actions for each item in a group of items.

# Syntax:
#  for variable in iterable:
     # code block (indented)

# for – keyword that starts the loop.
# variable – a temporary name used for each item in the loop.
# in – keyword that connects the variable with the iterable.
# iterable – something you can loop through (like a list, string, or range).
# The indented code block runs once for each item.

# Example 1: simple example.
for i in range(5): #here 5 is not included and starting point is not given so start from 0 and end in 4.
    print(i)

# Example 2: If you want to print 1 to 5.
for i in range(1,6): # for loop starts from 1 and goes to 5 not 6 because last one is not included.
    print(i)

# Example 3: explain with list.
fruits = ["apple", "banana", "mango"]

for fruit in fruits:
    print(fruit)


############################# Practice Questions ###########################
# 1.) Basic Looping : Write a for loop that prints the numbers from 1 to 10, each on a new line.
for i in range(1,11):
    print(i)

################################################

# 2.) Sum of Numbers : Write a for loop that calculates the sum of all numbers from 1 to 50 and prints the result.
total_sum = 0

for i in range(1,51):
    total_sum += i
print(total_sum)

#################################################

# 3.) Print Even Numbers : Write a program that prints all even numbers between 1 and 20 using a for loop.
for i in range(2,21): # or you can write this way, for i in range(start,end(not included), step):
    if i % 2 == 0:    #                  like , for i in range(2,21,2):
      print(i)        #                               print(i)

#################################################
# 4.) Loop Through a List : Create a list of five numbers and use a for loop to print each number in the list.

numbers = [2,5,8,12,19]

for num in numbers:
    print(num)

#################################################
# 5.) Count Down : Write a for loop that counts down from 10 to 1, printing each number on a new line.
for j in range(10,0,-1):
    print(j)
