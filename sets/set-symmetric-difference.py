set1 = {'Apple','Banana','Grapes','Orange','Mango','Watermelon'}
set2 = {'Strawberry','Kiwi','Dragonfruit','Watermelon','Mango'}

set3 = set1.symmetric_difference(set2)
print(set1)
print(set2)
print(set3)
print("___________________")

set1.symmetric_difference_update(set2)
print(set1)
print(set2)
print("___________________")