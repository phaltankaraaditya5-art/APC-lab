import re
post = input("Enter a social media post: ")
hashtags = re.findall(r"#\w+", post)
print("Hashtags:", hashtags)