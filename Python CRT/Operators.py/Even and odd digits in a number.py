Num=int(input("Enter an integer :"))
Even=0
Odd=0
while Num!=0:
    rem=Num%10
    if(rem%2==0):
        Even+=1
    else:
        Odd+=1
    Num//=10
print(f"No.of Even digits {Even}")
print(f"No.of Odd digits {Odd}")