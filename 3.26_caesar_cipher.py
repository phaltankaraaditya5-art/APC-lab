s = input("Enter message: ")
shift = int(input("Enter shift value: "))
mode = input("Encrypt or Decrypt (e/d): ")

if mode == "d":
    shift = -shift

result = ""
for ch in s:
    if ch.isalpha():
        base = ord('A') if ch.isupper() else ord('a')
        new_ch = chr((ord(ch) - base + shift) % 26 + base)
        result = result + new_ch
    else:
        result = result + ch

print("Result:", result)