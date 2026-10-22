class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        print(self.name, "makes a sound")


class Dog(Animal):
    def sound(self):
        print(self.name, "barks")


class Cat(Animal):
    def sound(self):
        print(self.name, "meows")


class Cow(Animal):
    def sound(self):
        print(self.name, "moos")


d = Dog("Tommy")
c = Cat("Kitty")
cow = Cow("Ganga")

d.sound()
c.sound()
cow.sound()