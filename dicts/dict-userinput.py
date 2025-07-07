id = int(input("ENTER ID - "))
name = input("ENTER NAME - ")
salary = int(input("ENTER SALARY - "))

emp = {
    'empId':id,
    'empName':name,
    'empSalary':salary
}

print(emp)
designation = input('ENTER DESIGNATION - ')
emp['empDesignation'] = designation
print(emp)