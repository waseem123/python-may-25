class Wood:
    def setWood(self, type, price):
        self.type = type
        self.price = price

    def getWood(self):
        print(f'Type - {self.type}')
        print(f'Price - {self.price}')


class Door(Wood):
    def setDoor(self, size, color):
        self.size = size
        self.color = color

    def getDoor(self):
        print(f'Size - {self.size}')
        print(f'Color - {self.color}')


class Sofa(Wood):
    def setSofa(self, color, design):
        self.color = color
        self.design = design

    def getSofa(self):
        print(f'Design - {self.design}')
        print(f'Color - {self.color}')


class Table(Wood):
    def setTable(self, table_type, height, length):
        self.table_type = table_type
        self.height = height
        self.length = length

    def getTable(self):
        print(f'Type - {self.table_type}')
        print(f'Height - {self.height}')
        print(f'Length - {self.length}')


d = Door()
s = Sofa()
t = Table()

d.setWood("Sagwan Wood",2000)
d.setDoor("7 X 3","Brown")

s.setWood("Sandal Wood",20000)
s.setSofa("Red","L Shaped Sofa")

t.setWood("Sagwan Wood",1500)
t.setTable("Computer Table",3,4)

d.getWood()
d.getDoor()
print("______________")

t.getWood()
t.getTable()
print("______________")

s.getWood()
s.getSofa()
print("______________")