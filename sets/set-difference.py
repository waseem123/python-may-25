set1 = {'Apple','Banana','Grapes','Orange','Mango','Watermelon'}
set2 = {'Strawberry','Kiwi','Dragonfruit','Watermelon','Mango'}

set3=set1.difference(set2)
print(set1)
print(set2)
print(set3)
print("___________________")
set4 = set2-set1
print(set1)
print(set2)
print(set4)
print("___________________")

set2.difference_update(set1)
print(set1)
print(set2)