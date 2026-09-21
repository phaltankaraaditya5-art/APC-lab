students = {}

while True:
    print("\n1.Add 2.Update 3.Delete 4.Search 5.Display 6.Highest 7.Average 8.Exit")
    choice = int(input("Enter choice: "))

    if choice == 1:
        name = input("Enter name: ")
        marks = int(input("Enter marks: "))
        students[name] = marks

    elif choice == 2:
        name = input("Enter name: ")
        if name in students:
            marks = int(input("Enter new marks: "))
            students[name] = marks
        else:
            print("Student not found")

    elif choice == 3:
        name = input("Enter name: ")
        if name in students:
            del students[name]
        else:
            print("Student not found")

    elif choice == 4:
        name = input("Enter name: ")
        if name in students:
            print("Marks:", students[name])
        else:
            print("Student not found")

    elif choice == 5:
        print(students)

    elif choice == 6:
        if students:
            highest = max(students, key=students.get)
            print("Highest:", highest, "-", students[highest])

    elif choice == 7:
        if students:
            average = sum(students.values()) / len(students)
            print("Average marks =", average)

    elif choice == 8:
        break