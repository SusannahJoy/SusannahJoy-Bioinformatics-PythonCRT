Num=int(input("Enter an integer :"))
#using if-else
if(Num>=10 and Num<=99):
    print(f"{Num} is a Two-digit Number")
else:
    print(f"{Num} is not a Two-digit Number")
#using ternary operator
Result="Two-digit Number" if(Num>=10 and Num<=99) else "not a Two-digit Number"
print(f"{Num} is a {Result}")