'''
Write a python program to read the year as the input from the user and 
check whether the year is a leap year or not
'''
Year=int(input("Enter the year:"))
if(Year%4==0 and Year%100!=0 or Year%400==0):
    print("Leap Year")
else:
    print("Not a Leap Year")