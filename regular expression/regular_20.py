import re
text = input("Enter filenames separated by space: ")
extensions = re.findall(r"\.([A-Za-z0-9]+)(?=[\s,;]|$)", text)
print("File extensions:", extensions)