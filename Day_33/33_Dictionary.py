# Topic: Dictionary in  Python.

# Dictionary: A dictionary in Python is a type of data that stores information in pairs.
# Each pair has a:
# Key – like a label or name
# Value – the actual data or information


# You can think of a dictionary like a real-life dictionary, where:
# The word is the key
# The definition is the value

# Syntax:
#  dictionary_name = {
#     key1: value1,
#     key2: value2,
#     key3: value3
#  }

# Example: 
person_1 = {
    "Name": "Jay",
    "Age": 21,
    "City": "Bengluru",
    "Favourite_car": "Range Rover Autobiography SV"
}

print(type(person_1))
# it will print the whole dictionary
print(person_1) 

# It will print the the value of "Name": which is "Jay"
# If the key is not present it will throw an error.
print("Name: ",person_1["Name"]) 

#  Using .get() Method:
# If the key is not present it will print none don't give an error.
print("Fav car: ",person_1.get("Favourite_car"))

# If you want to access only keys.
print(person_1.keys())

# If you want to access only values.
print(person_1.values())

# for loop in dictionary:
for keys,values in person_1.items():
    print(f"{keys}:{values}")

# Explanation:
# "Name" is a key, and "Jay" is its value.
# "Age" is a key, and 21 is its value.
# "City" is a key, and "Bengluru" is its value.
# "Favourite_car" is a key, and "Range Rover Autobiography SV" is its value.


# Key Features:
# Keys must be unique
# Values can be anything (numbers, strings, lists, even other dictionaries)
# Dictionaries are written using curly braces {}
# You access values using the key:

# Why Use Dictionaries?
# Because they are great for storing and organizing data that belongs together, like:
# A person's information
# Product details
# Settings/configurations
# Fast lookup by key


# Real-Life Uses of Dictionaries: 
# 1.) Shopping Cart (E-commerce)
# ➤ Store item names and their prices or quantities.
# 2.) User Profile (Web Apps / Social Media)
# ➤ Store user data like name, email, age, and location.
# 3.) Student Grades (School System)
# ➤ Store subjects as keys and marks as values.
# 4.) Weather Report (Weather App)
# ➤ Store city, temperature, and weather condition.
# 5.) Phone Book / Contacts
# ➤ Store names as keys and phone numbers as values.
# 6.) Inventory System (Store / Warehouse)
# ➤ Store product IDs or names and their stock quantity.
# 7.) Configuration Settings (Software / Apps)
# ➤ Store settings like theme, font size, or language.
# 8.) Bank Account Info (Banking App)
# ➤ Store account number, balance, and account holder info.
# 9.) Quiz App / Exam System
# ➤ Store questions as keys and correct answers as values.
# 10.) Employee Records (HR System)
# ➤ Store employee ID as key and details as value.
