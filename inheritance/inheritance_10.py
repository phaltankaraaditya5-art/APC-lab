class Vehicle:
    def __init__(self, brand):
        self.brand = brand


class Car(Vehicle):
    def __init__(self, brand, doors):
        super().__init__(brand)
        self.doors = doors


class SportsCar(Car):
    def __init__(self, brand, doors, top_speed):
        super().__init__(brand, doors)
        self.top_speed = top_speed

    def display(self):
        print("Brand:", self.brand, "Doors:", self.doors, "Top Speed:", self.top_speed)


class Bike(Vehicle):
    def __init__(self, brand, gear_count):
        super().__init__(brand)
        self.gear_count = gear_count


class ElectricBike(Bike):
    def __init__(self, brand, gear_count, battery_range):
        super().__init__(brand, gear_count)
        self.battery_range = battery_range

    def display(self):
        print("Brand:", self.brand, "Gears:", self.gear_count, "Range:", self.battery_range, "km")


sc = SportsCar("Ferrari", 2, 350)
eb = ElectricBike("Ather", 0, 120)

sc.display()
eb.display()