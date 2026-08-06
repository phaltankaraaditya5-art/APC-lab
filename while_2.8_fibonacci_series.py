n = int(input("Enter n: "))
a = 0
b = 1
count = 0
while count < n:
    print(a)
    next_term = a + b
    a = b
    b = next_term
    count = count + 1