# 1.) Positional arguments: You give arguements to a function in order. The order matters.

# Question: Write a function called greet that takes two arguments: name and time_of_day, and prints:

def greet(name,time_of_day):
    print(f"Hello!,{name} {time_of_day}!")


greet("Jay","Good morning")


################
# 2.) Keyword arguments: You don't need to give arguments to a function in order. just write keyword1 = value1, keyword3 = value3, keyword2 = value2......
# Function knows the values by its keywords.

# Question: Write a function called student_info with three parameters: name, grade, and subject.

def student_info(name,grade,subject):
    print(f"Hello!, I am {name} and I got {grade} grade in {subject} subject.")

student_info(name="Jay", subject="Python", grade="A+", )


###############
# 3.) Default arguments: if you don't give the value Function take default value.

# Question : Write a function describe_pet that takes two arguments: animal_type and name.
# Make animal_type default to "dog" if not given.

def describe_pet(animal_type, name = "buddy"):
    print(f"I have {animal_type} and it's name is {name}.")

describe_pet(animal_type = "dod")
describe_pet(animal_type = "lion",name="Sher")


#################
# 4.) Virable - length Arguments:

# 1.) *args: It takes many values without names.

# Question: Write a function add_numbers that takes any number of numbers using *args and prints the first and second numbers.
def add_numnbers(*args):
    print("First number: ",args[0])
    print("Second number: ",args[1])


add_numnbers(10,20,30,40)
add_numnbers(10,20)

# Another Example: 
def fruits(*args):
    print("These are the fruits in the basket: ")
    for fruit in args:
        print(fruit)
    

fruits("Apple", "Banana", "Mango")

fruits("Apple", "Banana", "Mango", "Orange", "Watermelon")


# 2.) **kwargs : It takes multiple named values.

# Question: Write a function display_user_info that accepts **kwargs and prints the values of "username" and "email".

# Example:
def display_user_info(**kwargs):
    print("Username: ", kwargs["username"])
    print("Email: ", kwargs["email"])


display_user_info(Username = "Jay@123", Email = "Gothijay@51203")

# Example 2: print elements by kwargs.get(element).
def display_user_info(**kwargs):
    print("Username: ", kwargs.get("username"))
    print("Email: ", kwargs.get("email"))


display_user_info(username = "Jay@123", email = "Gothijay@51203")

# Example: 
def display_user_info(**kwargs):
    print("The user details: ")
    for key,value in kwargs.items():
        print(f"{key}:{value}")


display_user_info(name="Jay Gothi",username="Jay@123",email= "Gothijay@51203",Password="Jay@1234")
