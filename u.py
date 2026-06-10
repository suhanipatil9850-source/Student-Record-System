students = []

def add_student():
    student_id = input("Enter Student ID: ")
    name = input("Enter Name: ")
    age = input("Enter Age: ")
    grade = input("Enter Grade: ")

    students.append({
        "id": student_id,
        "name": name,
        "age": age,
        "grade": grade
    })

    print("✅ Student added successfully!\n")


def view_students():
    if not students:
        print("No student records found.\n")
        return

    print("\n=== Student Records ===")
    for student in students:
        print(
            f"ID: {student['id']} | "
            f"Name: {student['name']} | "
            f"Age: {student['age']} | "
            f"Grade: {student['grade']}"
        )
    print()


def search_student():
    student_id = input("Enter Student ID to search: ")

    for student in students:
        if student["id"] == student_id:
            print("\nStudent Found:")
            print(student)
            return

    print("❌ Student not found.\n")


def update_student():
    student_id = input("Enter Student ID to update: ")

    for student in students:
        if student["id"] == student_id:
            student["name"] = input("Enter New Name: ")
            student["age"] = input("Enter New Age: ")
            student["grade"] = input("Enter New Grade: ")

            print("✅ Record updated successfully!\n")
            return

    print("❌ Student not found.\n")


def delete_student():
    student_id = input("Enter Student ID to delete: ")

    for student in students:
        if student["id"] == student_id:
            students.remove(student)
            print("✅ Student deleted successfully!\n")
            return

    print("❌ Student not found.\n")


def main():
    while True:
        print("===== Student Record System =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            update_student()
        elif choice == "5":
            delete_student()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("❌ Invalid choice.\n")


main()