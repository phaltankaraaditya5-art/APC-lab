def consultation_charges():
    return 500

def lab_charges(tests):
    return tests * 300

def medicine_charges(amount):
    return amount

def room_charges(days, rate):
    return days * rate

def apply_discount(total, category):
    if category == "senior_citizen":
        return total - (total * 0.10)
    elif category == "student":
        return total - (total * 0.05)
    else:
        return total

def final_bill(tests, medicine_amount, days, room_rate, category):
    total = consultation_charges() + lab_charges(tests) + medicine_charges(medicine_amount) + room_charges(days, room_rate)
    total = apply_discount(total, category)
    return total

tests = int(input("Enter number of lab tests: "))
medicine_amount = float(input("Enter medicine charges: "))
days = int(input("Enter number of room days: "))
room_rate = float(input("Enter room rate per day: "))
category = input("Enter category (senior_citizen/student/other): ")

print("Final bill =", final_bill(tests, medicine_amount, days, room_rate, category))