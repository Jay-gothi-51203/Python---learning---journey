# Practice of set methods.

# 1.) Add Items: Create a set of fruits. Add "apple", "banana", and "cherry" using .add() method.
fruits = set()
fruits.add("apple")
fruits.add("banana")
fruits.add("cherry")

print("add 3 fruits in the set: ",fruits)
# Output: add 3 fruits in the set:  {'banana', 'cherry', 'apple'}

# 2.) Remove vs Discard : # Try removing "banana" from the set using .remove() and then try removing "mango" using .discard(). Observe what happens in each case.

# remove(): remove the specific element and if the item is not present in the set then it will give an error.

# discard(): remove the specific element and if the item is not present in the set then it will not give an error.

fruits = {"apple","banana","cherry"}
fruits.remove("banana")

print("Remove: ",fruits)
# Output: Remove:  {'apple', 'cherry'}

fruits = {"apple","banana","cherry"}
fruits.discard("Mango")
print("discard: ",fruits)
# Output: discard:  {'apple', 'banana', 'cherry'}


# 3.) Pop Method: Use .pop() on a set and see which item gets removed. Try it a few times.
# pop means remove and return random items.
fruits = {"apple","banana","cheery"}
fruits.pop()

print("pop: ",fruits)
# Output: pop:  {'apple', 'cheery'}


# 4.) Clear a Set: Clear a set completely using .clear() and print it.
fruits = {"apple","banana","cheery"}
fruits.clear()

print("Clear fruits set: ",fruits)
# Output: Clear fruits set:  set()


#  Set Operations Practice:

# 5.) Union(): Let A = {1, 2, 3} and B = {3, 4, 5}. Find the union using .union() and |.
# Union make one set from A and B means it joint two sets.
A = {1, 2, 3}
B = {3, 4, 5}

print("A union B is: ",A.union(B)) # or print(A|B)
# Output: A union B is:  {1, 2, 3, 4, 5}


# 6.) Intersection(): Find the intersection of A and B using .intersection() and &.
# Intersection means take only common items from both sets.
A = {1, 2, 3}
B = {3, 4, 5}

print("A intersection B is: ",A.intersection(B)) # or print(A & B)
# Output: A intersection B is:  {3}


# 7.) Difference(): Find the difference A - B and B - A using .difference() and -.
# diffrence() means gives the values that is present in set A and but not present in set B.
A = {1, 2, 3}
B = {3, 4, 5}

print("The diffrence between A and B set is: ",A.difference(B)) # or print(A - B)
# Output: The diffrence between A and B set is:  {1, 2}

print("The diffrence between B and A set is: ",B.difference(A)) # or print(B - A)
# Output: The diffrence between B and A set is:  {4, 5}


# 8.) Symmetric Difference: Find elements in either A or B but not both using .symmetric_difference() or ^.
# Symmetric Difference: It gives those values which are not common in both sets.
A = {1, 2, 3}
B = {3, 4, 5}

print("Not common items in both the sets are: ",A.symmetric_difference(B)) #or print(A^B)
# Output: Not common items in both the sets are:  {1, 2, 4, 5}



# Set Relationship Practice:

# 9.) Subset & Superset
# Let C = {1, 2} and D = {1, 2, 3, 4}. Check if C is a subset of D and if D is a superset of C.
C = {1,2}
D = {1, 2, 3, 4}

# It means set D can contain all the items of set C 
print("C is subset of D: ",C.issubset(D))
# Output: C is subset of D:  True

# It means set D have set C inside it(set D).
print("D is superset of C: ",D.issuperset(C))
# Output: D is superset of C:  True

# 10.) Disjoint Sets
# Let E = {10, 20}, F = {30, 40}. Use .isdisjoint() to check if they share no elements.
E = {10, 20}
F = {30, 40}

# It check both the sets have diffrent items or not.
print("E and F have diffrent items: ",E.isdisjoint(F))
# Output: E and F have diffrent items: True



# Challenge Questions

# 1.) Common Friends: Two people have sets of friends. Write a function to return mutual friends using .intersection().

def mutual_friends(people_1,people_2):
    return people_1.intersection(people_2)


people_1 = {"Jay Patel","Virat Kohli","MS Dhoni","Rohit Sharma"}

people_2 = {"Alice","Jay Patel","Virat Kohli","Hardik Pandya"}

print("The mutual friends of people 1 and people 2 are: ",mutual_friends(people_1,people_2))

# Output: The mutual friends of people 1 and people 2 are:  {'Jay Patel', 'Virat Kohli'}


# 2.) Unique Elements in List: Write a function that takes a list and returns only the unique elements using sets.

list = [1,2,3,4,5,1]

print("list: ",list) #Output: ist:  [1, 2, 3, 4, 5, 1]

my_set = set(list) 

print(type(my_set)) #Output: <class 'set'> 
print("Set: ",my_set)
# Output: Set:  {1, 2, 3, 4, 5}


# 3.) Set Difference in Real Life: Given sets attended_class and submitted_assignment, find students who attended class but didn't submit the assignment.
def didnot_submit(attended_class,submitted_assignment):
    return attended_class.difference(submitted_assignment)

attended_class = {"Jay","Meet","Ronak","Karan","Rahul","Prit"}

submitted_assignment = {"Jay","Meet","Ronak"}

# didnot_submit = attended_class.difference(submitted_assignment)

print("Those student who attended the class but did't submit assignment: ", didnot_submit(attended_class,submitted_assignment))
# Output: Those student who attended the class but did't submit assignment:  {'Prit', 'Karan', 'Rahul'}

# Print with the help of for loop one name in one line.
# for name in didnot_submit:
#     print(name)


# 4.) Are Anagrams?: Write a function that takes two words and checks if they are anagrams using set comparisons.
#  Two words are anagrams if they contain the same characters, just in a different order.

def are_anagrams(word_1,word_2):
    if set(word_1) == set(word_2):
        print(f"{word_1} and {word_2} are Anagrams.")

    else:
        print(f"{word_1} and {word_2} are not Anagrams.")
        

word_1 = input("Enter the first words: ") # assume if user enter listen

word_2 = input("Enter the second words: ") # assume if user enter silent

are_anagrams(word_1,word_2)


# # 5.) Count how many vowels in the given sentence.

# take sentence from the user.
sentence = input("Enter the sentence: ").lower()

# 5 vowels 
vowels = {"a","e","i","o","u"}

# convert sentence in set to get uniqe character
char_in_sentence = set(sentence)

# get the common characters from vowels and char_in_sentence by using .intersection().
found_vowels = vowels.intersection(char_in_sentence)

# print the how many vowels are in the sentence.
print("Vowels in the sentence: ",found_vowels)

# Print the how many vowels are in the sentence.
print("The total number vowels in the sentence: ",len(found_vowels))

