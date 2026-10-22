import pandas as pd
employees = {}
for i in range(5):
    name = input("Name: ")
    salary = float(input("Salary: "))
    employees[name] = salary

series = pd.Series(employees)
print(series)
print("\nHighest:", series.max(), "Lowest:", series.min(), "Avg:", series.mean())
print("Above 50000:\n", series[series > 50000])