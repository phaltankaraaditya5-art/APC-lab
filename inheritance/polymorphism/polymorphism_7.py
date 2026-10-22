class BankAccount:
    def calculate_interest(self, balance):
        print("Interest not defined")


class SavingsAccount(BankAccount):
    def calculate_interest(self, balance):
        return balance * 0.04


class CurrentAccount(BankAccount):
    def calculate_interest(self, balance):
        return 0


class FixedDepositAccount(BankAccount):
    def calculate_interest(self, balance):
        return balance * 0.07


accounts = [SavingsAccount(), CurrentAccount(), FixedDepositAccount()]

for acc in accounts:
    print("Interest =", acc.calculate_interest(10000))