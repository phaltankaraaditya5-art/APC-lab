import pandas as pd
records = []

for i in range(5):
    id = input("Employee ID: ")
    name = input("Name: ")
    dept = input("Department: ")
    salary = float(input("Salary: "))
    exp = int(input("Experience: "))
    records.append({"Employee_ID": id, "Name": name, "Department": dept, "Salary": salary, "Experience": exp})

df = pd.DataFrame(records)

print(df)
print("\nSalary > 50000:\n", df[df["Salary"] > 50000])
print("Average salary:", df["Salary"].mean())
print("Highest salary:", df["Salary"].max())
print("Most experienced:\n", df[df["Experience"] == df["Experience"].max()])