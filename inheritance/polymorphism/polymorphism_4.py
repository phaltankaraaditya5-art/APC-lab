class Animal:
    def sound(self):
        print("Animal makes a sound")


class Dog(Animal):
    def sound(self):
        print("Dog barks")


class Cat(Animal):
    def sound(self):
        print("Cat meows")


class Cow(Animal):
    def sound(self):
        print("Cow moos")


class Lion(Animal):
    def sound(self):
        print("Lion roars")


animals = [Dog(), Cat(), Cow(), Lion()]

for a in animals:
    a.sound()