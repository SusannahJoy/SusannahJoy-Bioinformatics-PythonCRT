#Time Complexity=O(n^2)
Arr=[25,15,10,20,5]
print(f"Original Array : {Arr}")
for i in range(len(Arr)):
    Flag=False
    for j in range(len(Arr)-1):
        if (Arr[j]>Arr[j+1]):
            Arr[j],Arr[j+1]=Arr[j+1],Arr[j]
            print(Arr)
            Flag=True
    if Flag==False:
        break
print(Arr)
'''
Arr=[25,45,30,15,20,5,10,40,35,50]
count=0
print(f"Original Array: {Arr}")
n=len(Arr)
for i in range(1,n+1):
    Flag=False
    for j in range(n-1):
        if(Arr[j]>Arr[j+1]):
            Arr[j],Arr[j+1]=Arr[j+1],Arr[j]
            Flag=True
    if not Flag:
        break
    print(f"{i} iteration")
    print(Arr)
print(f"Sorted Array:{Arr}")
'''