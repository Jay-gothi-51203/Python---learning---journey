# Topic: Typles in Python.

# Tuples: Tuples are ordered collection of data items. They store multiple items in a single variable. Tuple items are separated by commas and enclosed within round brackets (). Tuples are unchangeable meaning we can not alter them after creation.

#  A tuple is a collection in Python used to store multiple items in a single variable.

# It is:
# Ordered (items have a defined order)
# Immutable (cannot be changed after creation)
# Allow duplicate values

# It uses Rounded bracket().

# Syntax: my_tuple = (value1, value2, value3, ...)

# Example:

my_tuple = ("apple", 1, 2, 3, True)

print(type(my_tuple)) #Output: <class 'tuple'>
print(my_tuple) # Output: ('apple', 1, 2, 3, True)
print(my_tuple[0]) # Access each element by its index.

print("The length of a tuple: ",len(my_tuple)) #print the length of a tuple.


#######
# Tuple Indexing: Indexing means getting specific items from a tuple using their position number.

things = ("Iphone", "Macbook", "Apple watch", "Ipad", "Airpods")

# Positive index: 
# things = ("Iphone", "Macbook", "Apple watch", "Ipad", "Airpods")
# indexing=    0    ,    1     ,      2       ,   3   ,     4     

print(things[0]) #print 0 index item which is "Iphone"
print(things[4]) #print 4 index item which is "Airpods"


# Range:
print(things[0:3]) #It will print index 0,1,2 because index 3 will not be included.
print(things[:]) #It will print full tuple.

# with a step:
print(things[::2]) #It will go through all iteams in the tuple but skip 2(second) item. means skip 1 and jump on second.

# Negative index:
# things = ("Iphone", "Macbook", "Apple watch", "Ipad", "Airpods")
# Indexing=    -5   ,    -4    ,     -3       ,    -2 ,    -1

print(things[-4]) #It will print index: -4 which is Macbook
print(things[-1]) #It will print index: -1 which is Airpods.

# Range:
print(things[-3:-1]) #It will print index -3, and -2 but not -1 because it is not included.

# with a Step:
print(things[-4:-1:2]) #It will print index -4 and skip index 3and jump to index -2 and -1 is not included.


#################
# To check a item is present or not in the tuple.
things = ("Iphone", "Macbook", "Apple watch", "Ipad", "Airpods")

if "Iphone" in things:
    print("Iphone is present in the tuple.")

if "Laptop" not in things:
    print("Laptop is not in the tuple.")