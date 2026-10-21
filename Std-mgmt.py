
students = []

while True:
    print("\n1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Remove Student")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        roll = input("\nRoll number: ").strip()

        if not roll or any(s["roll"] == roll for s in students):
            print("\nInvalid or duplicate roll number!")
            continue

        name = input("\nName: ").strip()
        if not name:
            print("\nName cannot be empty!")
            continue

        age = input("\nAge: ").strip()
        if not age.isdigit() or int(age) < 1:
            print("\nInvalid age!")
            continue

        course = input("\nCourse: ").strip()
        if not course:
            print("\nCourse cannot be empty!")
            continue

        students.append({
            "roll": roll,
            "name": name,
            "age": int(age),
            "course": course
        })
        print("\nStudent added!")

    elif choice == "2":
        if not students:
            print("\nNo records found.")
        for s in students:
            print(s)

    elif choice == "3":
        roll = input("\nEnter roll number: ").strip()
        found = False

        for s in students:
            if s["roll"] == roll:
                print(s)
                found = True

        if not found:
            print("\nStudent not found.")

    elif choice == "4":
        roll = input("\nEnter roll number to remove: ").strip()
        found = False

        for s in students:
            if s["roll"] == roll:
                students.remove(s)
                print("\nStudent removed successfully!")
                found = True
                break

        if not found:
            print("\nStudent not found.")
            
    elif choice == "5":
        print("\nGoodbye!")
        break

    else:
        print("\nInvalid choice!")
