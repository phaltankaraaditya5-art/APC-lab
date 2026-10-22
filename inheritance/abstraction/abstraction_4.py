from abc import ABC, abstractmethod

class FoodOrder(ABC):
    @abstractmethod
    def calculate_bill(self):
        pass

    @abstractmethod
    def delivery_charge(self):
        pass


class RestaurantOrder(FoodOrder):
    def __init__(self, amount):
        self.amount = amount

    def calculate_bill(self):
        return self.amount

    def delivery_charge(self):
        return 0


class HomeDeliveryOrder(FoodOrder):
    def __init__(self, amount):
        self.amount = amount

    def calculate_bill(self):
        return self.amount

    def delivery_charge(self):
        return 50


ro = RestaurantOrder(500)
hd = HomeDeliveryOrder(500)

print("Restaurant Bill =", ro.calculate_bill() + ro.delivery_charge())
print("Home Delivery Bill =", hd.calculate_bill() + hd.delivery_charge())