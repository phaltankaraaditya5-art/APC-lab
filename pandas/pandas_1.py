import pandas as pd
records = []

for i in range(5):
    id = input("Student ID: ")
    name = input("Name: ")
    python = int(input("Python marks: "))
    dbms = int(input("DBMS marks: "))
    maths = int(input("Maths marks: "))
    records.append({"Student_ID": id, "Name": name, "Python": python, "DBMS": dbms, "Maths": maths})

df = pd.DataFrame(records)
df["Total"] = df["Python"] + df["DBMS"] + df["Maths"]
df["Average"] = df["Total"] / 3

print(df)
print("\nAbove 75%:\n", df[df["Average"] > 75])