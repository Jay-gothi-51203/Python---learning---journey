# Topic: Dictionary Methods in Python.

# Dictionary mthods: Python gives us some built-in methods to work with dictionaries.

# 1.) get(): Used to get the value of a key. If the key doesn’t exist, it returns None or a default value you provide.

person = {
    "name":"Jay Patel",
    "age": 21,
}

print(person.get("name")) # Output = Jay Patel
print(person.get("age"))  # Output = 21
print(person.get("city")) # Output = None


print("\n")

# 2.) keys (): Returns all the keys in the dictionary.

person = {
    "name":"Jay Patel",
    "age": 21,
}

print(person.keys())
# Output: 


print("\n")

# 3.) values() : Returns all the values in the dictionary.
person = {
    "name":"Jay Patel",
    "age": 21,
}

print(person.values())
# Output: dict_values(['Jay Patel', 21])


print("\n")

# 4.) items(): Returns all key-value pairs as tuples.
person = {
    "name":"Jay Patel",
    "age": 21,
}

print(person.items()) 
# Output: dict_items([('name', 'Jay Patel'), ('age', 21)])


print("\n")

# 5.) update(): Adds new key-value pairs or updates existing ones.
person = {
    "name":"Jay Patel",
    "age": 21,
}

person.update({"City":"Bengluru"})
print(person)


print("\n")

# 6.) pop(): Removes a key and returns its value.
person = {
    "name":"Jay Patel",
    "age": 21,
    "city": "Bengluru"
}

person.pop("name")

print(person)


print("\n")

# 7.) clear(): Removes all items from the dictionary.
person = {
    "name":"Jay Patel",
    "age": 21,
    "city": "Bengluru"
}

person.clear()

print("Clear dictionary: ",person)


print("\n")

# 8.) copy(): Creates a copy of the dictionary.
person = {
    "name":"Jay Patel",
    "age": 21,
    "city": "Bengluru"
}

new_person = person.copy()
new_person.update({"Fav fruits":"mango"})

print("New dicyionary",new_person)


print("\n")

# 9.) setdefault():
# It does two things:
# 1.) If the key already exists, it just returns the value.
# 2.) If the key does not exist, it:
#     Adds the key to the dictionary with the value you give.
#     Returns that new value.

person = {
    "name":"Jay Patel", # if the name did't exist then it will print bob
    "age": 21,
}

person.setdefault("name","bob")

print(person)

