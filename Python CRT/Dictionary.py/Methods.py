EventCode={101:'Hackathon',102:'Coding',103:'Programming'}
print(EventCode)
#Modification
EventCode[102]='Coding Challenge'
print(EventCode)
#another Modification
JobRole={101:'Full Stack Developer',102:'Data Engineer',103:'Data Analyst',104:'Data scientist'}
print(JobRole)
JobRole[105]='Cloud Engineer'
JobRole[106]='Web Developer'
JobRole[107]='Bioinformatician'
print(JobRole)
#pop an item
JobRole.pop(101)
print(JobRole)
#delete any element using del keyword
del JobRole[102]
print(JobRole)
#len-returns the length of elements
print(len(JobRole))
#keys-prints the no.of keys
print(JobRole.keys())
#values-returns list of all values
print(JobRole.values())
#items-returns a list of key-value pairs(tuples)
print(JobRole.items())
#copy-returns the copy of dictionary
b=JobRole.copy()
print(b)
#update-returns one dictionary in another dictionary
Dict1={1:'a',2:'b',3:'c',4:'d'}
print(Dict1)
Dict2={5:'e',6:'f',7:'g'}
print(Dict2)
Dict1.update(Dict2)
print(Dict1)