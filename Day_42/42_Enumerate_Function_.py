# Topic: Enumerate Function in Python

# Enumerate Function: The enumerate() function helps you get the position (number) of items while looping through a list.

# Example: 
fruits = ["apple","banana","cherry"]

for index,fruit in enumerate(fruits):
    print(index,fruit)

# Output:
#  0 apple
# 1 banana
# 2 cherry


print("\n")

# 2.) use start:
for index,fruit in enumerate(fruits,start=1):
    print(index,fruit)


print("\n")

# Example - 4: 
marks = [10,20,50,70,99,6,9,10]

for index,mark in enumerate(marks):
    print(index,mark)
    if index == 4:
        print("Jay is awesome!")

print("\n")

# Example - 3:
names = ["Jay","Het","Meet","Rahul","Ronak"]

for index,name in enumerate(names):
    print(index,name)