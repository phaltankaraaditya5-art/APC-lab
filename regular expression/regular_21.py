import re
text = "<html><body><h1>Hello,   World!!</h1><p>This  is   a   <b>sample</b> text...  &nbsp; with @#$ junk &amp; tags.</p></body></html>"
print("Original:\n", text)

text = re.sub(r"<[^>]+>", " ", text)
text = re.sub(r"&\w+;", " ", text)
text = re.sub(r"[^\w\s.,!?]", "", text)
text = re.sub(r"\s+", " ", text).strip()
print("\nCleaned:\n", text)