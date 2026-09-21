marks = {"Namokar": 95, "Jaydev": 90, "Sarthak": 78}

lowest_student = min(marks, key=marks.get)
print("Lowest marks:", lowest_student, "-", marks[lowest_student])