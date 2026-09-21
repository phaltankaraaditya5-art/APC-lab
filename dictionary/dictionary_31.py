words = ["tiger", "lepord", "elephant", "ant", "lion", "goat"]
grouped = {}

for word in words:
    length = len(word)
    if length in grouped:
        grouped[length].append(word)
    else:
        grouped[length] = [word]

print(grouped)