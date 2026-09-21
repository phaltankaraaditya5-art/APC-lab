marks = {"Namokar": 95, "Jaydev": 90, "Sarthak": 78}

highest_student = max(marks, key=marks.get)
print("Highest marks:", highest_student, "-", marks[highest_student])