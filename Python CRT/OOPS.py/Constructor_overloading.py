'''
Write a python program to create a employee class and declare the states and 
create 5 objects using different constructors
'''
class Employee:
    #Constructor Overloading
    def __init__(self,Empname,EmpID,Job,Salary,Location,Dept):
        self.Empname=Empname
        self.EmpID=EmpID
        self.Job=Job
        self.Salary=Salary
        self.Location=Location
        self.Dept=Dept
        print("Hey...! I'm a Six Parameterized Constructor")
    def __init__(self,Empname,EmpID,Job,Salary,Location):
        self.Empname=Empname
        self.EmpID=EmpID
        self.Job=Job
        self.Salary=Salary
        self.Location=Location
        print("Hey...! I'm a Five Parameterized Constructor")
    def __init__(self,Empname,EmpID,Job,Salary):
        self.Empname=Empname
        self.EmpID=EmpID
        self.Job=Job
        self.Salary=Salary
        print("Hey...! I'm a Four Parameterized Constructor")
    def __init__(self,Empname,EmpID,Job):
        self.Empname=Empname
        self.EmpID=EmpID
        self.Job=Job
        print("Hey...! I'm a Three Parameterized Constructor")
    def __init__(self,Empname,EmpID):
        self.Empname=Empname
        self.EmpID=EmpID
        print("Hey...! I'm a Two Parameterized Constructor")
    def __init__(self,Empname):
        self.Empname=Empname
        print("Hey...! I'm a One Parameterized Constructor")
    def __init__(self):
        print("Hey...! I'm No Parameterized Constructor")
Emp2=Employee("Joy")
Emp3=Employee("Glory",101)
Emp4=Employee("Susannah",102,'HR')
Emp5=Employee("Srujanah",103,'Developer',25000)
Emp6=Employee("Susannah Joy",105,'Data Analyst',30000,'Bengaluru')