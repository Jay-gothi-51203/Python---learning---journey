# Topic: List in python.

# List: A list is like a container that can hold multiple items in one place. Think of it like a shopping list – you can write down many things on it.

# You create a list by putting items inside square brackets [ ], separated by commas(,).

# A list can hold anything:
# Numbers: [1, 2, 3
# Strings: ["cat", "dog"]
# Mixed items: ["hello", 5, True]
# Even other lists: [1, 2, [3, 4]]

# Syntax:
# To create a list: my_list = [item1, item2, item3]
# To access a list: list_name[index]

# Example: 
fruits = ["Apple","Banana", "Mango"]
# index = (  0   ,   1    ,   2    )

print(fruits[0])
print(fruits[1])



# List- operation you can.

# 1.) Loop through a list:
for fruit in fruits:
    print(fruit)

# 2.) Length of a list.
fruits = ["Apple","Banana","Mango"]
print(len(fruits))

# 3.) append(): You can add iteam at last in the list.
fruits = ["Apple","Banana","Mango"]
fruits.append("kiwi")
print(fruits)

# 4.) insert(): you can add item at the specific position in the list.
fruits = ["Apple","Banana","Mango"]
fruits.insert(1,"kiwi")
print(fruits)

# 5.) Remove(): you can remove specific element whatever element you want.
fruits = ["Apple","Banana","Mango","kiwi"]
fruits.remove("kiwi")
print(fruits)

# 6.) pop(): you can remove last item of the list.
fruits = ["Apple","Banana","Mango"]
fruits.pop()
print(fruits)

# 7.) in or not in operators : Check if Item Exists
fruits = ["Apple","Banana","Mango"]

if "Apple" in fruits:
    print("Yes, Apple is in the list!") 

if "kiwi" not in fruits:
    print("No, kiwi is not in the list!")

