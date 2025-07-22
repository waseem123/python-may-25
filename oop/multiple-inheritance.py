class Watch:
    def setWatch(self, company, type):
        self.company = company
        self.type = type

    def get_watch(self):
        print(f'Company - {self.company}')
        print(f'Type - {self.type}')
        print(f'Basic features - Time and Date')


class Android:
    def getSmartFeatures(self):
        self.smart_features = ['Calling', 'SMS', 'Notifications', 'Fitness Tracker', 'Music']
        print(f'Smart Features - {self.smart_features}')


class SmartWatch(Watch, Android):
    def setSmartWatch(self, price, color):
        self.price = price
        self.color = color

    def getSmartWatch(self):
        print(f'Price - {self.price}')
        print(f'Color - {self.color}')

s = SmartWatch()
s.setWatch('boAt','Digital')
s.setSmartWatch(6500,'Black')
s.get_watch()
s.getSmartWatch()
s.getSmartFeatures()