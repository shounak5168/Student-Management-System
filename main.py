from database import initialize_db
from student_operations import add_student, view_students, update_student, delete_student, search_student

def main():
    initialize_db()
    while True:
        print("\n--- Student Management System ---")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Search Student")
        print("6. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            name = input("Enter name: ")
            age = int(input("Enter age: "))
            grade = input("Enter grade: ")
            email = input("Enter email: ")
            add_student(name, age, grade, email)
        elif choice == "2":
            view_students()
        elif choice == "3":
            student_id = int(input("Enter student ID to update: "))
            name = input("Enter new name: ")
            age = int(input("Enter new age: "))
            grade = input("Enter new grade: ")
            email = input("Enter new email: ")
            update_student(student_id, name, age, grade, email)
        elif choice == "4":
            student_id = int(input("Enter student ID to delete: "))
            delete_student(student_id)
        elif choice == "5":
            keyword = input("Enter name or ID to search: ")
            search_student(keyword)
        elif choice == "6":
            print("Exiting the system...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
