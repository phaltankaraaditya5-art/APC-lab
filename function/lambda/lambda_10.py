def is_prime(n):
    if n < 2:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False
    return True

n = int(input("How many numbers? "))
numbers = []

for i in range(n):
    num = int(input("Enter number: "))
    numbers.append(num)

primes = list(filter(lambda x: is_prime(x), numbers))

print("Prime numbers:", primes)