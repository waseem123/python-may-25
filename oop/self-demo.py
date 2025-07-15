class Employee:
    empid = 0
    empname = ""

    def setEmployee(self,empid,empname):
        self.empid = empid
        self.empname = empname

    def getEmployee(s):
        print(s.empid, s.empname)

e1 = Employee()
e2 = Employee()

e1.setEmployee(101,"Alex")
e2.setEmployee(102,"Alexa")

e1.getEmployee()
e2.getEmployee()