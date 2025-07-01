N=int(input("Enter the Value of n :"))
def NaturalNum(N):
    if N!=0:
        print(N)
        return NaturalNum(N-1)
NaturalNum(N)