class BankAccount:

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        print("Account created for", self.name)

    def deposit(self, amount):
        self.balance = self.balance + amount
        print("Deposited:", amount)

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance = self.balance - amount
            print("Withdrew:", amount)

    def display_balance(self):
        print("Account Holder:", self.name)
        print("Current Balance:", self.balance)

    def __del__(self):
        print("Account of", self.name, "closed. Object destroyed.")


name = input("Enter account holder name: ")
initial_balance = float(input("Enter initial balance: "))

account = BankAccount(name, initial_balance)

while True:
    print("\n1.Deposit 2.Withdraw 3.Check Balance 4.Exit")
    choice = int(input("Enter choice: "))

    if choice == 1:
        amount = float(input("Enter amount to deposit: "))
        account.deposit(amount)

    elif choice == 2:
        amount = float(input("Enter amount to withdraw: "))
        account.withdraw(amount)

    elif choice == 3:
        account.display_balance()

    elif choice == 4:
        break

del account