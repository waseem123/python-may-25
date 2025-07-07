mydict = {'rollno': 101, 
          'name': 'Bob', 
          'std': 1, 
          'div': 'B', 
          'school': 'InfoStack Coding School', 
          'marks': 98, 
          'address': 'Sadar Bazar Solapur'}
print(mydict)

mydict.popitem() #end value delete from the dict
print(mydict)

mydict.pop('div') # delete specific key-value
print(mydict)

del mydict['rollno']
print(mydict)

mydict.clear()
print(mydict)

del mydict
print(mydict)