import random as r

print(r.randint(1,5))
print(r.randrange(1,5))

print(r.randint(1000,9999))

mylist = ['Pune','Bengaluru','Delhi','Hyderabad','Solapur','Mumbai']
print(r.choice(mylist))

r.shuffle(mylist)
print(mylist)