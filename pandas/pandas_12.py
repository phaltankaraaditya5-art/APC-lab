import pandas as pd
students = {}
for i in range(5):
    name = input("Name: ")
    attendance = float(input("Attendance %: "))
    students[name] = attendance

series = pd.Series(students)
print(series)
print("\nAvg attendance:", series.mean())
print("Below 75%:\n", series[series < 75])
print("Above 90%:\n", series[series > 90])
print("Highest:", series.max())