n = int(input("How many products? "))
products = []

for i in range(n):
    name = input("Enter product name: ")
    price = float(input("Enter price: "))
    quantity = int(input("Enter quantity: "))
    products.append((name, price, quantity))

total_values = list(map(lambda p: (p[0], p[1] * p[2]), products))
above_1000 = list(filter(lambda p: (p[1] * p[2]) > 1000, products))
sorted_by_value = sorted(products, key=lambda p: p[1] * p[2])

print("Total value of each product:", total_values)
print("Products costing more than 1000:", above_1000)
print("Sorted by total value:", sorted_by_value)