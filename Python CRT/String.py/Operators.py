Str="Python"
print(f"length of {Str} is {len(Str)}")
#Accessing without index
for i in Str:
    print(i,end=" ")
print()
#Accessing with index
for i in range(len(Str)):
    print(Str[i],end=" ")
#type error because strings are immutable
str1="Students"
str1[4]="i"
for c in str1:
    print(c)