students = []
def add_student():
    name = input("Enter student name: ")
    age = int(input("Enter student age: "))
    grade = input("Enter student grade: ")

    student = {
        'name': name,
        'age': age,
        'grade': grade
    }
    students.append(student)
    print("Student added successfully!\n")
def view_student(index):
    student = students[index]
    print(f"Name: {student['name']}")
    print(f"Age: {student['age']}")
    print(f"Grade: {student['grade']}\n")
def delete_student(index):
    del students[index]
    print("Student deleted successfully!\n")

def list_students():
    if len(students) == 0:
        print("No students in the database.\n")
    else:
        for index, student in enumerate(students):
            print(f"Index: {index}")
            print(f"Name: {student['name']}")
            print(f"Age: {student['age']}")
            print(f"Grade: {student['grade']}\n")

def update_student(index):
    student = students[index]

    print("Leave blank if you don't want to update a field.")

    name = input("Enter student name: ")
    if name:
        student['name'] = name

    age = input("Enter student age: ")
    if age:
        student['age'] = int(age)

    grade = input("Enter student grade: ")
    if grade:
        student['grade'] = grade

    print("Student updated successfully!\n")

while True:
    print("===== Student Database Program =====")
    print("1. Add Student")
    print("2. View Student")
    print("3. Delete Student")
    print("4. List Students")
    print("5. Update Student")
    print("0. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        add_student()
    elif choice == '2':
        index = int(input("Enter student index: "))
        view_student(index)
    elif choice == '3':
        index = int(input("Enter student index: "))
        delete_student(index)
    elif choice == '4':
        list_students()
    elif choice == '5':
        index = int(input("Enter student index: "))
        update_student(index)
    elif choice == '0':
        print("Exiting program. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.\n")