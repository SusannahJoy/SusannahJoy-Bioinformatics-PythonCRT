'''
Sort a  list of dates provided in DD-MM-YYYY format chronologically.
Input:
An integer n(1<=n<=100)
a list of n strings in DD-MM-YYYY format
Output:
Sorted list of dates(earliest to latest)
Example:
Input:["12-05-2023","01-01-2022","15-08-2021"]
Output:["15-08-2021","01-01-2022","12-05-2023"]
'''
n=int(input("Enter the Number of integers:"))
Arr=[]
for i in range(n):
    temp=input("Enter the Date(DD-MM-YYYY):")
    Arr.append(temp)
print(f"Unsorted dates:{Arr}")
def date_key(d):
    date,month,year=d.split('-')
    return int(year),int(month),int(date)
Arr.sort(key=date_key)
print("Sorted dates:",Arr)