class Bottle:
    material = ""
    quantity = 0
    price = 0

    def __init__(self, material="", quantity=0, price=0):
        print("Inside INIT Method")
        self.material = material
        self.quantity = quantity
        self.price = price

    def getdata(self):
        print(f'MATERIAL - {self.material}')
        print(f'QUANTITY - {self.quantity}')
        print(f'PRICE    - {self.price}')


b1 = Bottle("Plastic", 1, 20)
b1.getdata()

b2 = Bottle("Steel", 1, 200)
b2.getdata()

b3 = Bottle()
b3.getdata()

b4 = Bottle(quantity=2, material="Plastic", price=60)
b4.getdata()
