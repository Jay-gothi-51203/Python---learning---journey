# Practice of enumerate function.

# 1.) Practice Question 1:
# You have a list of names: Print each name with its number, starting from 1.

# names = ['Alice', 'Bob', 'Charlie']

names = ['Alice', 'Bob', 'Charlie']

for index,name in enumerate(names,start=1):
    print(index,name)


print("\n")

# 2.) Practice Question 2:  Print only the animals that are at an even position (like 0, 2, 4...) in the list.
# You have a list of animals: animals = ['cat', 'dog', 'elephant']

animals = ['cat', 'dog', 'elephant']

for index,animal in enumerate(animals):
    if index % 2 == 0:
     print(index,animal)


print("\n")

# 3.) You have a list of tasks: Create this output using enumerate():
# Task 1: wake up
# Task 2: brush teeth
# Task 3: eat breakfast
# Task 4: go to school

tasks = ['wake up', 'brush teeth', 'eat breakfast', 'go to school']

for index,task in enumerate(tasks,start = 1):
   print(f"Task {index}: {task}")


print("\n")

# 4.) You have a list of numbers: Print this: "The number at position X is Y"

numbers = [10, 20, 30, 40, 50]

for index,number in enumerate(numbers):
   print(f"The number at position {index} is {number}")
