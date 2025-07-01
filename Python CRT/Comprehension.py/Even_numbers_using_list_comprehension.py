'''
Write a python program to print even numbers from 1 to n using list comprehension
'''
n=int(input("Enter an integer :"))
New=[i for i in range(n) if i%2==0]
print(New)