Num=int(input("Enter an integer :"))
Temp=Num
DigitCount=0
while (Num>0):
    Num=Num//10
    DigitCount+=1 #DigitCount=DigitCount+1
print(f"{Temp} has {DigitCount} digits")