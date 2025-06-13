Num=int(input("Enter the Interger value :"))
#using if-else
if(Num>=-9 and Num<=9):
    print(f"{Num} is Digit")
else:
    print(f"{Num} is Number")
#Ternary
Result="Digit" if(Num>=-9 and Num<=9) else "Number"
print(f"{Num} is {Result}")