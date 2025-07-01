'''
Write a python program to create a linked list of size n ,value of n as input from the user
'''
class Node():
    def __init__(self,data):
        self.data=data
        self.next=None
        head=None
n=int(input("Enter the size of Linked List"))