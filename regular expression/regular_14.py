import re
text = input("Enter text: ")
urls = re.findall(r"https?://\S+", text)
print("Web addresses:", urls)