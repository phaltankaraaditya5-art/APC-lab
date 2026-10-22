import numpy as np
marks_list = []
for i in range(10):
    m = int(input("Enter marks: "))
    marks_list.append(m)

marks = np.array(marks_list)
print("Highest marks:", np.max(marks))
print("Lowest marks:", np.min(marks))
print("Average marks:", np.mean(marks))
print("Median:", np.median(marks))
print("Standard deviation:", np.std(marks))