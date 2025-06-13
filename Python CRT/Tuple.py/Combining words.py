n=int(input("Enter the no.of words that you would like to find :"))
while(True):
    List=['Marker','Water','Wrist','Bread','Class','Home','Jim','Black','Crack']
    Tuple=('Pen','Bottle','Watch','Jam','Room','Theatre','Jam','Board','Jack')
    i=1
    while(i<=n):
        Word=input("Enter the word :")
        index=List.index(Word)
        print(f"{Word}-{Tuple[index]}")
        i+=1