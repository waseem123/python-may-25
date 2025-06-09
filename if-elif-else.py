x = 100
y = 100
z = 1000

if x>y and x>z:
    print(f'{x} IS LARGER THAN {y} AND {z}')
elif y>x and y>z:
    print(f'{y} IS LARGER THAN {x} AND {z}')
elif z>x and z>y:
    print(f'{z} IS LARGER THAN {x} AND {y}')
else:
    print("ANY OF THE NUMBER IS EQUAL TO ANOTHER")