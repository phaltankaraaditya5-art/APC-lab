def calculate_bill(prices, quantities, discount_percent):
    total = 0

    for i in range(len(prices)):
        total = total + (prices[i] * quantities[i])

    discount = total * (discount_percent / 100)
    final_bill = total - discount
    return final_bill

n = int(input("How many items? "))
prices = []
quantities = []

for i in range(n):
    price = float(input("Enter price: "))
    qty = int(input("Enter quantity: "))
    prices.append(price)
    quantities.append(qty)

discount_percent = float(input("Enter discount percent: "))

print("Final bill =", calculate_bill(prices, quantities, discount_percent))