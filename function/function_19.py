def electricity_bill(units):
    if units <= 100:
        bill = units * 3
    elif units <= 200:
        bill = 100*3 + (units-100)*5
    else:
        bill = 100*3 + 100*5 + (units-200)*8
    return bill

units = int(input("Enter units consumed: "))
print("Electricity bill =", electricity_bill(units))