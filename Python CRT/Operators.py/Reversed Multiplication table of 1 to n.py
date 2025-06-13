Num=int(input("Enter an integer :"))
for i in range(1,Num+1):
    print(f"Multiplication table of {i}:")
    for j in range(10,0,-1):
        print(f"{i}x{j}={i*j}")