# Exercise: Create a program capable of displaying question to the user like KBC.

# Use list data type to store the questions and their answers.

# Display the final amount the person is taking after playing the game.

print("\n")

print("Let's play Kaun Banega Carorpati(KBC)")

# List of questions
questions = [
    "What is the capital of India?",
    "Which number comes after 7?",
    "Which animal is known as the king of the jungle?",
    "How many days are there in a week?"
]

# Multiple-choice options for each question
options = [
    ["A. Mumbai", "B. Delhi", "C. Kolkata", "D. Chennai"],
    ["A. 6", "B. 9", "C. 8", "D. 10"],
    ["A. Lion", "B. Tiger", "C. Dog", "D. Elephant"],
    ["A. 5", "B. 6", "C. 8", "D. 7"]
]

# Correct answers for each question (corresponds to above options)
answers = ["B", "C", "A", "D"]

# Amount won for each correct answer
prize = 10000

# To keep track of total prize won
total = 0

# Welcome message
print("Welcome to KBC Game \n")

# Loop through all the questions using their index
for i in range(len(questions)):
    print(f"Q{i+1}: {questions[i]}")  # Print the current question

    # Print the four options for the current question
    for option in options[i]:
        print(option)

    # Ask user for their answer and format it properly
    user_answer = input("Your answer (A/B/C/D): ").strip().upper()

    # Check if user's answer is correct
    if user_answer == answers[i]:
        print("Correct!\n")
        total += prize  # Add prize money to total
    else:
        print("Wrong answer!")
        print("The correct answer was:", answers[i])  # Show correct answer
        break  # Stop the game if the answer is wrong

# Show the final amount won by the user
print(f"\nYou won ₹{total}. Thanks for playing!")

