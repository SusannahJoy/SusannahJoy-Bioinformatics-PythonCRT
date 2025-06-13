Num=int(input("Enter an integer :"))
Temp=Num
Sum=0
Rem=0
while Num!=0:
    Rem=Num%10
    Sum=Sum+Rem
    Num=Num//10
print(f"Summation is {Sum} ")