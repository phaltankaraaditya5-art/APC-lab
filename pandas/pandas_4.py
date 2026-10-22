import pandas as pd
records = []

for i in range(5):
    id = input("Patient ID: ")
    name = input("Name: ")
    age = int(input("Age: "))
    disease = input("Disease: ")
    charges = float(input("Medical Charges: "))
    records.append({"Patient_ID": id, "Name": name, "Age": age, "Disease": disease, "Medical_Charges": charges})

df = pd.DataFrame(records)

print(df)
print("\nAbove 60 years:\n", df[df["Age"] > 60])
print("Average charge:", df["Medical_Charges"].mean())
print("Max charge:", df["Medical_Charges"].max())
print("Charges > 50000:\n", df[df["Medical_Charges"] > 50000])