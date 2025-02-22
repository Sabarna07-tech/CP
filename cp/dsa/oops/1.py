class Employee:
    def __init__(self,empid=None, name=None, salary=None):
        self.empid = empid
        self.name = name
        self.salary = salary
    def setEmpid(self,empid):
        self.empid = empid
    def setSalary(self,salary):
        self.salary = salary
    def setName(self, name):
        self.name = name
    def getEmpid(self):
        return self.empid
    def getSalary(self):
        
        return self.salary
    def getName(self):
        return self.name
e1 = Employee()
e2 = Employee(1,"Rahul",4000)