'''
      T
    T T E
  A T T E R
P A T T E R N
  A T T E R
    T T E
      T
'''
Str="PATTERN"
for i in range(len(Str)):
    if(i<=len(Str)//2):
        for j in range(len(Str)):
            if(j>=(len(Str)//2)-i and j<=(len(Str)//2)+i):
                print(Str[j],end=" ")
            else:
                print(" ",end=" ")
        print()
    else:
        k=(len(Str))-1-i
        for j in range(len(Str)):
            if(j>=(len(Str)//2)-k and j<=(len(Str)//2)+k):
                print(Str[j],end=" ")
            else:
                print(" ",end=" ")
        print()