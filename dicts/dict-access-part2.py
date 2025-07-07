mydict = {'rollno': 101, 
          'name': 'Bob', 
          'std': 1, 
          'div': 'B', 
          'school': 'InfoStack Coding School', 
          'marks': 98, 
          'address': 'Sadar Bazar Solapur'}
print(mydict)

for i in mydict.keys():
    print(f'{i} -> {mydict[i]}')

print("_____________")

for i in mydict.values():
    print(i)
print("_____________")

for i in mydict.items():
    print(i)
print("_____________")

for i in mydict.items():
    print(f'{i[0]}-{i[1]}')
print("_____________")

for i,j in mydict.items():
    print(f'{i}-{j}')