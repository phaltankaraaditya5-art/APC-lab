import pandas as pd
products = {}
for i in range(5):
    name = input("Name: ")
    price = float(input("Price: "))
    products[name] = price

series = pd.Series(products)
print(series)
print("\nAfter 10% increase:\n", series * 1.10)
print("Most expensive:", series.idxmax(), "-", series.max())
print("Above 1000:\n", series[series > 1000])