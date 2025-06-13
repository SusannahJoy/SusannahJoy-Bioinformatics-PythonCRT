'''
Write Python program to:
--->Take a list of toy names(some repeated)
--->Remove duplicates
--->sort and display the final toy list
'''
size=int(input("Enter the Size of List :"))
Toy_List=[]
Newtoy_List=[]
for i in range(size):
    Temp=(input(f"Enter the element at {i} index :"))
    Toy_List.append(Temp)
print(Toy_List)
for i in Toy_List:
    if i not in Newtoy_List:
        Newtoy_List.append(i)
print("After removing Duplicates",Newtoy_List)
Newtoy_List.sort()
print("After sorting",Newtoy_List)