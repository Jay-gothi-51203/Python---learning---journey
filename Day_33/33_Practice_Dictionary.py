# Practice of Dictionary:

# 1.) Create a dictionary that stores your name, age, and favorite color. Print each value using the key.

# Create a dictionary that stores your name, age, and favorite color.
person_1 = {
    "Name": "Jay",
    "Age": 21,
    "Favorite color": "Black"
}

# Print each value using the key.
print(person_1["Name"])
print(person_1["Age"])
print(person_1["Favorite color"])


print("\n")

# 2.) Given this dictionary: Print the student's name and grade.

# Given the dictionary that stores your name, age and grade.
student = {"name": "John", "age": 20, "grade": "B"}

# Print the student's name and grade.
print("Student's name: ",student["name"])
print("Student's grade: ",student["grade"])


print("\n")

# 3.) Add a new key-value pair to the dictionary (e.g., add "city": "London").
student = {"name": "John", "age": 20, "grade": "B"}

student["City"] = "London" # Method - 1 to add city in current dictionary

#student.update({"City": "London"}) # Method - 2 to add city in current dictionary

print(student) # print the whole dictionary


print("\n")

# 4.) Update the value of an existing key. Change the age to 21.
student = {"name": "John", "age": 20, "grade": "B"}

student.update({"age" : 21}) #change the value of a key "age" 20 to 21.

print("Age changed 20 to",student["age"])

print(student)


# 5.) Check if a key exists in a dictionary (e.g., check if "grade" is in student).
student = {"name": "John", "age": 20, "grade": "B"}

if "grade"  in student:
    print(f"Yes, 'grade' is present in the student dictionary.")

else:
    print("Sorry,'grade' is not present in the student dictionary.")


print("\n")

# 6.) Create a dictionary of 3 friends and their favorite foods :➤ Use a for loop to print each friend and their favorite food.

favorite_foods = {
    "Jay" : "Pizza",
    "Meet": "Mancurian",
    "Rahul": "Khandvi"
}

for keys, values in favorite_foods.items():
    print(f"{keys}:{values}")


print("\n")

# 8.) You have this dictionary:
# prices = {"apple": 30, "banana": 10, "milk": 50}
# ➤ Ask the user to enter an item name and print the price.

prices = {"apple": 30, "banana": 10, "milk": 50}

print('''
We have the following items:
    - apple
    - banana 
    - milk
Type 'exit' to finish your shopping.
''')

count = 0 

while True:
   
   user_input = input("Enter the item you want to buy: ").lower().strip()

   if user_input == "apple":
    count += 30
    print(f"The price of apple is {prices["apple"]}.")
    
   elif user_input == "banana":
    count += 10
    print(f"The price of banana is {prices["banana"]}.")

   elif user_input == "milk":
    count += 50
    print(f"The price of milk is {prices["milk"]}.")

   elif user_input == "exit" or user_input == "Exit":
    print("Thank You!, have a nice day, see you again")
    break

   else:
    print("Invalid input. We only offer three things apple, banana, milk.")
    break

print(f"You have to pay: {count}")
