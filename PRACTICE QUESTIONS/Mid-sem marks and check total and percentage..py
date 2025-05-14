    #          Jay              Meet
# OS:          27                31
# Web tech:    33                30
# Oops:        23                19
# Python:      28                30
# CGAVM:       30                29
#--------------------------------------
# Total:      141               139

# This is a program in python to Enter a marks of the subjects and get Total marks and percentage. MID-SEM (4th sem)
Os_marks = int(input("Enter the marks of Operating system: "))

Webtech_marks = int(input("Enter the marks of Web Tech with UI/UX: "))

Oops_marks = int(input("Enter the marks of object oriented programming with UML marks: "))

Python_marks = int(input("Enter the marks of Python: "))

CGAVM_marks = int(input("Enter the marks of Computer Graphics AR VR Metaverse: "))


Total_marks = Os_marks + Webtech_marks + Oops_marks + Python_marks + CGAVM_marks 


percentage = (Total_marks * 100) / 200 

if percentage >= 90:
    print("Congratulation!, You have O (outstanding) Grade. ")

elif percentage >= 80:
    print("You have A+ grade. ")

elif percentage >= 70:
    print("You have A grade. ")

elif percentage >= 60:
    print("You have B garde. ")

elif percentage >= 50: 
    print("You have C grade. ")

elif percentage >= 40:
    print("You have D garde. ")

elif percentage >= 33:
    print("You have E grade .")

else:
    print(" You are fail. ")



print("Your total marks:  ", Total_marks)

print("You have" , percentage , ".")
