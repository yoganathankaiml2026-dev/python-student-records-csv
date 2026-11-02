# Student Record Management with List, Tuple, Dictionary, Text File and CSV
import csv

# List of dictionaries to store student records
students = []

n = int(input("Enter number of students: "))
for i in range(1, n + 1):
    print(f"\nStudent {i}")
    roll = input("Enter Roll No: ")
    name = input("Enter Name: ")
    dept = input("Enter Department: ")
    mark = int(input("Enter Mark: "))
    students.append({"RollNo": roll, "Name": name,
                     "Department": dept, "Mark": mark})

# Tuple example: fixed course details
course_name = input("\nEnter course name: ")
credits = int(input("Enter course credits: "))
course = (course_name, credits)
print("Course Tuple:", course)

# Write text file
with open("students.txt", "w") as file:
    for student in students:
        file.write(str(student) + "\n")

# Write CSV file
with open("students.csv", "w", newline="") as file:
    fields = ["RollNo", "Name", "Department", "Mark"]
    writer = csv.DictWriter(file, fieldnames=fields)
    writer.writeheader()
    writer.writerows(students)

# Read CSV file
print("\n--- Records from CSV ---")
with open("students.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row["RollNo"], row["Name"],
              row["Department"], row["Mark"])


# Sample Output:
#
# Enter number of students: 3
#
# Student 1
# Enter Roll No: 101
# Enter Name: Anitha
# Enter Department: CSE
# Enter Mark: 86
#
# Student 2
# Enter Roll No: 102
# Enter Name: Bala
# Enter Department: CSE
# Enter Mark: 91
#
# Student 3
# Enter Roll No: 103
# Enter Name: Chitra
# Enter Department: ECE
# Enter Mark: 78
#
# Enter course name: Python
# Enter course credits: 4
# Course Tuple: ('Python', 4)
#
# --- Records from CSV ---
# 101 Anitha CSE 86
# 102 Bala CSE 91
# 103 Chitra ECE 78
