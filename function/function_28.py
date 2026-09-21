cart = []

def add_product(name, price, quantity):
    cart.append({"name": name, "price": price, "quantity": quantity})

def remove_product(name):
    global cart
    cart = [item for item in cart if item["name"] != name]

def calculate_subtotal():
    subtotal = 0

    for item in cart:
        subtotal = subtotal + (item["price"] * item["quantity"])

    return subtotal

def apply_coupon(subtotal, coupon_percent):
    return subtotal - (subtotal * coupon_percent / 100)

def calculate_gst(amount):
    return amount * 0.18

def generate_invoice(coupon_percent):
    subtotal = calculate_subtotal()
    after_coupon = apply_coupon(subtotal, coupon_percent)
    gst = calculate_gst(after_coupon)
    final_total = after_coupon + gst

    print("Subtotal =", subtotal)
    print("After coupon =", after_coupon)
    print("GST =", gst)
    print("Final total =", final_total)

n = int(input("How many products? "))

for i in range(n):
    name = input("Enter product name: ")
    price = float(input("Enter price: "))
    quantity = int(input("Enter quantity: "))
    add_product(name, price, quantity)

coupon_percent = float(input("Enter coupon discount percent: "))

generate_invoice(coupon_percent)