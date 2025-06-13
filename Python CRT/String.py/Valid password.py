'''
Write a python program to read a password from the user and check whether valid password or invalid
a)'''
'''
Write a python program to read name,contact number,mail-id and password and make sure that contact number has only 10 digits 
and mail should have a name@orgname.com and password should have atleast 3 uppercase alphabets 3 lowecase alphabets and 
3 special characters and 1 number and password length should not be less than 10
'''
'''
Write a python program to read a string as a input from the user and split the string into 3 equal halfs using slicing
'''
str=input("Enter a string :")
length=len(str)
if length%3==0:
    part_size=length//3
    part1=str[:part_size]
    part2=str[part_size:2*part_size]
    part3=str[2*part_size]
    print("Part 1:",part1)
    print("Part 2:",part2)
    print("Part 3:",part3)
else:
    print("Cannot split into 3 equal parts")