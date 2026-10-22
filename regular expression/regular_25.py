import re
paragraph = "Rehan Pathan, Roll No: 101, Marks: 85. Varad Shinde, Roll No: 102, Marks: 92. Shivratna Jare, Roll No: 103, Marks: 78."
records = re.findall(r"([A-Z][a-z]+(?: [A-Z][a-z]+)*), Roll No: (\d+), Marks: (\d+)", paragraph)
for name, roll, marks in records:
    print("Name:", name, "| Roll No:", roll, "| Marks:", marks)