# Menu-Driven Student Information System

students = {}


def add_student():
    roll = input("Enter Roll No: ").strip()
    if not roll:
        print("Error: Roll No cannot be empty.")
        return
    name = input("Enter Name: ").strip()
    dept = input("Enter Department: ").strip()

    students[roll] = {"Name": name, "Department": dept}
    print("Student added successfully.")


def view_students():
    if not students:
        print("No student records found.")
        return
    print("\n--- Student Records ---")
    for roll, data in students.items():
        print(f"Roll No: {roll} | Name: {data['Name']} | Department: {data['Department']}")


def search_student():
    roll = input("Enter Roll No to search: ").strip()
    if roll in students:
        data = students[roll]
        print("\n--- Student Found ---")
        print(f"Roll No: {roll} | Name: {data['Name']} | Department: {data['Department']}")
    else:
        print("Student not found.")


def delete_student():
    roll = input("Enter Roll No to delete: ").strip()
    if roll in students:
        del students[roll]
        print("Student deleted successfully.")
    else:
        print("Student not found.")


def main():
    while True:
        print("\n--- Student Information System Menu ---")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main()


