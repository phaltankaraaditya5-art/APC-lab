class Vehicle:
    def start(self):
        print("Vehicle starting...")


class Car(Vehicle):
    def start(self):
        print("Car starts with a key ignition")


class Bike(Vehicle):
    def start(self):
        print("Bike starts with a kick or self-start")


class Bus(Vehicle):
    def start(self):
        print("Bus starts with a diesel engine ignition")


vehicles = [Car(), Bike(), Bus()]

for v in vehicles:
    v.start()