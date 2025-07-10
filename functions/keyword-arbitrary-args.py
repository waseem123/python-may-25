# KWARGS

def printdata(**x):
    print(x)
    print(type(x))
    print(x.items())
    
    for i,j in x.items():
        print(i,'->',j)
    
printdata(name="Usaid",city="Solapur",age=17)