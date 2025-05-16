# Topic: Break and continue statements. 

# 1. break Statement: The break statement is used to exit or stop the loop (like for or while) before it has gone through all its iterations.
# It "breaks" out of the loop as soon as it's encountered, so the rest of the loop will not run.

# Example: It will print 1,2 and as soon as the contion is med means when i==3 it breaks the loop.
for i in range(1,6):
    if i == 3:
        break
    print(i)


# 2. continue Statement: The continue statement is used to skip the current iteration of the loop and move to the next iteration.

# It doesn't stop the loop entirely, but instead, it skips the code below it for the current iteration and goes back to the top of the loop for the next one.

# Example: It will print 1,2,4,5,6 and when the condition is met means i == 3 it skip 3 and goes to next line. 
for j in range(1,6):
    if j == 3:
        continue
    print(j)


print("\n")


####################### Practice questions ##########################

# Example 1: Print numbers from 1 to 10, but stop the loop if the number is 6.
# 👉 Use break to stop the loop.

for i in range(1,11):
    if i == 6:
        break
    print("For loop",i)

# While loop:
i = 1
while(i<=10):
    if i == 6:
        break
    print("While loop", i)
    i+=1

# Example 2: Print numbers from 1 to 10, but skip the number 4.
# 👉 Use continue to skip 4.
for i in range(1,11):
    if i == 4:
        continue
    print(i)

print("\n")

j = 1
while j <= 10:
    if j == 4:
        j += 1  # Increment before skipping
        continue
    print(j)
    j +=1

print("\n")

# Example 3: From a list of numbers, find the first number that is divisible by 7 and stop checking after that.
# 👉 Use break.

List = [5, 8, 11, 14, 18, 21]

for i in List:
    if i % 7 == 0:
        print("First number divisible by 7 is: ",i)
        break

print("\n")

# Example 4: Print all odd numbers from 1 to 10 using continue (i.e., skip even numbers).
# 👉 Use continue.
for i in range(1,11):
    if i % 2 == 0:
        continue
    print(i)
        
print("All odd numbers between 1 to 10 are printed.")

print("\n")

# Example 5: 5. Loop through characters in a string and skip all vowels.
# 👉 Use continue.

text = "hello world"

vowels = "aeiouAEIOU"

for i in text:
    if i in vowels:
        continue
    print(i)