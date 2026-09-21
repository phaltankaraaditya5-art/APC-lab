products = {"Pen": 20, "Book": 5, "Bag": 15, "Pencil": 8}

while True:
    print("\n1.Add 2.Update 3.Delete 4.Search 5.Low Stock 6.Exit")
    choice = int(input("Enter choice: "))

    if choice == 1:
        name = input("Enter product name: ")
        qty = int(input("Enter quantity: "))
        products[name] = qty

    elif choice == 2:
        name = input("Enter product name: ")
        if name in products:
            qty = int(input("Enter new quantity: "))
            products[name] = qty

    elif choice == 3:
        name = input("Enter product name: ")
        if name in products:
            del products[name]

    elif choice == 4:
        name = input("Enter product name: ")
        if name in products:
            print("Quantity:", products[name])
        else:
            print("Product not found")

    elif choice == 5:
        print("Products with quantity below 10:")
        for name, qty in products.items():
            if qty < 10:
                print(name, "-", qty)

    elif choice == 6:
        break