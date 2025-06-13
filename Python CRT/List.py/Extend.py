#extend------>merging of 2 lists
Prog_Lang=['C','C++','Java','Python','Go-Lang']
Database=['SQL','NO_SQL']
print(Prog_Lang)
Front_End=['HTML','CSS','JAVASCRIPT','REACT JS','ANGULAR JS']
print(Front_End)
Prog_Lang.extend(Front_End)
print(Prog_Lang)
Prog_Lang.extend(Database)
print(Prog_Lang)
print(Prog_Lang.count('HTML'))