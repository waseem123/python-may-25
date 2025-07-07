employees = {
    'emp1':{
        'id':'101',
        'name':'abc',
        'salary':50000
    },
    'emp2':{
        'id':'102',
        'name':'pqr',
        'salary':55000
    },
    'emp3':{
        'id':'103',
        'name':'abc',
        'salary':60000
    }
}

print(employees)

e1 = {
        'id':'101',
        'name':'abc',
        'salary':50000
    }

e2 = {
        'id':'102',
        'name':'pqr',
        'salary':55000
    }

e3 = {
        'id':'103',
        'name':'abc',
        'salary':60000
    }

empdict = {
    'emp1':e1,
    'emp2':e2,
    'emp3':e3
}
print(empdict)



emplist = [e1,e2,e3]
for i in emplist:
    print(i)
    
print("+++++++++++++++++++++++")
print(employees.keys())
print(employees.values())
print(employees.items())

for i in employees.values():
    for j,k in i.items():
        print(j,k)