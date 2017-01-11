class Bicycle(object):
    def __init__(self, name, weight, cost, quantity):
        self.name = name
        self.weight = weight
        self.cost = cost
        self.quantity = quantity
        
class Shop(object):
    def __init__(self, name, margin):
        self.name = name
        self.margin = margin
        
class Customers(object):
    def __init__(self, name, fund):
        self.name = name
        self.fund = fund
