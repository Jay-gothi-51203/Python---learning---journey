# Excercise - 1: Create a calculator. 


a = float(input("Enter the first value: "))

b = float(input("Enter the second value: "))

operators = input("Enter the operations you want to performe from these like + , - , * , / : ")

if operators == "+":
    print("The sum of two numbers: ", a+b)

elif operators == "-":
    print("The substraction of two numbers: ", a-b)

elif operators == "*":
    print("The multiplication of two numbers: ", a*b)

elif operators == "/":
    if(b!= 0):
     print("The dividion of two numbers: ", a/b) 
    else:
     print("Cannot divide by zero.")
    
else:
    print(" Enter valid Operation. choose from sum(+), substration(-), multiplication(*), division(/) only. ")


