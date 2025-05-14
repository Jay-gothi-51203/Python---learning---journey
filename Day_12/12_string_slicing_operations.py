# TOPIC: String Slicing: 

# String Slicing: String slicing means cutting a part of a string using indexes.

Names = "Harry ,Subham"
print(Names[:5]) # it will start from index 0 and goes to index 5 but 5 is not included. index no included: H=0, a=1, r=2, r=3, y=4. #Output: Harry

# In order to find length of string use len().
# Example: 
print(len(Names))

fruits= "Mango"
print(fruits[:]) #If you didn't write anything then python will starts from 0 index and goes to last index which is included here it will starts from 0 index and goes to last index and print all indexes.
#Output: Mango

print(fruits[:3]) #If we want first 3 character. #Output: Man

print(fruits[0:]) #It will starts from index 0 and goes to end and print all the characters.

print(fruits[1:4]) #If you want to print index 1 to 4 then it will starts from 1 and ends with 4.

# Spelling: M    A    N    G    O
# Index:   -5   -4   -3   -2   -1
# Syntax: fruits[ start : end ] # end is not included. 
print(fruits[ -5:-1]) #It will starts from -5 and end -1 but -1 is end and end is not included. It will take index -5, -4, -3, -2 

# Use a step: Syntax = fruits[start:end:step] step means it will skip if step is 2 like [0:0:2]it will 
print(fruits[::2]) # It will start from index 0 and till goes to end but it will skip 2 character like it will print 'M','N', 'O'. and skip 'A','G'.

# It is used to reverse a string.
print(fruits[ : :-1]) # It will print string reverse. 


#####################   Practice Questions  ###################

word = "Programming"
# word =            p    r    o    g    r    a    m    m    i    n    g
# Positive Index:   0    1    2    3    4    5    6    7    8    9    10
# Negative Index:  -11  -10  -9   -8   -7   -6   -5   -4   -3   -2    -1

print(word[0:6]) #It will start from index 0 and goes to till 6 but 6 is not included. #Output: Progra
print(word[3:8]) #It will start from index 3 and goes to till 8 but 8 is not included. #Output: gramm
print(word[-4:]) #It will start from index -4 and goes to till -1 but -1 is not included.#Output: ming
print(word[:-5]) #It will start from index -11 and goes to till -5 but -5 is not included. #Output: progra
print(word[-1:-4:-1])#It will start from index -1 and goes to till -4 but -4 is not included and step -1 means it will goes to -1 to -4 and print them in reverse order. #Output: gni
print(word[::-1]) #It will start from index 1 and goes till to last index but last index is included and print the string in reverse order.  #Output: gnimmargorP
print(word[::2]) #It will start from index 0 and goes till to index last but last index is included and print the character 2 means print first character and then skip one after that print another character. #Output: Pormig
print(word[-7:-2]) #It will start from index -7 and goes to till index -2 but -2 index is not included. #Output: rammi
