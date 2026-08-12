s = "programming"
freq = {}
for ch in s:
    freq[ch] = freq.get(ch, 0) + 1
 
sorted_freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
print("Second most frequent character:", sorted_freq[1][0], "->", sorted_freq[1][1])