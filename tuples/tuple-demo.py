mytuple = (10,20,30,40,50)
print(mytuple)
print(type(mytuple))
print("_______________________")

data = tuple(("C","C++","Java","Python")) #Tuple Constructor
print(data)
print(type(data))
print(data[0])
print(data[1])
print(data[2])

for i in mytuple:
    print(i)
    
for i in range(len(mytuple)):
    print(f'{i}->{mytuple[i]}')
    
print(type(data[1]))