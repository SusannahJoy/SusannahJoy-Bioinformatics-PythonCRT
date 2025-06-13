'''
Write a python program to read a string as a input from the user and print the count of
a) upper case vowels
b) lower case vowels
c) upper case consonants
d) lower case consonants
'''
Str=input("Enter the string :")
U_Vowels,L_Vowels,U_Consonants,L_Consonants=0,0,0,0
for ch in Str:
    if(ch.isalpha() and ch.isupper()):
        if ch in 'AEIOU':
            U_Vowels+=1
        else:
            U_Consonants+=1
    if(ch.isalpha() and ch.islower()):
        if ch in 'aeiou':
            L_Vowels+=1
        else:
            L_Consonants+=1
print(f"Lower Case Vowel Count :{L_Vowels}")
print(f"Upper Case Vowel Count :{U_Vowels}")
print(f"Lower Case Consonant Count :{L_Consonants}")
print(f"Upper Case Consonant Count :{U_Consonants}")

#Alternative Method
Str=input("Enter the String:")
U_vowels,L_vowels,U_consonants,L_consonants=0,0,0,0
for ch in Str:
    if(ch>='A' and ch<='Z'):
        if ch in 'AEIOU':
            U_vowels+=1
        else:
            U_consonants+=1
    if(ch>='a' and ch<='z'):
        if ch in 'aeiou':
            L_vowels+=1
        else:
            L_consonants+=1
print(f"Lower case Vowel Count:{L_vowels}")
print(f"Upper case Vowel Count:{U_vowels}")
print(f"Lower case Consonants Count:{L_consonants}")
print(f"Upper case Consonants Count:{U_consonants}")