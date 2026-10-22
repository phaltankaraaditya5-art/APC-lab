class Payment:
    def make_payment(self, amount):
        print("Processing payment...")


class UPIPayment(Payment):
    def make_payment(self, amount):
        print("Paid", amount, "via UPI")


class CardPayment(Payment):
    def make_payment(self, amount):
        print("Paid", amount, "via Card")


class WalletPayment(Payment):
    def make_payment(self, amount):
        print("Paid", amount, "via Wallet")


def process_payment(payment_obj, amount):
    payment_obj.make_payment(amount)


process_payment(UPIPayment(), 500)
process_payment(CardPayment(), 1500)
process_payment(WalletPayment(), 800)