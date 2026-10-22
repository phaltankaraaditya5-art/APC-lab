import re
s = input("Enter a string with extra spaces: ")
result = re.sub(r" {2,}", " ", s)
print("Before:", s)
print("After :", result)