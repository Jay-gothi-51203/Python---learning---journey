# Topic: File handling methods like readline(), readlines(), writelines(), 

# 1.) Read(): Reads the whole file content
# Reads the entire file content as a single string.
# with open("sample.txt","r") as file:
    # print("Read the content of a file: ",file.read())

# for loop in file:
# with open("sample.txt","r") as file:
#     for lines in file:
#         print(lines)


print("\n")


# 2.) readline(): Reads one line at a time
# Reads just one line from the file each time you call it.
# with open("sample.txt","r") as file:
#     print("Read one line at a time: ",file.readline())


print("\n")


# 3.) readlines(): Reads multiple lines at a time but as list.
# with open("sample.txt","r") as file:
#     print("Read multiple lines but as list: ",file.readlines())


print("\n")


# 4.) write(): write one line at a time.
with open("sample.txt","w") as file:
    file.write("Hello I am write method.")


# for loop in write method:
# file = open("sample.txt","w")
# lines = ["line-1 \n","line-2 \n","Line-3 \n"]
# for line in lines:
#     file.write(line)
# file.close()


print("\n")


# 5.) writelines() method: 
with open("sample.txt","w") as file:
    file.writelines(["This is writelines() method: ","First line \n, Second line \n, Third line."])







