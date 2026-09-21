def calculate_slab_charge(units):
    if units <= 100:
        return units * 3
    elif units <= 200:
        return 100*3 + (units-100)*5
    else:
        return 100*3 + 100*5 + (units-200)*8

def add_fixed_charges(amount):
    return amount + 50

def add_tax(amount):
    return amount + (amount * 0.05)

def apply_discount(amount, discount_percent):
    return amount - (amount * discount_percent / 100)

units = int(input("Enter units consumed: "))
discount_percent = float(input("Enter discount percent: "))

bill = calculate_slab_charge(units)
bill = add_fixed_charges(bill)
bill = add_tax(bill)
bill = apply_discount(bill, discount_percent)

print("Final electricity bill =", round(bill, 2))