# Topic: map(), filter(), reduce() in Python. 

# 1.) map() : map() is used when you want to change every item in a list.
# It does something with every item and gives you a new list. 

# Syntax: map(lambda function, list)

# Example: 
numbers = [1, 2, 3, 4, 5 ]

add_five = map(lambda x: x+5, numbers)

print(f"after adding 5 to the list: { list(add_five) } ")


print("\n")


# 2.) filter(): filter() is used when you want to keep some items from a list.
# It only keeps items in the list depending on the condition. 

# Syntax: filter(lambda function, list)

# Example: 
numbers = [1, 2, 3, 4, 5]

even_only = filter(lambda x: x % 2 == 0, numbers)

odd_only = filter(lambda x: x % 2 != 0, numbers)


print(f"even numbers in the list: { list(even_only) }")

print(f"odd numbers in the list: { list(odd_only) }")


print("\n")

# Practice question:
Numbers = [10, 15, 20, 25, 30 ]

five_sub = map(lambda x: x-5, Numbers)

biger_fifteen = filter(lambda x: x > 15, Numbers)

print(f"after sub 5 from the list: { list(five_sub) }")

print(f"greater than 15 in the list: { list(biger_fifteen) }")


print("\n")


# 3.) reduce() : 

from functools import reduce

num = [1, 2, 3, 4]

total_sum = reduce(lambda x, y: x + y, num)

print(f"Total sum of the list: { total_sum }")


# example - 2:

Num = [1, 2, 3]

multiply = reduce(lambda x, y: x * y, Num)


print(f"After multiplication: { multiply }")









