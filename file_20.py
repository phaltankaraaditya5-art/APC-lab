file = open("transactions.txt", "w")
file.write("deposit,5000\n")
file.write("withdraw,2000\n")
file.write("deposit,3000\n")
file.write("withdraw,1000\n")
file.close()

file = open("transactions.txt", "r")
lines = file.readlines()
file.close()

total_deposit = 0
total_withdraw = 0
largest = 0

for line in lines:
    parts = line.strip().split(",")
    txn_type = parts[0]
    amount = int(parts[1])

    if txn_type == "deposit":
        total_deposit = total_deposit + amount
    else:
        total_withdraw = total_withdraw + amount

    if amount > largest:
        largest = amount

balance = total_deposit - total_withdraw

print("Total deposits =", total_deposit)
print("Total withdrawals =", total_withdraw)
print("Final balance =", balance)
print("Largest transaction =", largest)