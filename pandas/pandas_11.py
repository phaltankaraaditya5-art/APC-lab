import pandas as pd
patients = {}
for i in range(5):
    id = input("Patient ID: ")
    age = int(input("Age: "))
    patients[id] = age

series = pd.Series(patients)
print(series)
print("\nAvg age:", series.mean())
print("Oldest:", series.idxmax(), "-", series.max())
print("Youngest:", series.idxmin(), "-", series.min())
print("Above 60:\n", series[series > 60])