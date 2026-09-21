s = input("Enter a string: ")
freq = {}

for ch in s:
    if ch in freq:
        freq[ch] = freq[ch] + 1
    else:
        freq[ch] = 1

for ch in s:
    if freq[ch] == 1:
        print("First non-repeating character:", ch)
        break