x = ('j','k','l')
y = 100

mydict = dict.fromkeys(x,y)
print(mydict)

mydict = {'rollno': 101, 
          'name': 'Bob', 
          'std': 1, 
          'div': 'B', 
          'school': 'InfoStack Coding School', 
          'marks': 98, 
          'address': 'Sadar Bazar Solapur',
          'city':'Mumbai'}
print(mydict)

mydict.setdefault('city','Solapur')
print(mydict)