class Employee():
    def __init__(self,empname,empID,designation,salary,deptname):
        print("Object is created")
        self.EmpName=empname
        self.EmpID=empID
        self.Designation=designation
        self.Salary=salary
        self.Deptname=deptname
    def Get_Details(self):
        print(self.EmpName)
        print(self.EmpID)
        print(self.Designation)
        print(self.Salary)
        print(self.Deptname)
E1=Employee('Scott','EMP101','Data Analyst',2500,'DeploymentTeam')
E1.Get_Details()