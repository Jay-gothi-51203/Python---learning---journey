# Question:
# Write a python program to translate a message into secret code language. Use the rules below to translate normal English into secret code language

# Coding:
# if the word contains atleast 3 characters, remove the first letter and append it at the end
#   now append three random characters at the starting and the end
# else:
#   simply reverse the string

# Decoding:
# if the word contains less than 3 characters, reverse it
# else:
#   remove 3 random characters from start and end. Now remove the last letter and append it to the beginning

# Your program should ask whether you want to code or decode


# Answer:

# Fixed "random" strings for simplicity
r1 = "dfg"  # start code to add
r2 = "izo"  # end code to add

# Ask user for action
choice = input("Do you want to code or decode? (Enter 'code' or 'decode'): ").strip().lower()

# Get the message from the user
message = input("Enter the message: ")

# Split the message into words
words = message.split()

# Create a list to hold the new (encoded or decoded) words
new_words = []

# If user wants to encode the message
if choice == "code":
    for word in words:
        if len(word) >= 3:
            word = word[1:] + word[0]       # Move first letter to the end
            word = r1 + word + r2           # Add r1 at the start and r2 at the end
        else:
            word = word[::-1]               # Reverse if short
        new_words.append(word)

# If user wants to decode the message
elif choice == "decode":
    for word in words:
        if len(word) < 3:
            word = word[::-1]               # Just reverse short words
        else:
            word = word[3:-3]               # Remove r1 and r2
            word = word[-1] + word[:-1]     # Move last letter to front
        new_words.append(word)

else:
    print("Invalid choice. Please enter 'code' or 'decode'.")
    exit()

# Join all words together with spaces
new_message = ' '.join(new_words)

# Show the final result
print("Result:", new_message)
