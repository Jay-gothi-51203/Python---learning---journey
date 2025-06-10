# Number Guessing Game:

# In this game You have to guess the correct the number from specific range.

import random   # Import random module to generate random numbers

print("\n Let's play number guessing game.")  # Welcome message

print("\n Best of the luck for the game.") # Good luck message

correct_number = random.randint(1,10)  # Generate a random number between 1 and 10

while True:  #while infinite loop

    guess_number = int(input("\n Enter a number between 1 to 10: "))  # # Ask the user to enter a number and convert it to an integer.

    # Check if the guess is correct
    if guess_number == correct_number:
        print("Correct!, You guess it right!") # print this line if condition is true
        break  # if the user guess it right then this "break" will take the user exit the loop.
    
    elif guess_number < correct_number: # If the user guess the low number than the correct number.
        print("sorry, too late!, try again.")
    
    elif guess_number > correct_number: # If the user guess the high number than the correct number.
        print("sorry!, too high!, try again.")