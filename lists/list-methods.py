mylist = ['Usaid','Maaz','Noman','Muzammil','Noman','Zaid','Noman','Amber','Noman','Misbha','Farah']
yourlist = ['Ayesha','Ummehani','Sulaim','Shravani']

print(mylist.count('Zaid'))
print(mylist.count('xyz'))
print(mylist.index('Noman'))
print(mylist.index('Noman'))
print(mylist.count('Noman'))
mylist.sort(reverse=True)
print(mylist)

data = [10,4,65,7,-25,-7,30]
data.sort(reverse=True)
print(data)

yourlist.extend(mylist)
print(mylist)
print(yourlist)

mylist = [100,200,300,400,500]
yourlist = [2,4,6,8,10]
result = mylist + yourlist
print(result)

print(mylist*2)


