class Student:
    rollno = 0
    name = ""
    subject1 = 0
    subject2 = 0
    subject3 = 0

    def getstudent(self):
        self.rollno = int(input("ENTER ROLL NUMBER - "))
        self.name = input("ENTER NAME OF STUDENT - ")
        self.subject1 = int(input("ENTER SUBJECT1 MARKS - "))
        self.subject2 = int(input("ENTER SUBJECT2 MARKS - "))
        self.subject3 = int(input("ENTER SUBJECT3 MARKS - "))

    def showstudent(self):
        print(self.rollno)
        print(self.name)

    def getresult(t):
        t.total = t.subject1 + t.subject2 + t.subject3
        t.percentage = t.total / 3
        print("Total: ", t.total)
        print("PERCENTAGE: ", t.percentage)


s1 = Student()
s1.getstudent()
s1.showstudent()
s1.getresult()
print("________________________")
s2 = Student()
s2.getstudent()
s2.showstudent()
s2.getresult()
