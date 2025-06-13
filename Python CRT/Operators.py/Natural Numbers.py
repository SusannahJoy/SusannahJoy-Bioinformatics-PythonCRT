#To print Natural Numbers from 1 to n
Num=int(input("Enter an Integer :"))
print(f"Natural Numbers from 1 to {Num} : ")
for i in range(1,Num+1):
    print(i)

#To print natural numbers from n to 1
Num=int(input("Enter an Integer :"))
print(f"Natural Numbers from {Num} to 1 : ")
for i in range(Num,0,-1):
    print(i)