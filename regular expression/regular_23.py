import re
code = '''x = 10  # store ten
print("Item #1")
y = 5
# full line comment
url = "http://site.com/#top"
text = """
This # is inside a multiline string
"""
'''

comments = re.findall(r"#.*", code)
print("Comments found by regex:")
for c in comments:
    print(" ", c)