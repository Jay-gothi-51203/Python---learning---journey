# Practice: File IO

# 1.) open the file: 
# if the file is not exist it will give an error, if the file is exist then it will open it.

# f = open("example.txt","r")
# The file "example.txt" is exist so it will not give an error.

# f = open("Jay.txt","r")
# The file "Jay.txt" is not exist so it will give an error.


print("\n")


# 2.) read the file:
# It is used to raed file. if the file is exist then it will read it otherwise it will give an error.

# file = open("example.txt","r")

# In oreder to execute one line of the code comment out other two lines.

# print("Read one line of the content: ",file.readline()) # It will print the line of the content of a file.

# print("Read miltiple lines of the content in list: ",file.readlines()) # It will print the lines of the content of a file in list.

# print("Read the whoel content of a file: ",file.read()) # It will print the whole content of a file:



# 3.) Write the file: if the file is not exist it will create it and if the file exist so it will overwrite the content.

# file = open("write.txt","w") #the file "write.txt" was not created before.

# file.write("Hello, How are you ?")


# Output: when you see in the file you can see that before written words are erased and you want to written words are written in the file.


# 4.) append the file: if the file is not exist it will create it and if the file exist so it will write the content in it.
# file = open("kemo.txt","a")

# file.write("Hello Kemo, How are you ? do you know ?\n")
# file.write("Kemo says,He is good")
# file.close()


# 5.) automatically close:

# with open("kemo.txt","r") as file:
    # print(file.read())


##############################################################

# 1.) Read a File and Print Content
# Write a program to read a text file named sample.txt and print its content.
file = open("sample.txt","w")
file.write("Hey I am sample.txt")

file = open("sample.txt","r")
print("Reading content of a file: ",file.read())

# file.readline() --> It is used to read line one of the content.
# file.readlines() --> It is used to read lines of the content but in list.

print("\n")


# 2.) Write to a File
# Create a file named output.txt and write the following lines to it:
# Hello, this is line 1
# This is line 2
file = open("output.txt","w")
file.write("Hello, this is line 1 \n")
file.write("This is line 2 \n")
file.close()

print("\n")


# 3.) Append to a File:
# Append the line "This line is appended." to the output.txt file.
file = open("output.txt","a")
file.write("This line is appended.")
file.close()


print("\n")


# 4.) Count Lines in a File
# Read a file and count the total number of lines.
file = open("output.txt","r")
lines = file.readlines()

print("The lines in the file are: ", len(lines))
file.close()


print("\n")


# 8.) Read and Reverse
# Read a file and write its content in reverse order (line by line) to a new file.

file = open("sample.txt","r")

content = file.read()

reverese_content = content[::-1]

print("Real content: ",content)

print("Reverse content: ",reverese_content)

file.close()


