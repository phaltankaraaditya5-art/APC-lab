class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __eq__(self, other):
        return self.price == other.price

    def __gt__(self, other):
        return self.price > other.price


p1 = Product("Phone", 20000)
p2 = Product("Tablet", 20000)

print("Equal price:", p1 == p2)
print("p1 costs more:", p1 > p2)