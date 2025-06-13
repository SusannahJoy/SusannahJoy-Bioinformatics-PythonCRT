'''
Write a pytton program to read the input string fom the  user
a) reverse the string
b) convert the string into lower case
c) convert the string into upper case
d) convert the characters of string to lower case if in upper case and convert to upper case if in lower case
f) check if the string is starting with the letter a
g) print the count of the character a from the given string and replace all letter p to letter j
'''
Str=input("Enter the String :")
print(Str[::-1])
print(Str.lower())
print(Str.upper())
print(Str.swapcase())
print(Str.startswith('P'))
print(Str.count('P'))
Str=Str.lower()
print(Str.replace('p','j'))