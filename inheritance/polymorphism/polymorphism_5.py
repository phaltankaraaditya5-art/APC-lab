class Notification:
    def send(self):
        print("Sending notification...")


class EmailNotification(Notification):
    def send(self):
        print("Sending Email notification")


class SMSNotification(Notification):
    def send(self):
        print("Sending SMS notification")


class PushNotification(Notification):
    def send(self):
        print("Sending Push notification")


notifications = [EmailNotification(), SMSNotification(), PushNotification()]

for n in notifications:
    n.send()