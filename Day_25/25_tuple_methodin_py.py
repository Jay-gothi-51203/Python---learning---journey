# Topic: Tuples methods in Python.

# Tuple method: A tuple method is a built-in function that you can use on a tuple to do something with or to its items.

# Tuples are immutable, hence if you want to add, remove or change tuple items, then first you must convert the tuple to a list. Then perform operation on that list and convert it back to tuple.

countries = ("Spain", "Italy", "India", "England", "Germany")
temp = list(countries)      # Convert tuple into list.
temp.append("Russia")       #add item 
temp.pop(3)                 #remove item        
countries = tuple(temp)    # Convert list into tuple 
print(countries)

# Output: ('Spain', 'Italy', 'India', 'Germany', 'Russia')


########
# Tuple concatenation:
countries_1 = ("Spain", "Italy", "India", "England", "Germany","Russia", "Isreal","Australia")

countries_2 = ("sri lanka","Japan","Canada","Bhutan")

print(countries_1 + countries_2)

# 👉 Since tuples can't be changed, there are only a few methods available.

# 1.) count() – Tells how many times a value appears.

my_tuple = (1,2,3,4,5,2,2)

print("2 appears this times in tuples: ",my_tuple.count(2))
#output: 3

# 2.) index() – Tells the position of the first time a value appears.

# find or tell the index of a value.

print("The index of 5 is: ",my_tuple.index(5))