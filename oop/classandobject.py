class Person:
    name = "Alexander"
    city = "New York"
    age = 2


p1 = Person()
print(p1.name)
print(p1.city)
print(p1.age)
print("________________________")

p2 = Person()
p2.name = "John"
p2.city = "London"
p2.age = 25

print(p2.name)
print(p2.city)
print(p2.age)

print("________________________")
p3 = Person()
p3.name = input("ENTER NAME OF PERSON - ")
p3.city = input("ENTER CITY OF PERSON - ")
p3.age = int(input("ENTER AGE OF PERSON - "))

print(p3.name)
print(p3.city)
print(p3.age)
