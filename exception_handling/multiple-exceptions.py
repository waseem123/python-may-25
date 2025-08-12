try:
    nr = int(input('ENTER A NUMBER - '))
    dr = int(input('ENTER A NUMBER - '))
    division = nr / dr
    print(division)

    mylist = ['Bata','Paragon','Mochi','Nike','Woodland','Puma']
    # print(mylist[9])
except ZeroDivisionError:
    print('Error : You can not divide any number by zero')
except ValueError:
    print('Error : Wrong input! Please provide only valid numberrs')
except:
    print('Error : Something went wrong')
else:
    print('Try block executed')
finally:
    print('Finally, The code has finished its execution')