'''
1
2 3
4 5 6
7 8 9 10
'''
def print_numbers(rows):
    num=1
    for i in range(1,rows+1):
        for j in range(i):
            print(num,end=' ')
            num+=1
        print()
print_numbers(4)