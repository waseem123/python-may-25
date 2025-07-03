set1={'Dragonfruit', 'Mango', 'Orange', 'Strawberry', 'Kiwi', 'Banana', 'Grapes', 'Apple', 'Watermelon'}
set2 = {'Strawberry','Kiwi','Dragonfruit','Watermelon','Mango'}
set3 = {'Apple','Banana','Grapes','Orange','Mango','Watermelon'}

print(set1.issuperset(set2))
print(set2.issubset(set1))
print(set2.isdisjoint(set3))