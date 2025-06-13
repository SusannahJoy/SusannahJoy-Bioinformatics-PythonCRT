'''
Write a python program to build a function which prints the multiplication table of n
'''
def Table(Num):
    for i in range(1,11):
        print(f"{Num}x{i}={Num*i}")
Table(5)