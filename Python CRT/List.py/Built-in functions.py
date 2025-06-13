Size=int(input("Enter the Size of List :"))
Num=[]
for i in range(Size):
    Temp=int(input(f"Enter the Element at {i} index:"))
    Num.append(Temp)
print(f"Given List : {Num}")
print("Maximum Element :",max(Num))
print("Minimum Element :",min(Num))
print("Summation :",sum(Num))
print("Sorted List :",sorted(Num))