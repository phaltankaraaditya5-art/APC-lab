def to_binary(n):
    if n == 0:
        return ""
    return to_binary(n // 2) + str(n % 2)

n = int(input("Enter a decimal number: "))

if n == 0:
    print("0")
else:
    print("Binary:", to_binary(n))