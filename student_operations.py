from database import connect_db
from tabulate import tabulate

def add_student(name, age, grade, email):
    """Add a new student to the database."""
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO students (name, age, grade, email) VALUES (?, ?, ?, ?)", (name, age, grade, email))
    conn.commit()
    conn.close()
    print("Student added successfully.")

def view_students():
    """View all student records."""
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()
    conn.close()
    if rows:
        print(tabulate(rows, headers=["ID", "Name", "Age", "Grade", "Email"], tablefmt="grid"))
    else:
        print("No student records found.")

def update_student(student_id, name, age, grade, email):
    """Update a student's information."""
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE students SET name = ?, age = ?, grade = ?, email = ? WHERE id = ?
    """, (name, age, grade, email, student_id))
    conn.commit()
    conn.close()
    print("Student updated successfully.")

def delete_student(student_id):
    """Delete a student record."""
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM students WHERE id = ?", (student_id,))
    conn.commit()
    conn.close()
    print("Student deleted successfully.")

def search_student(keyword):
    """Search for students by name or ID."""
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT * FROM students WHERE name LIKE ? OR id LIKE ?
    """, (f"%{keyword}%", f"%{keyword}%"))
    rows = cursor.fetchall()
    conn.close()
    if rows:
        print(tabulate(rows, headers=["ID", "Name", "Age", "Grade", "Email"], tablefmt="grid"))
    else:
        print("No matching student records found.")
