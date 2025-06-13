'''
Write a Python program to:
--->Store 10 Student names
--->Swap the positions of any two students
--->Print the new seating arrangement
'''
size=10
List=[]
for i in range(size):
    Temp=input(f"Enter the element at {i} index :")
    List.append(Temp)
for i in List:
    List.swap(1,2)
    print("New List :",List)