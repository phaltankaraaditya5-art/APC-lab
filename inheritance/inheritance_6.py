class BankAccount:
    def __init__(self, account_no, balance):
        self.account_no = account_no
        self.balance = balance

    def display(self):
        print("Account No:", self.account_no, "Balance:", self.balance)


class SavingsAccount(BankAccount):
    def __init__(self, account_no, balance, interest_rate):
        super().__init__(account_no, balance)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        return self.balance * (self.interest_rate / 100)


class PremiumSavingsAccount(SavingsAccount):
    def __init__(self, account_no, balance, interest_rate, benefits):
        super().__init__(account_no, balance, interest_rate)
        self.benefits = benefits

    def display(self):
        super().display()
        print("Interest Rate:", self.interest_rate, "Benefits:", self.benefits)


psa = PremiumSavingsAccount("A1", 100000, 5, "Free Locker, Priority Service")
psa.display()
print("Interest =", psa.calculate_interest())