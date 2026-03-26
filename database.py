import csv

file = "students.csv"

def add_student(student):
    with open(file, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([student.student_id, student.name, student.age, student.course, student.marks])

def view_students():
    with open(file, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)
