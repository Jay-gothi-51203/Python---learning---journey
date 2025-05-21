import time

t = time.strftime('%H:%M:%S') 

hour = int(input("Enter hour: "))


if (hour>=0 and hour <=12):
    print("Good morning sir!")

elif (hour>=11 and hour<=15):
    print("Good afternoon!")

elif (hour>=16 and hour<=24):
    print("Good night sir!")

else:
    print("Invalid input, enter hour between 0 to 24.")


