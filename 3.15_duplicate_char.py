s = "programming"
seen = set()
duplicates = set()
for ch in s:
    if ch in seen:
        duplicates.add(ch)
    else:
        seen.add(ch)
print("Duplicate characters:", duplicates)