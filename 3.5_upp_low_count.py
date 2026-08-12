s = "Hello World"
upper = lower = 0
for ch in s:
    if ch.isupper():
        upper += 1
    elif ch.islower():
        lower += 1
print("Uppercase count:", upper)
print("Lowercase count:", lower)