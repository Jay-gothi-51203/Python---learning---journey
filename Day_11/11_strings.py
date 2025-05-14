# TOPIC: Strings in Python. 

# What is a String?
# A string is just text in Python.
# Anything you type inside quotes (' ' or " ") is a string.

name = "Jay"
texto = "Python is fun"
no = "12345" # Even numbers inside quotes are strings, not numbers.

#####################   Some Basic Things You Can Do with Strings: ###############

# 1. Joining strings (Concatenation)
Name = "Jay"
print("Hello " + Name + "!") #Output: Hello Jay!

# 2. Repeating strings:
print(name * 3)

# 3. Getting part of a string (Slicing):
text = "Python" # indexing: p=0, y=1, t=2, h=3, o=4, n=5, 
# [start : end]
print(text[0:]) #Output: Python,  #It will start from 0 index and till go end of the index.
print(text[0:3]) #Output: Pyt,  #It will start from 0 index and till go to 3 but 3 is not included so it will print index 0,1,2 (Total - 3(0,1,2). )

# 4. String length:
text = "Python"
print(len(text))

####################  Some Useful String Methods   #########################

# 1.) .lower(): It convert all text into lower case.
Cricket = "VIRAT"
print(Cricket.lower()) #Output: virat

# 2.) .upper() : It converts all text into upper case.
Cricket = "virat"
print(Cricket.upper())  #Output: VIRAT

# 3.) .capitalize() : It keeps first letter capitalize and rest of others in lowercase.
Cricket = "virat"
print(Cricket.capitalize())  #Output: Virat

# 4.) .title()
# Capitalizes the first letter of every word.
Cricket = "virat kohli"
print(Cricket.title())  #Output: Virat Kohli

# 5. .strip()
# Removes spaces from both ends of a string.
Cricket = " Virat "
print(Cricket.strip()) #Output: Virat , It will remove unnecessary space from both side in string.

# 6. .replace(old, new)
# Replaces parts of the string.
TEXT = "I love apples."
print(TEXT.replace("apples", "banana"))

# 7. .startswith() / .endswith()
# Checks if string starts or ends with a certain substring.
Para = "Hello world!"
print(Para.startswith("Hello")) #Output: True because it starts with Hello. 
print(Para.endswith("virat ")) # Output: False because it don't end with virat it ends with world!.

# Multi-line string: If we have to print multiple lines like (chats) on screen at that time we can use triple quotes(''') and between triple quotes (''') is known as string and you can print it. 

chats = ''' 
        He: Hello!
        She: hey!
        He: How are you ?
        She: Fine.
        He: What's your name ?
        She: Wamiqua, and what's your name ?
        He: my name is Jay.
'''

print(chats) # It will print multiple lines.

print(name[0]) 

########################   🧠 Practice Questions on Python Strings  #######################

# 1.) Concatenation: 
first_name = "John "
last_name = "Doe"
print(first_name + last_name)

# 2.) Repeating Strings:
print("hello " * 3)

# 3.) String Slicing:
# Print the first 3 letters
# Print the last 4 letters
# Print from index 3 to 7
# Indexing: p=0.r=1,o=2,g=3,r=4,a=5,m=6,m=7,i=8,n=9,g=10. 
word = "Programming"
print(word[0:3]) # It will print first three letters: p,r,o
print(word[7:]) # It will print last four letters: m,i,n,g
print(word[3:7]) # It will print the character whose index is 3 to 7. like: g,r,a,m. because last one index 7 is not included.

# 4.) String Length: Write a program that takes a string and prints how many characters it has (including spaces).
sentence = "Python is powerful"
print(len(sentence)) #Output: 18


##### String Methods Practice: #####

# 5.) Use .lower() and .upper():
Text = "HeLLo WoRLD"
print(Text.lower()) #Output: hello world
print(Text.upper()) #Output: HELLO WORLD

# 6) Use .capitalize() and .title():
quote = "Life is beautiful"
print(quote.capitalize()) #Output: Life is beautiful.
print(quote.title()) #Output: Life Is Beautiful.

# 7.) Use .strip():
dirty = " clean me "
print(dirty) #It will print with unnecessary space.#Output:  clean me  
print(dirty.strip()) # It will print without unnecsessary space., #Output: clean me

# 8.) Use .replace():
# I tried new message not the practice one.
message = "I hate you"
print(message.replace("hate","love")) #Output: I love you.

# 9.) Use .startswith() and .endswith():
Line = "Once upon a time in Python."
print(Line.startswith("Once")) #Output: True
print(Line.endswith("Python.")) #Output: True
print(Line.endswith("Java")) #Output: False


##### Multi-line strings #####

# 10.) Create and print the following multi-line string.
practice_para = '''Hello,
This is Python.
Let's learn strings!'''

print(practice_para) #This will print multiple line strings.


