class Product:
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price


class ElectronicProduct(Product):
    def __init__(self, product_id, name, price, brand, warranty):
        super().__init__(product_id, name, price)
        self.brand = brand
        self.warranty = warranty

    def final_price(self, discount_percent):
        return self.price - (self.price * discount_percent / 100)


ep = ElectronicProduct("P1", "Laptop", 60000, "Dell", "2 years")
print("Final Price =", ep.final_price(10))