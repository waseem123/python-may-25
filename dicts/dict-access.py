mydict = {'rollno': 101, 
          'name': 'Bob', 
          'std': 1, 
          'div': 'B', 
          'school': 'InfoStack Coding School', 
          'marks': 98, 
          'address': 'Sadar Bazar Solapur'}
print(mydict)

print(mydict['marks'])
print(mydict.get('rollno'))
print("__________________")

print(mydict.keys())
print(mydict.values())
print(mydict.items())

for i in mydict:
    print(i)