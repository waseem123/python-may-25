class box:
    def set_box(self, width, height):
        self.width = width
        self.height = height

    def get_box(self):
        print(f'Width - {self.width}')
        print(f'Height - {self.height}')


class ColoredBox(box):
    def set_box_color(self, color):
        self.color = color

    def get_colored_box(self):
        print(f'Color - {self.color}')


class ShippedBox(ColoredBox):
    def set_shipped_box(self, weight, shipping_cost):
        self.weight = weight
        self.shipping_cost = shipping_cost

    def get_shipped_box(self):
        print(f'Shipped weight- {self.weight}')
        print(f'Shipping cost- {self.shipping_cost}')


s = ShippedBox()
s.set_box(100, 100)
s.set_box_color("Brown")
s.set_shipped_box(5, 100)
s.get_box()
s.get_colored_box()
s.get_shipped_box()
