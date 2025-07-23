class Bag:
    def setData(self, brand, color):
        self.brand = brand
        self.color = color

    def getData(self):
        print(f'BRAND - {self.brand}')
        print(f'COLOR - {self.color}')


class LaptopBag(Bag):
    def setData(self, brand, color, price, material):
        super().setData(brand, color)
        self.price = price
        self.material = material

    def getData(self):
        super().getData()
        print(f'PRICE - {self.price}')
        print(f'MATERIAL - {self.material}')


l = LaptopBag()
l.setData('American Tourister','Brown',3600, 'Leather')
l.getData()
