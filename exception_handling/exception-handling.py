nr = int(input('ENTER A NUMBER - '))
dr = int(input('ENTER A NUMBER - '))
try:
    division = nr / dr
    print(division)
except ZeroDivisionError:
    print('Error : You can not divide any number by zero')