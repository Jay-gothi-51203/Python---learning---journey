# Topic: String Methods in Python. 

# Strings are immutable. So it will create a new string.
# String Methods/ String Operation : String methods are built-in tools you can use to work with strings.
# They help you do things like change letters to uppercase, count letters, replace words, etc.

##########  Common String Methods  #############

name = " Virat kohli "

# 1.) upper() – Makes all letters uppercase
print(name.upper()) #Output: VIRAT KOHLI

# 2.) lower() - Makes all letters lowercase
print(name.lower()) #Output: virat kohli

# 3.) capitalize - Makes the first letters uppercase
print(name.capitalize()) #Output: Virat kohli

# 4.) title() – Makes first letter of each word uppercase
print(name.title()) #Output: Virat kohli

# 5.) strip() – Removes spaces at the beginning and end
print(name.strip()) #Output:Virat kohli

# 6.) replace() – Replaces part of the string
print(name.replace("Virat", "Anushka")) #Output: Anushka kohli

# 7.) .startwith() / .endswith() - It will check that the string is start with or end with something. 
print(name.startswith(" Virat")) #Output: True
print(name.endswith("kohli ")) #Output: True 
print(name.endswith("Dhoni")) #Output: False

# 8.) split() – Splits the string into a list of words
print(name.split()) #Output: ['Virat', 'kohli']

# 9.) count() – Counts how many times something appears
print(name.count("i")) #Output: 2 

# 10.) find() – Finds the position of a word/letter
print(name.find("V")) #Output: 1   

first = "Jay"
last = "Gothi"
print(f'{first} [{last}] is a coder.')
