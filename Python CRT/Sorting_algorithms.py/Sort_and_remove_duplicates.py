'''
Problem:
Given a list of integers that may contain duplicates,
sort the list in ascending order and remove all duplicates.
Input:
A list of integers arr with length n

Output:
Sorted list with unique elements only

Input:[4,2,2,8,4,6]
Output:[2,4,6,8]
'''
list=[]
new_list=[]
n=int(input("Enter the number of integers:"))
for i in range(n):
    temp=input("Enter the Numbers:")
    list.append(temp)
print(list)
for i in range(len(list)):
    for j in range(len(list)-1):
        if (list[j]>list[j+1]):
            t=list[j]
            list[j]=list[j+1]
            list[j+1]=t
print(list)
for i in list:
    if i not in new_list:
        new_list.append(i)
print(new_list)