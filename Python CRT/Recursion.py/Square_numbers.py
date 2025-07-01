'''
Write a python program to print square numbers from 1 to n
Write a python program to print square numbers from n to 1
'''
def Square(N):
    if N==0:
        return
    Square(N-1)
    print(N*N)
Square(5)
print("---------------------")
def Square(N):
    if N==0:
        return
    print(N*N)
    Square(N-1)
Square(5)