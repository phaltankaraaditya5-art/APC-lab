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
df["Total_Sales"] = df["Price"] * df["Quantity"]

print(df)
print("\nSales > 10000:\n", df[df["Total_Sales"] > 10000])
print("Max sales:\n", df[df["Total_Sales"] == df["Total_Sales"].max()])
print("Average sales:", df["Total_Sales"].mean())