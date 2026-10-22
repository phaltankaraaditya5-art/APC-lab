import pandas as pd
df = pd.read_csv("patients.csv")
print("Patients above 60 years:\n", df[df["Age"] > 60])
print("\nAverage medical expense:", df["Medical_Expense"].mean())
print("\nPatient with highest medical expense:\n", df[df["Medical_Expense"] == df["Medical_Expense"].max()])

print("\nPatient count for each disease:")
print(df["Disease"].value_counts())

print("\nPatients with medical expense > 50000:\n", df[df["Medical_Expense"] > 50000])