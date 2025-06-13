#To print Squares from 1 to n
Num=int(input("Enter an Integer :"))
print(f"Squares from 1 to {Num} : ")
for i in range(1,Num+1):
    print(i*i)

#To print Squares from n to 1
Num=int(input("Enter an Integer :"))
print(f"Squares from {Num} to 1 : ")
for i in range(Num,0,-1):
    print(i*i)