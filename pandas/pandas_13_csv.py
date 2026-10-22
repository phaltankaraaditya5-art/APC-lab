import pandas as pd
df = pd.read_csv("students.csv")
print("First 5 records:\n", df.head())
print("\nLast 5 records:\n", df.tail())

df["Total"] = df["Python"] + df["DBMS"] + df["Maths"]
df["Average"] = df["Total"] / 3

print("\nTotal and Average marks:\n", df[["Name", "Total", "Average"]])
print("\nStudents with average above 75:\n", df[df["Average"] > 75])
print("\nStudent with highest average:\n", df[df["Average"] == df["Average"].max()])

print("\nAverage marks per subject:")
print("Python:", df["Python"].mean())
print("DBMS:", df["DBMS"].mean())
print("Maths:", df["Maths"].mean())