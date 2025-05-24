# Topic: Set methods in Python.

s1 = {1,2,5,6}

s2 = {3,6,7}

print(s1.union(s2))

print(s1.intersection(s2))



# Set methods:

# 1.) add() : Used to add one item to the set
a = {1,2,3,4}
a.add(5)

print("add 5 to the set: ",a)
# Output: add 5 to the set:  {1, 2, 3, 4, 5}


# 2.) remove() : Used to delete a specific item from the set
# If the item is not found, it gives an error.
a = {1,2,3,4,5}
a.remove(4)

print("Remove 4 from set: ",a)
# Output: Remove 4 from set:  {1, 2, 3, 5}


# 3.) discard(): Also removes a specific item
# BUT it does not give an error if the item is not found.
a = {1,2,3,4,5}
a.discard(3)

print("discard 3 from set: ",a)
# Output: discard 3 from set:  {1, 2, 4, 5}


# 4.) clear(): remove all the items from the set.
a = {1,2,3,4,5}
a.clear()

print("clear the set: ",a)
# Output: clear the set:  set()


# 5.) Pop : Removes and returns a random item
# Since sets are unordered, it can remove any item.
# You don't choose the item – Python does.
a = {1,2,3,4,5}

print("pop: ",a.pop())
# Output: pop: 1


# 6.) Union(): Combines two sets. Keeps all unique values.
a = {1,2}
b = {2,3}

print("a union b is:",a.union(b))
# Output: a union b is: {1, 2, 3}


# 7.) intersection () : Gives only the common items from both sets.
a = {1,2,3,5}
b = {3,4,5}

print("a intersection b is: ",a.intersection(b))
# Output: a intersection b is: {3, 5}


# 8.) differnce(): Gives the items that are in the first set but not in the second

a = {1,2,3,4}
b = {2,3,4}

print("diffrence: ",a.difference(b))


# 9.) issubset(): Checks if all items in one set are also in another set.
# Returns True or False
a = {1,2,3,4}
b = {1,2,3,4,5}

print("a's all items are present in b: ",a.issubset(b)) #Output: True
print("b's all items are present in a: ",b.issubset(a)) #Output: False


# 10.) issuperset(): Checks if a set has all the items of another set
a = {1,2,3,4,5}
b = {1,2,3,4}

print("set 'a' has all the items of set 'b': ",a.issuperset(b)) #Output: True
print("Set 'b' has all the items of set 'a': ",b.issuperset(a)) #Output: False


# 11.) symmetric_difference = give those values which are not common in two sets.
a = {1,2,3,4,5}
b = {1,2,3,4}

print("diffrent thing in both the set is: ",a.symmetric_difference(b))
# Output: diffrent thing in both the set is: {5}


# 12.) isdisjoint(): It checks if two sets have NO common elements.
# If the sets have no matching items, it returns True.
# If even one item is the same in both, it returns False.

a = {1,2,3}
b = {4,5,6}

print("a is diffrent from b: ",a.isdisjoint(b)) # Output: a is diffrent from b:  True
print("b is diffrent from a: ",b.isdisjoint(a)) # Output: b is diffrent from a:  True


# 13.) Update() : take everything from the second set (or list) and put it into the first set.
# the second set's elements go into the first set.

a = {1,2,3}
b = {4,5,6}
a.update(b)

print("a Upadte b: ",a)