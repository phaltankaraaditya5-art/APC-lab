def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

def calculate(func, a, b):
    return func(a, b)

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

print("Addition =", calculate(add, a, b))
print("Subtraction =", calculate(subtract, a, b))
print("Multiplication =", calculate(multiply, a, b))
print("Division =", calculate(divide, a, b))