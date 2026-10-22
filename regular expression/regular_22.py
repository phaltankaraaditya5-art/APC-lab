import re
invoice = """
Invoice No: INV-2026-0045
Date: 15-10-2026
Item 1: Laptop       Rs. 55,000.00
Item 2: Mouse        Rs. 500
Total Amount: INR 55,500.00

Invoice No: INV-2026-0046
Date: 16/10/2026
Item 1: Keyboard     Rs. 1,500.50
"""

invoice_numbers = re.findall(r"INV-\d{4}-\d{4}", invoice)
dates = re.findall(r"\b\d{2}[-/]\d{2}[-/]\d{4}\b", invoice)
amounts = re.findall(r"(?:Rs\.?|INR|\u20b9)\s?\d[\d,]*(?:\.\d+)?", invoice)

print("Invoice numbers:", invoice_numbers)
print("Dates:", dates)
print("Amounts:", amounts)