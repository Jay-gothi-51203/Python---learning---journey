# Topic: List method 

# List method: List methods in Python are built-in functions that you can use to change or work with lists. They help you add, remove, sort, or find items in a list.

# Example of list:
fruits = ["apple", "banana","mango"]
print(type(fruits))
print(fruits)

# print the items in the list one item in one line with the help of for loop.
# for i in fruits:
#     print(i)

###################### List Method  ########################

# 1.) append: Adds one item to the "end" of the list.

# syntax: list.append(item)

# example:
fruits = ["apple", "banana","mango"]
fruits.append("kiwi")
print("append kiwi: ",fruits)
# Output: append kiwi:['apple', 'banana', 'mango', 'kiwi']


print("\n")

# 2. insert() : Inserts an item at a specific index in the list.

# Syntax: list.insert(index, item)

fruits = ["apple", "banana","mango"]
fruits.insert(1,"kiwi")
print("Insert kiwi at index 1: ",fruits)
# Output: Insert kiwi at index 1: ['apple', 'kiwi', 'banana', 'mango']


print("\n")

# 3.) 3. extend(): The extend() method in Python is used to add elements of one list to the end of another list.
# Adds multiple elements (from another list or iterable) to the end.

#  Syntax: list.extend(iterable) or list.extend(list_2)

# Used when you want to combine two lists or add several elements at once.

fruits = ["apple", "banana","mango"] #List - 1
vegetables = ["tomato","chilli","potato","carrot","Ladies finger"] #List - 2

fruits.extend(vegetables)
print("Extend two lists: ",fruits)
# Output: Extend two lists:  ['apple', 'banana', 'mango', 'tomato', 'chilli', 'potato', 'carrot', 'Ladies finger']


print("\n")

# 4.) reverse(): Reverses the order of the list (not sorting, just reversing the sequence).

# Syntax: list.reverse()

# Changes the list to read backward from its current order.

fruits = ["apple", "banana","mango"]
fruits.reverse()
print("Reverese a list: ",fruits)
# Output: Reverese a list: ['mango', 'banana', 'apple']


print("\n")

# 5.) copy(): Returns a shallow copy of the list.

# Syntax: new_list = list.copy()

# Used to create a copy of a list so changes to the new list don’t affect the original.

fruits = ["apple", "banana","mango"]
newfruits = fruits.copy()
newfruits.append("Orange")

print("Original (old) list: ",fruits)
print("Duplicate (new) list: ",newfruits)
# Output: Original (old) list:  ['apple', 'banana', 'mango']
#         Duplicate (new) list:  ['apple', 'banana', 'mango', 'Orange']


print("\n")

# 6.) clear(): Removes all items from the list.

#  Syntax: list.clear()

# This empties the list completely but keeps the list variable itself.

fruits = ["apple", "banana","mango"]
fruits.clear()
print("Clear() method: ",fruits)
# Output: Clear() method: []


print("\n")

# 7.) pop() : Removes and returns the item at the given index. If no index is specified, it removes the last item.
# or remove last element in the list.

#  Syntax: list.pop(index)  # index is optional

# It's like cutting a specific slice out of the list.

fruits = ["apple", "banana","mango",]
fruits.pop()
print("pop the last element: ",fruits)
# Output: pop the last element: ['apple', 'banana']

fruits = ["apple", "banana","mango",]
fruits.pop(1)
print("pop the specific index element: ",fruits)
# Output: pop the specific index element: 


print("\n")

# 8.) remove(): Removes the specific value from the list.

#  Syntax: list.remove(value)

# Useful for deleting a specific value. If the value is not found, it raises an error.

fruits = ["apple", "banana","mango"]
fruits.remove("banana")
print("remove the specific element: ",fruits)

# Output: remove the specific element:  ['apple', 'mango']


print("\n")

# 9.) count(): count the iteam how many time it appears in the list.

#  Syntax: list.count(value)

# Handy for checking frequency of an item.

fruits = ["apple", "banana","mango","apple"]

print("count() the items how many time is present: ",fruits.count("apple"))
# Output: count() the items how many time is present:  2


print("\n")

# 10.) sort(): Sorts the list in ascending order by default (can also sort descending).

#  Syntax: list.sort()
# list.sort(reverse=True)  # For descending order

# Modifies the original list. For sorting without changing the original list, use sorted() function.

fruits = ["mango", "banana","apple","kiwi"]
fruits.sort()
print("sort the list in acsending order: ",fruits)
# Output: sort the list in acsending order: ['apple', 'banana', 'kiwi', 'mango']

fruits.sort(reverse = True)
print("sort thr list in decending order: ",fruits)
# Output: sort thr list in decending order: ['mango', 'kiwi', 'banana', 'apple']


print("\n")


# 11.) length() : this is used to find length of a list.
fruits = ["apple", "banana","mango"]

print("Length of a list: ",len(fruits))
# Output: Length of a list: 3


print("\n")

# 12.) index(): Returns the index of the first occurrence of the given value.

#  Syntax: list.index(value)

# If the value is found multiple times, it returns the index of the first one. Raises an error if not found.

fruits = ["apple", "banana","mango"]

print("index() method: ", fruits.index("mango"))


