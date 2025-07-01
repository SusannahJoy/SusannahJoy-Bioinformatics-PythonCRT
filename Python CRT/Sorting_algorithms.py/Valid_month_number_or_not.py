'''
Write a python program to read the month number as input from the user 
and check whether the month number is valid month number or not
'''
Month=int(input("Enter the Month Number:"))
if (Month>=1 and Month<=12):
    print("Valid Month Number")
else:
    print("In-Valid Month Number")