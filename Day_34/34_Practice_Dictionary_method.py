# Topic: Practice Dictionary methods.

# 1.) get()
# Question:
# Create a dictionary car = {"brand": "Toyota", "year": 2020}.
# Use the .get() method to retrieve the value of "brand" and "model" (which doesn’t exist). Print the results.

car = {
    "brand": "Toyota",
    "year": 2020,
}

print(car.get("brand"))
print(car.get("year"))
print(car.get("model"))

# Output: Toyota
#         2020
#         None


print("\n") ################

# 2. keys() and values()
# Question:
# Given the dictionary student = {"name": "Alex", "age": 22, "grade": "A"},
# print all keys and all values separately using keys() and values().

student = {
    "name": "Alex",
    "age": 22,
    "grade": "A"
    }

print(student.keys())
# dict_keys(['name', 'age', 'grade'])

print(student.values()) 
# dict_values(['Alex', 22, 'A'])


print("\n") ################

# 3.) items()
# Question:
# Given inventory = {"pen": 10, "notebook": 5, "eraser": 3},
# use a for loop with .items() to print each item and its quantity in this format:
# Item: pen, Quantity: 10

inventory = {
    "pen": 10,
    "notebook": 5, 
    "eraser": 3
    }

for keys,values in inventory.items():
    print(f"Item: {keys}, Quantity: {values}")


print("\n") #################

# 4.) 4. update()
# Question:
# You have a dictionary profile = {"username": "jay123", "email": "jay@email.com"}.
# Update it to include "age": 21 using update().

profile = {
    "username": "jay123",
    "email": "jay@email.com"
    }

profile.update({"age" : 21})

print(profile)


print("\n") #################

# 5.) pop()
# Question:
# Given menu = {"burger": 50, "fries": 30, "soda": 20},
# remove "fries" from the dictionary using pop() and print the remaining dictionary.

menu = {
    "burger": 50,
    "fries": 30, 
    "soda": 20
    }

menu.pop("fries")

print(menu)


print("\n") #################

# 6.) popitem()
# Question:
# Given data = {"a": 1, "b": 2, "c": 3},
# remove the last inserted item using popitem() and print the dictionary.

data = {
    "a": 1, 
    "b": 2, 
    "c": 3
    }

data.popitem()

print(data)


print("\n") #################

# 7.) clear()
# Question:
# Create a dictionary with 3 key-value pairs. Then use clear() to remove all items and print the empty dictionary.

data = {
    "a": 1, 
    "b": 2, 
    "c": 3
    }

data.clear()

print("clear() method:",data)


print("\n") #################

# 8.) copy()
# Question:
# Make a copy of this dictionary:
# original = {"fruit": "mango", "color": "yellow"}
# Add a new key "taste": "sweet" to the copied dictionary and print both original and the new dictionary.

original = {"fruit": "mango", "color": "yellow"}

new_dictionary = original.copy()

new_dictionary.update({"taste":"sweet"})

print("Original dictionary:",original)

print("New dictionary:",new_dictionary)


print("\n") #################

# 9.) fromkeys()
# Question:
# Create a dictionary using fromkeys() where keys are ["name", "age", "city"] and all values are set to None.
keys = ["name", "age", "city"]

new_dict = dict.fromkeys(keys,"none")

print(new_dict) 


print("\n") #################

# 10.) Bonus Challenge – All Methods Together
# Question:
# Write a program that:
# Creates a dictionary for a book (title, author, year)
# Makes a copy
# Adds a price to the copied dictionary
# Removes the year
# Prints keys and values separately

book = {
    "title": "The Psychology of Money",
    "author": "Morgan Housel",
    "year": "2020"
    }

new_book = book.copy()

new_book.update({"price":"₹ 283.00"})

new_book.pop("year") 

print("New book:",new_book)


print(new_book.keys())

print(new_book.values())




