file = open("attendance.txt", "w")
file.write("Shiva,80,90\n")
file.write("Rehan,60,90\n")
file.write("Varad,70,90\n")
file.close()

file = open("attendance.txt", "r")
lines = file.readlines()
file.close()

print("Students with attendance below 75%:")
for line in lines:
    parts = line.strip().split(",")
    name = parts[0]
    attended = int(parts[1])
    total = int(parts[2])
    percentage = (attended / total) * 100
    
    if percentage < 75:
        print(name, "-", round(percentage, 2), "%")