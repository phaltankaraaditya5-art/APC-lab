class Media:
    def play(self):
        print("Playing media...")


class Audio(Media):
    def play(self):
        print("Playing audio track")


class Video(Media):
    def play(self):
        print("Playing video")


class Podcast(Media):
    def play(self):
        print("Playing podcast episode")


media_list = [Audio(), Video(), Podcast()]

for m in media_list:
    m.play()