import numpy as np
marks_list = []
for i in range(20):
    m = int(input("Enter marks: "))
    marks_list.append(m)

marks = np.array(marks_list)

average = np.mean(marks)
above_average = marks[marks > average]
print("Class average:", average)
print("Students above average:", above_average)