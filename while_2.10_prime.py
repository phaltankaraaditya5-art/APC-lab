n = int(input("Enter a number: "))
i = 2
is_prime = True

if n < 2:
    is_prime = False

while i * i <= n:
    if n % i == 0:
        is_prime = False
        break
    i = i + 1

if is_prime:
    print(n, "is prime")
else:
    print(n, "is not prime")