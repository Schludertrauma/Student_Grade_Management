'''student_grade_management.py'''
'''This module provides functions to manage student grades, including adding, updating, and retrieving grades.'''
'''It also includes a function to calculate the average grade for a student.'''
'''This script is created only for exercise purposes.'''

# definition of functions


def welcome():
    import time
    print("Welcome to the Student Grade Management System!")
    time.sleep(2)


def add_grade(student_grades, student_name, grade):
    """Adds a grade for a student."""
    if student_name in student_grades:
        student_grades[student_name].append(grade)
    else:
        student_grades[student_name] = [grade]
    print(f"Grade {grade} added for {student_name}.")


def update_grade(student_grades, student_name, old_grade, new_grade):
    """Updates a specific grade for a student."""
    if student_name in student_grades and old_grade in student_grades[student_name]:
        index = student_grades[student_name].index(old_grade)
        student_grades[student_name][index] = new_grade
        print(
            f"Grade updated from {old_grade} to {new_grade} for {student_name}.")
    else:
        print(f"Grade {old_grade} not found for {student_name}.")


def get_grades(student_grades, student_name):
    """Retrieves all grades for a student."""
    if student_name in student_grades:
        return student_grades[student_name]
    else:
        print(f"No grades found for {student_name}.")
        return []


def calculate_average(student_grades, student_name):
    """Calculates the average grade for a student."""
    if student_name in student_grades and student_grades[student_name]:
        grades = student_grades[student_name]
        average = sum(grades) / len(grades)
        return average
    else:
        print(f"No grades found for {student_name}.")
        return None


def display_grades(student_grades):
    """Displays all students and their grades."""
    if not student_grades:
        print("No student grades available.")
        return
    for student, grades in student_grades.items():
        print(f"{student}: {grades}")


def main():
    welcome()
    student_grades = {}

    while True:
        print("\nOptions:")
        print("1. Add Grade")
        print("2. Update Grade")
        print("3. Get Grades")
        print("4. Calculate Average")
        print("5. Display All Grades")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter student name: ").strip().lower()
            grade = float(input("Enter grade: "))
            add_grade(student_grades, name, grade)
        elif choice == '2':
            name = input("Enter student name: ").strip()
            old_grade = float(input("Enter old grade: "))
            new_grade = float(input("Enter new grade: "))
            update_grade(student_grades, name, old_grade, new_grade)
        elif choice == '3':
            name = input("Enter student name: ").strip().lower()
            grades = get_grades(student_grades, name)
            print(f"Grades for {name}: {grades}")
        elif choice == '4':
            name = input("Enter student name: ").strip().lower()
            average = calculate_average(student_grades, name)
            if average is not None:
                print(f"Average grade for {name}: {average:.2f}")
        elif choice == '5':
            display_grades(student_grades)
        elif choice == '6':
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


# start the program


if __name__ == "__main__":
    main()
