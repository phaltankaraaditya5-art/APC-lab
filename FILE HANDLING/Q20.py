total_deposits = 0
total_withdrawals = 0
largest_transaction = 0

with open("transactions.txt", "r") as file:
    for line in file:
        transaction_type, amount = line.strip().split(",")

        amount = float(amount)

        if transaction_type == "D":
            total_deposits += amount
        elif transaction_type == "W":
            total_withdrawals += amount

        if amount > largest_transaction:
            largest_transaction = amount

final_balance = total_deposits - total_withdrawals

print("Total Deposits:", total_deposits)
print("Total Withdrawals:", total_withdrawals)
print("Final Balance:", final_balance)
print("Largest Transaction:", largest_transaction)
