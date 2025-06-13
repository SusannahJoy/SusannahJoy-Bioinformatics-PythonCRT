'''
Write a python program to print upper case alphabets from A to Z including thier ASCII values
'''
for i in range(1,27):
    print(chr(i+64),"--->",i+64)
print("-------------------")
for i in range(1,27):
    print(chr(i+96),"--->",i+96)
'''
Write a python program to read a character as input from the user ans print ASCII value of the character
'''
char=input("Enter the character :")
print(ord(char))