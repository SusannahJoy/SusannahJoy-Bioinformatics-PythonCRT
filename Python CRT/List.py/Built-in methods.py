Cartoons=['Tom & Jerry','Doremon','Shinchan','Oggy & Cockroaches']
print(Cartoons)
print("After Appending : ")
Cartoons.append('Heidi')
print(Cartoons)
#Add another element
#append()----->adds the element at the end of the list
Cartoons.append('Smurfs')
print(Cartoons)
#insert()----->adds the element at the specific position
print("After Inserting : ")
Cartoons.insert(0,'ChotaBheem')
print(Cartoons)
#pop()-------->deletes the element from the list
print("After Poping : ")
Cartoons.pop()
print(Cartoons)
#pop(n)------->deletes the element given position
Cartoons.pop(0)
print(Cartoons)
#remove()----->removes the last element from the list
print("After Removing : ")
Cartoons.remove('Oggy & Cockroaches')
print(Cartoons)
#index()------>prints the position of the element
#print("After Indexing")
#X=Cartoons.index('Tom & Jerry')
#print(X)
print(Cartoons.index('Doremon'))
#reverse()---->prints the reverse order of the list
print("After Reversing : ")
Cartoons.reverse()
print(Cartoons)