import pandas as pd
records = []

for i in range(5):
    id = input("Student ID: ")
    name = input("Name: ")
    dept = input("Department: ")
    total = int(input("Total Classes: "))
    attended = int(input("Classes Attended: "))
    records.append({"Student_ID": id, "Name": name, "Department": dept, "Total_Classes": total, "Classes_Attended": attended})

df = pd.DataFrame(records)
df["Attendance_Percentage"] = (df["Classes_Attended"] / df["Total_Classes"]) * 100

print(df)
print("\nBelow 75%:\n", df[df["Attendance_Percentage"] < 75])