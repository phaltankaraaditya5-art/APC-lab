s = input("Enter a string: ")
freq = {}

for ch in s:
    if ch in freq:
        print("First repeating character:", ch)
        break
    freq[ch] = 1