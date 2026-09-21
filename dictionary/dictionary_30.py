students = {"Jaydev": "CS", "Varad": "IT", "Pravin": "CS", "Anand": "Mech", "Nakul": "IT"}
grouped = {}

for name, dept in students.items():
    if dept in grouped:
        grouped[dept].append(name)
    else:
        grouped[dept] = [name]

print(grouped)