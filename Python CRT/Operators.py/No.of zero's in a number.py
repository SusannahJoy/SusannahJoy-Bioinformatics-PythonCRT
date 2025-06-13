Num=int(input("Enter an integer :"))
Num_str=str(Num)
zero_count=0
for digit in Num_str:
    if digit=='0':
        zero_count+=1
print(f"No.of Zero's present in {Num} are {zero_count}")