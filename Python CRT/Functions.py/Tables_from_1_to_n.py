'''
Write a python program to build a function which prints the multiplication tables of 1 to n
'''
def Table(Num):
    for i in range(1,Num+1):
        print(f"Multiplication Tables of {i} :")
        for j in range(1,11):
            print(f"{i}x{j}={i*j}")
Table(3)