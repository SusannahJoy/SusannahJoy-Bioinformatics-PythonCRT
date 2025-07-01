'''
1
4  9
16 25 36
49 64 81 100
'''
def print_square_pattern(rows):
    num=1
    for i in range(1,rows+1):
        for j in range(i):
            print(num**2,end=' ')
            num+=1
        print()
print_square_pattern(4)