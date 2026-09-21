file = open("employees.txt", "w")
file.write("E101,Shiva,IT,45000\n")
file.write("E102,Rehan,HR,55000\n")
file.write("E103,Varad,Finance,60000\n")
file.close()

def display_employees():
    file = open("employees.txt", "r")
    for line in file:
        print(line.strip())
    file.close()

def highest_paid():
    file = open("employees.txt", "r")
    lines = file.readlines()
    file.close()

    highest = lines[0].strip().split(",")
    for line in lines:
        parts = line.strip().split(",")
        if int(parts[3]) > int(highest[3]):
            highest = parts
    print("Highest paid employee:", highest)

def average_salary():
    file = open("employees.txt", "r")
    lines = file.readlines()
    file.close()

    total = 0
    for line in lines:
        parts = line.strip().split(",")
        total = total + int(parts[3])
    print("Average salary =", total / len(lines))

def above_salary(limit):
    file = open("employees.txt", "r")
    for line in file:
        parts = line.strip().split(",")
        if int(parts[3]) > limit:
            print(parts)
    file.close()

display_employees()
highest_paid()
average_salary()
above_salary(50000)