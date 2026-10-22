import pandas as pd
df = pd.read_csv("employees.csv")
print("Employees from CSE department:\n", df[df["Department"] == "CSE"])

print("\nAverage salary:", df["Salary"].mean())
print("Highest salary:", df["Salary"].max())
print("Lowest salary:", df["Salary"].min())

print("\nEmployees with salary > 50000:\n", df[df["Salary"] > 50000])

print("\nDepartment-wise average salary:")
print(df.groupby("Department")["Salary"].mean())