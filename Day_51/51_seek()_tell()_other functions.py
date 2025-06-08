# Topic: seek(), tell() and other functions

# 1.)seek(): if you give 5 like seek(5) then it will skip the first 5 letters and start reading from 6
# with open("sample.txt","r") as file:

    # file.seek(5) # It will skip first 5 letters and start reading from 6 letter

    # print("remaining last five letters are: ",file.read()) # It will print the remaining 5 letters from 6 to 10.


print("\n")

# 2.) tell(): It tells you where you are in the file (like a position marker.
# It is used to see wher we are after the writing or reading means where is the pointer in the file.
# with open("sample.txt","w") as file:

    # file.write("123456789") # It will print 1 to 9 in the file

    # print("Your position in the file is: ",file.tell()) # 1 to 9 is written in the file and that's why the pointer(marker or position) it shows 9.


print("\n")


# 3.) read(n): It reads only a few letters (you choose how many).
# with open("sample.txt","r") as file:
    # print("First 5 letters are: ",file.read(5)) # It reads first 5 letters


print("\n")


# 4.) flush(): It saves what you wrote to the file immediately.
# with open("sample.txt","a") as file:
    # file.write("Hello")
    # file.flush() # It saves what you write immediately.


print("\n")


# 5.) truncate(): It cuts the file to a smaller size.
# with open("sample.txt","r+") as file:
    # file.truncate(5) #It will keep the first 5 letters safe.