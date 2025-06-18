mylist = ['Maaz','Muzammil', 'Zaid', 'Noman', 'Shravani', 'Sulaim', 'Ummehani', 'Ayesha','Shravani','Shravani','Shravani',]
print(mylist)

#delete the data from end of the list
mylist.pop()
print(mylist)
mylist.pop()
print(mylist)

#delete the data at specific index
mylist.pop(5)
print(mylist)

#delete the data by value
mylist.remove("Shravani")
print(mylist)

del mylist[3]
print(mylist)

mylist.clear()
print(mylist)

del mylist
print(mylist)