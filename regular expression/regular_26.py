import re
references = """
[1] A. Kumar and B. Singh (2019). Deep learning for crop disease detection.
    Journal of AI, 12(3). DOI: 10.1016/j.jai.2019.01.005.
    Contact: akumar@iitb.ac.in. URL: https://doi.org/10.1016/j.jai.2019.01.005
[2] P. Sharma (2021). Machine learning in healthcare. Health Informatics Review.
    DOI: 10.1145/3447548.3467123. Email: psharma@iisc.ac.in
    Available at https://example.org/papers/healthcare-ml
"""

dois = re.findall(r"10\.\d{4,9}/[^\s,;]+", references)
dois = [d.rstrip(".") for d in dois]
dois = list(dict.fromkeys(dois))

emails = re.findall(r"[\w.+-]+@[\w-]+(?:\.[\w-]+)+", references)

urls = re.findall(r"https?://\S+", references)

without_links = re.sub(r"https?://\S+|10\.\d{4,9}/\S+", " ", references)
years = re.findall(r"\b(?:19|20)\d{2}\b", without_links)

print("DOIs:", dois)
print("Years:", years)
print("Emails:", emails)
print("URLs:", urls)