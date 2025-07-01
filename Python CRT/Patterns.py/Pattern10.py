'''
      P
      A
      T
P A T T E R N
      E
      R
      N
'''
Str="PATTERN"
Length=len(Str)
for i in range(Length):
    for j in range(Length):
        if i==Length//2:
            print(f"{Str[j]}  ",end=" ")
        elif j==Length//2:
            print(f"{Str[i]}  ",end=" ")
        else:
            print("   ",end=" ")
    print()