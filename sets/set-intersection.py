set1 = {'Apple','Banana','Grapes','Orange','Mango','Watermelon'}
set2 = {'Strawberry','Kiwi','Dragonfruit','Watermelon','Mango'}

set3 = set1.intersection(set2)
print(set1)
print(set2)
print(set3)
print("____________________")

set2.intersection_update(set1)
print(set1)
print(set2)