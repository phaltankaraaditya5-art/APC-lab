import pandas as pd
records = []

for i in range(5):
    id = input("Order ID: ")
    customer = input("Customer: ")
    product = input("Product: ")
    qty = int(input("Quantity: "))
    price = float(input("Price: "))
    discount = float(input("Discount: "))
    records.append({"Order_ID": id, "Customer": customer, "Product": product, "Quantity": qty, "Price": price, "Discount": discount})

df = pd.DataFrame(records)
df["Final_Amount"] = (df["Quantity"] * df["Price"]) - df["Discount"]

print(df)
print("\nAbove 5000:\n", df[df["Final_Amount"] > 5000])
print("Highest order:\n", df[df["Final_Amount"] == df["Final_Amount"].max()])
print("Average order value:", df["Final_Amount"].mean())