from student import Student
from database import add_student, view_students
from menu import menu

while True:
    menu()
    choice = input("Enter choice: ")

    if choice == "1":
        sid = input("Student ID: ")
        name = input("Name: ")
        age = input("Age: ")
        course = input("Course: ")
        marks = input("Marks: ")

        student = Student(sid, name, age, course, marks)
        add_student(student)

    elif choice == "2":
        view_students()

    elif choice == "3":
        break
