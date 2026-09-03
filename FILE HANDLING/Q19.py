# Calculate attendance percentage

with open("attendance.txt", "r") as file:
    for line in file:
        roll_no, name, attended, total = line.strip().split(",")

        attended = int(attended)
        total = int(total)

        percentage = (attended / total) * 100

        print(name, ":", percentage, "%")

        if percentage < 75:
            print("  Attendance below 75%")
