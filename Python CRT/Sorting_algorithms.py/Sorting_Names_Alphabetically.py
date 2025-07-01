'''
Problem:
Sort a list of names in alphabetical order using a sorting algorithm without built-in sort functions.
Input:
An integer n-number of names
A list of n names(strings of max length 100)

Output:
List of names sorted alphabetically 

Input:["Zara","John","Alex","Scott"]
Output:["Alex","John","Scott","Zara"]
'''
list=[]
num=int(input("Enter the number of names to be in the list:"))
for i in range(num):
    temp=input("Enter the name:")
    list.append(temp)
print(list)
for i in range(len(list)):
    for j in range(len(list)-1):
        if(list[j]>list[j+1]):
            t=list[j]
            list[j]=list[j+1]
            list[j+1]=t
print(list)