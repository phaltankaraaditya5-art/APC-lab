contacts = {}

while True:
    print("\n1.Add 2.Search 3.Update 4.Delete 5.Display 6.Exit")
    choice = int(input("Enter choice: "))

    if choice == 1:
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        contacts[name] = phone

    elif choice == 2:
        name = input("Enter name: ")
        if name in contacts:
            print("Phone:", contacts[name])
        else:
            print("Contact not found")

    elif choice == 3:
        name = input("Enter name: ")
        if name in contacts:
            phone = input("Enter new phone number: ")
            contacts[name] = phone

    elif choice == 4:
        name = input("Enter name: ")
        if name in contacts:
            del contacts[name]

    elif choice == 5:
        print(contacts)

    elif choice == 6:
        break