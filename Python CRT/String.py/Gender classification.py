'''
Write a python program to take name as input including prefix(Mr/Ms)
print the gender classification of the name on the bases of prefix
'''
Str=input("Enter your name : ")
if(Str.startswith("Mr.")):
    print("Male")
elif(Str.startswith("Ms")):
    print("Female")
else:
    print("Invalid Name")