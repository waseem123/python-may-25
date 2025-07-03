set1 = {'Apple','Banana','Grapes','Orange','Mango','Watermelon'}
set2 = {'Strawberry','Kiwi','Dragonfruit','Watermelon','Mango'}

#union will collect all set elements in new set
set3 = set2.union(set1)
print(set1)
print(set2)
print(set3)
print("__________________________")

#update will collect all set elements and update the existing set
set2.update(set1)
print(set1)
print(set2)