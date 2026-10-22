import pandas as pd
students = {}
for i in range(5):
    name = input("Name: ")
    marks = int(input("Marks: "))
    students[name] = marks

series = pd.Series(students)
print(series)
search = input("\nEnter student name to check marks: ")
print("Marks of", search, ":", series[search])

print("\nMax:", series.max(), "Min:", series.min(), "Avg:", series.mean())
print("Above 75:\n", series[series > 75])