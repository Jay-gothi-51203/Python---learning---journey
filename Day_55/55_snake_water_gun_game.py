# Topic: Snake water gun game in Python. 

import random   # Getting random input from computer

def get_computer_choice():  # function named "get_computer_choice()" get the computer choice randomly.
    return random.choice([ "snake", "water", "gun" ]) # computer select from this. 


def decide_winner(user, computer): # Function named "decide winner(user, computer)" parameters to decide who will the game.

    if user == computer: # If user choice equal to computer choice then it will be tie between them.
        return "It's tie!"
    
    # compare user and computer choice.
    if (user == "snake" and computer == "water") or \
       (user == "water" and computer == "gun") or \
       (user == "gun" and computer == "snake"):
        return "Congratulation, You won!"

    else: 
        return "Oops, Computer won!"

# Welcome message
print("\n Welcome to the snake, water, gun game")

print("\n")

# message for users to get input.
print("choose your choice: snake, water, gun and if you want to exit write 'exit' ")

# infinity loop to play the game as many time as user want
while True:
     
     user_choice = input("Enter your choice: ").lower().strip() # taking user input

     if user_choice not in ["snake","water","gun"]: #if user input not valid then this will print.
      print("Invalid choice!, plese choose one the right option from this: [snake, water, gun] ")

      if user_choice == "exit": # if user want to exit
         print("Thank you for playing the game.") # goodbye message. 

         break # take the user out of the loop or game. 
      
     else: 
      computer_choice = get_computer_choice() # make computer_choice variable to get computer choice
      print(f"computer chose: {computer_choice}") # it will print the computer choice 

      print(decide_winner(user_choice,computer_choice)) # calling the function which is decide_winner(user_choice, computer choice)

      print("\n")

