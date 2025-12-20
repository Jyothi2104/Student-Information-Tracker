students = {}

def add_student():
    student_id = input("Enter student ID: ")
    name = input("Enter name: ")
    marks = float(input("Enter marks: "))
    students[student_id] = {"name": name, "marks": marks}
    print("Student added successfully!")

def view_students():
    if not students:
        print("No students found.")
        return
    for sid, info in students.items():
        print(f"ID: {sid}, Name: {info['name']}, Marks: {info['marks']}")

def average_marks():
    if not students:
        print("No students found.")
        return
    total = sum(info["marks"] for info in students.values())
    print("Average Marks:", total / len(students))

def main():
    while True:
        print("\n1. Add Student\n2. View Students\n3. Average Marks\n4. Exit")
        choice = input("Enter choice: ")
        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            average_marks()
        elif choice == "4":
            break
        else:
            print("Invalid choice!")

main()
