'''
Write a python program to read a string as a input from the user and replace all vowerls with zero's
'''
Str=input("Enter the String :")
modified=""
for ch in Str:
    if ch in 'AEIOUaeiou':
        modified+='0'
    else:
        modified+=ch
print(modified)