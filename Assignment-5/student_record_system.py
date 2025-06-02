import csv
import os

filename = "./student_record_system_utility/students.csv"

def initialize_file():
    if not os.path.exists(filename):
        with open(filename, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Name", "Age", "Grade"])

def add_student():
    name = input("Enter name: ")
    age = input("Enter age: ")
    grade = input("Enter grade: ")
    with open(filename, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([name, age, grade])

def search_student():
    name = input("Enter name to search: ")
    found = False
    with open(filename, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["Name"].lower() == name.lower():
                print("Found:", row)
                found = True
    if not found:
        print("Student not found.")

def delete_student():
    name = input("Enter name to delete: ")
    rows = []
    deleted = False
    with open(filename, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if row and row[0].lower() != name.lower():
                rows.append(row)
            else:
                deleted = True
    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(rows)
    if deleted:
        print("Student deleted.")
    else:
        print("Student not found.")


initialize_file()  # to create the file when it does not exists
while True:
    print("\nStudent Records Menu:")
    print("1. Add Student")
    print("2. Search Student")
    print("3. Delete Student")
    print("4. Exit")
    choice = input("Choose an option (1-4): ")

    if choice == "1":
        add_student()
    elif choice == "2":
        search_student()
    elif choice == "3":
        delete_student()
    elif choice == "4":
        break
    else:
        print("Invalid choice.")


