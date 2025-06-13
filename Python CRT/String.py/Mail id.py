'''
Write a python program to read mail id as input from the user and print user name and organization name based on mail id
(name@orgname.com)
'''
Mail_ID=input("Enter the Mail ID :")
List=Mail_ID.split('@')
print(f"User Name : {List[0]}")
Org=List[1]
List=Org.split('.')
print(f"Org Name : {List[0]}")