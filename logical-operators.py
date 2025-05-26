a = 30
b = 25

print(a<b and a<28)
print(a<b and a>28)
print(a>b and a<28)
print(a>b and a>28)
print("_____________")

print(a<b or a<28)
print(a<b or a>28)
print(a>b or a<28)
print(a>b or a>28)
print("_____________")


print(not(a>b))
print(not(a<b))
print("_____________")

a = 30
b = 25
print(not(a>b and a<28))
print(not(a>b and a>28))
print(not(a>b) and a>28)
print(not(a>b) or not(a<28))
print(not(not(a>b) or not(a<28)))
print("_____________")