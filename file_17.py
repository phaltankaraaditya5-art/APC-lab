file = open("students.csv", "w")
file.write("RollNo,Name,Marks\n")
file.write("101,Varad,85\n")
file.write("102,Shiva,92\n")
file.write("103,Rehan,78\n")
file.close()

file = open("students.csv", "r")
lines = file.readlines()
file.close()

print("All records:")
records = []
for line in lines[1:]:
    parts = line.strip().split(",")
    records.append(parts)
    print(parts)

highest = records[0]
for record in records:
    if int(record[2]) > int(highest[2]):
        highest = record
print("Highest marks:", highest)

total = 0
for record in records:
    total = total + int(record[2])
average = total / len(records)
print("Average marks =", average)

print("Students scoring above 80:")
for record in records:
    if int(record[2]) > 80:
        print(record)