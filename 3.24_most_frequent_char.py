s = "programming"
freq = {}
for ch in s:
    freq[ch] = freq.get(ch, 0) + 1
 
most_frequent = max(freq, key=freq.get)
print("Most frequent character:", most_frequent, "->", freq[most_frequent])