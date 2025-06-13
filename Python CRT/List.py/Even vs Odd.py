'''
Write a Python program to:
--->Input a list of numbers
--->Create two new lists: one for even numbers and one for odd numbers
--->Display both lists
'''
size=int(input("Enter the Size of the List :"))
List=[]
for i in range(size):
    Temp=int(input(f"Enter the element at {i} index :"))
    List.append(Temp)
Even_List=[]
Odd_List=[]
for i in List:
    if i%2==0:
        Even_List.append(i)
    else:
        Odd_List.append(i)
print("Even Numbers",Even_List)
print("Odd Numbers",Odd_List)