mytuple = ("C","C++","Java","Python","Javascript","Ruby")
print(mytuple)

# mytuple.insert(2,"Pearl")

mylist = list(mytuple)
mylist.append("Pearl")
print(mylist)
mytuple = tuple(mylist)
print(mytuple)

mytuple = mytuple + ("C#",)
print(mytuple)