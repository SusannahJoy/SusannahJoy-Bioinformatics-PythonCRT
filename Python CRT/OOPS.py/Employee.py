class Employee():
    def __init__(self,empname,empID,designation,salary,deptname):
        print("Object is created")
        self.Empname=empname
        self.EmpID=empID
        self.Designation=designation
        self.Salary=salary
        self.Deptname=deptname
def Display_Details(self):
    print("Details of Employees :")
    print(f"Employee Name : {self.Empname}")
    print(f"Employee ID : {self.EmpID}")
    print(f"Employee's Designation : {self.Designation}")
    print(f"Employee's Salary : {self.Salary}")
    print(f"Employee's DeptName : {self.Deptname}")
E1=Employee('Scott','EMP101','Data Analyst',2500,'DeploymentTeam')
Display_Details(E1)