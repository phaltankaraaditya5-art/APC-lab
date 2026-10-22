from abc import ABC, abstractmethod

class Transport(ABC):
    @abstractmethod
    def calculate_fare(self, distance):
        pass


class Bus(Transport):
    def calculate_fare(self, distance):
        return distance * 2


class Train(Transport):
    def calculate_fare(self, distance):
        return distance * 1.5


class Taxi(Transport):
    def calculate_fare(self, distance):
        return distance * 10


class Flight(Transport):
    def calculate_fare(self, distance):
        return distance * 20


transports = [Bus(), Train(), Taxi(), Flight()]
distance = 100

for t in transports:
    print("Fare =", t.calculate_fare(distance))