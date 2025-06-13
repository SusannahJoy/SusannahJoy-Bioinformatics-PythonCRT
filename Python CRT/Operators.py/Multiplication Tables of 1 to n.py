Num=int(input("Enter an Integer : "))
for i in range(1,Num+1):
    print(f"Multiplication Table of {i}:")
    for j in range(1,11):
        print(f"{i}x{j}={i*j}")