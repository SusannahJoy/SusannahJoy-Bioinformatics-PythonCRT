Num=int(input("Enter an integer :"))
#using if-else
if(Num>=100 and Num<=999):
    print(f"{Num} is a Three-digit number")
else:
    print(f"{Num} is not a Three-digit Number")
#using ternary operator
Result="Three-digit Number" if(Num>=100 and Num<=999) else "not a Three-digit Number"
print(f"{Num} is a {Result}")