class MobilePhone:
    _company = 'Samsung'
    _model = 'S24 Ultra'
    _price = 100000

    def setCompany(self,company):
        self._company = company

    def getCompany(self):
        return self._company

    def setModel(self,model):
        self._model = model

    def getModel(self):
        return self._model

    def setPrice(self,price):
        self._price = price

    def getPrice(self):
        return self._price

m = MobilePhone()
print(m.getCompany())
print(m.getModel())
print(m.getPrice())

m.setPrice(80000)
print(m.getCompany())
print(m.getModel())
print(m.getPrice())