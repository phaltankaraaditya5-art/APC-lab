balance = 0
transaction_history = []

def deposit(amount):
    global balance
    balance = balance + amount
    transaction_history.append("Deposited: " + str(amount))

def withdraw(amount):
    global balance

    if amount > balance:
        print("Insufficient balance")
    else:
        balance = balance - amount
        transaction_history.append("Withdrew: " + str(amount))

def balance_enquiry():
    print("Current balance =", balance)

def show_history():
    for txn in transaction_history:
        print(txn)

while True:
    print("\n1.Deposit 2.Withdraw 3.Balance 4.History 5.Exit")
    choice = int(input("Enter choice: "))

    if choice == 1:
        amount = float(input("Enter amount to deposit: "))
        deposit(amount)

    elif choice == 2:
        amount = float(input("Enter amount to withdraw: "))
        withdraw(amount)

    elif choice == 3:
        balance_enquiry()

    elif choice == 4:
        show_history()

    elif choice == 5:
        break