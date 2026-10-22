class Camera:
    def take_photo(self):
        print("Taking a photograph...")


class Phone:
    def make_call(self):
        print("Making a call...")


class Smartphone(Camera, Phone):
    def use_smartphone(self):
        self.take_photo()
        self.make_call()


sp = Smartphone()
sp.use_smartphone()