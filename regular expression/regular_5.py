import re
text = "Hello World\tPython\nRegex  Test\tDone"
print("Text:", repr(text))

spaces = re.findall(r" ", text)
tabs = re.findall(r"\t", text)
newlines = re.findall(r"\n", text)

print("Spaces =", len(spaces))
print("Tabs =", len(tabs))
print("Newlines =", len(newlines))

print("\nPositions:")
for m in re.finditer(r"[ \t\n]", text):
    print("Index", m.start(), "->", repr(m.group()))