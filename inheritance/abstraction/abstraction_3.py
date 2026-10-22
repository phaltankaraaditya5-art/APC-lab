from abc import ABC, abstractmethod

class BankAccount(ABC):
    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass


class SavingsAccount(BankAccount):
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        self.balance = self.balance + amount
        print("Deposited in Savings:", amount)

    def withdraw(self, amount):
        self.balance = self.balance - amount
        print("Withdrew from Savings:", amount)


class CurrentAccount(BankAccount):
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        self.balance = self.balance + amount
        print("Deposited in Current:", amount)

    def withdraw(self, amount):
        self.balance = self.balance - amount
        print("Withdrew from Current:", amount)


sa = SavingsAccount()
sa.deposit(5000)
sa.withdraw(1000)

ca = CurrentAccount()
ca.deposit(10000)
ca.withdraw(2000)