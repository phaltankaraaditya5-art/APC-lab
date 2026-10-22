import pandas as pd
records = []

for i in range(5):
    id = input("Product ID: ")
    name = input("Name: ")
    cat = input("Category: ")
    price = float(input("Price: "))
    qty = int(input("Quantity: "))
    records.append({"Product_ID": id, "Product_Name": name, "Category": cat, "Price": price, "Quantity": qty})

df = pd.DataFrame(records)
df["Total_Amount"] = df["Price"] * df["Quantity"]

print(df)
print("\nHighest sale:\n", df[df["Total_Amount"] == df["Total_Amount"].max()])