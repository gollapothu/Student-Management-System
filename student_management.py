import json
import os

FILE_NAME = "students.json"

# Load students from file
def load_students():
    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, "r") as file:
                return json.load(file)
        except json.JSONDecodeError:
            print("Error: Corrupted student file. Starting fresh.")
            return []
    return []

# Save students to file
def save_students(students):
    with open(FILE_NAME, "w") as file:
        json.dump(students, file, indent=4)

# Add student
def add_student(students):
    roll_no = input("Enter Roll Number: ").strip()
    if not roll_no:
        print("Roll Number cannot be empty!")
        return

    for student in students:
        if student["roll_no"] == roll_no:
            print(f"Student with Roll No {roll_no} already exists!")
            return

    name = input("Enter Name: ").strip()
    department = input("Enter Department: ").strip()

    student = {
        "roll_no": roll_no,
        "name": name if name else "Unknown",
        "department": department if department else "Unknown",
        "marks": 0,
        "attendance": 0
    }

    students.append(student)
    save_students(students)
    print("Student Added Successfully!")

# View all students
def view_students(students):
    if not students:
        print("No Students Found!")
        return

    print("\n===== STUDENT LIST =====")
    for student in students:
        print("-" * 40)
        print("Roll No   :", student["roll_no"])
        print("Name      :", student["name"])
        print("Department:", student["department"])
        print("Marks     :", student["marks"])
        print("Attendance:", student["attendance"], "%")

# Search student
def search_student(students):
    roll_no = input("Enter Roll Number: ").strip()
    for student in students:
        if student["roll_no"] == roll_no:
            print("\nStudent Found")
            print("-" * 40)
            print("Roll No   :", student["roll_no"])
            print("Name      :", student["name"])
            print("Department:", student["department"])
            print("Marks     :", student["marks"])
            print("Attendance:", student["attendance"], "%")
            return
    print(f"Student with Roll No {roll_no} Not Found")

# Update student
def update_student(students):
    roll_no = input("Enter Roll Number: ").strip()
    for student in students:
        if student["roll_no"] == roll_no:
            print("\nLeave blank to keep old value")
            name = input("New Name: ").strip()
            department = input("New Department: ").strip()
            if name:
                student["name"] = name
            if department:
                student["department"] = department
            save_students(students)
            print("Student Updated Successfully")
            return
    print(f"Student with Roll No {roll_no} Not Found")

# Delete student
def delete_student(students):
    roll_no = input("Enter Roll Number: ").strip()
    for student in students:
        if student["roll_no"] == roll_no:
            students.remove(student)
            save_students(students)
            print("Student Deleted Successfully")
            return
    print(f"Student with Roll No {roll_no} Not Found")

# Add marks
def add_marks(students):
    roll_no = input("Enter Roll Number: ").strip()
    for student in students:
        if student["roll_no"] == roll_no:
            try:
                marks = int(input("Enter Marks (0-100): "))
                if 0 <= marks <= 100:
                    student["marks"] = marks
                    save_students(students)
                    print("Marks Updated")
                else:
                    print("Marks must be between 0 and 100")
            except ValueError:
                print("Invalid Marks")
            return
    print(f"Student with Roll No {roll_no} Not Found")

# Add attendance
def add_attendance(students):
    roll_no = input("Enter Roll Number: ").strip()
    for student in students:
        if student["roll_no"] == roll_no:
            try:
                attendance = int(input("Enter Attendance Percentage (0-100): "))
                if 0 <= attendance <= 100:
                    student["attendance"] = attendance
                    save_students(students)
                    print("Attendance Updated")
                else:
                    print("Attendance must be between 0 and 100")
            except ValueError:
                print("Invalid Attendance")
            return
    print(f"Student with Roll No {roll_no} Not Found")

# Grade calculator
def calculate_grade(marks):
    if marks >= 90: return "A+"
    elif marks >= 80: return "A"
    elif marks >= 70: return "B"
    elif marks >= 60: return "C"
    elif marks >= 50: return "D"
    return "F"

# Student report
def student_report(students):
    roll_no = input("Enter Roll Number: ").strip()
    for student in students:
        if student["roll_no"] == roll_no:
            marks = student["marks"]
            grade = calculate_grade(marks)
            print("\n===== STUDENT REPORT =====")
            print("Roll No   :", student["roll_no"])
            print("Name      :", student["name"])
            print("Department:", student["department"])
            print("Marks     :", marks)
            print("Grade     :", grade)
            print("Attendance:", student["attendance"], "%")
            print("=" * 30)
            return
    print(f"Student with Roll No {roll_no} Not Found")

# Class statistics
def class_statistics(students):
    if not students:
        print("No Students Found!")
        return

    total_marks = sum(student["marks"] for student in students)
    total_attendance = sum(student["attendance"] for student in students)
    count = len(students)

    avg_marks = total_marks / count
    avg_attendance = total_attendance / count

    print("\n===== CLASS STATISTICS =====")
    print("Total Students :", count)
    print("Average Marks  :", round(avg_marks, 2))
    print("Average Grade  :", calculate_grade(avg_marks))
    print("Average Attendance:", round(avg_attendance, 2), "%")
    print("=" * 30)

# Main Program
def main():
    students = load_students()
    while True:
        print("\n" + "=" * 40)
        print(" STUDENT MANAGEMENT SYSTEM ")
        print("=" * 40)
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Add Marks")
        print("7. Add Attendance")
        print("8. Student Report")
        print("9. Class Statistics")
        print("10. Exit")

        choice = input("Enter Choice: ").strip()
        if choice == "1": add_student(students)
        elif choice == "2": view_students(students)
        elif choice == "3": search_student(students)
        elif choice == "4": update_student(students)
        elif choice == "5": delete_student(students)
        elif choice == "6": add_marks(students)
        elif choice == "7": add_attendance(students)
        elif choice == "8": student_report(students)
        elif choice == "9": class_statistics(students)
        elif choice == "10":
            print("Thank You! Exiting...")
            break
        else:
            print("Invalid Choice")

if __name__ == "__main__":
    main()
