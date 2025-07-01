'''
1st loop decides no of lines
2nd loop decides no of chars for each line
        *
      * *
    * * *
  * * * *
* * * * *
'''
n=int(input("Enter the value of n :"))
for i in range(1,n+1):
    for j in range(n-i):
         print(" ",end=' ')
    for k in range(i):
          print("*",end=' ')
    print()