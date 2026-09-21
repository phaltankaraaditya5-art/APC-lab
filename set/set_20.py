python_students = {"Sartaj", "Salman", "Sufi"}
java_students = {"Salman", "Shahrukh", "Sufi"}

both_courses = python_students.intersection(java_students)
only_one_course = python_students.symmetric_difference(java_students)

print("Enrolled in both:", both_courses)
print("Enrolled in only one:", only_one_course)