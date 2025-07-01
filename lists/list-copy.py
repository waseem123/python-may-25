mylist = ['India','Iran','Israel','America','Ukrain','Russia','North Korea']
datalist = mylist
print(mylist)
print(datalist)
mylist[2] = 'Japan'
print(mylist)
print(datalist)
yourlist = mylist.copy()
print(yourlist)
yourlist[3] = 'UK'
print(yourlist)
print(mylist)

mylist.reverse()
print(mylist)