# ------------------------------------------------------------------------------------------ #
# Title: Assignment07
# Desc: Classes and Objects
# Change Log: (Who, When, What)
#   ADawood,05/29/2024,Created Script
# ------------------------------------------------------------------------------------------ #

import json

# Constants
MENU = """
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course
    2. Show current data  
    3. Save data to a file
    4. Exit the program
----------------------------------------- 
"""

FILE_NAME = "Enrollments.json"

# Variables
menu_choice = ""
students = []

# Classes
class FileProcessor:
    """Class to handle file operations."""
    @staticmethod
    def read_data_from_file(file_name: str, student_data: list):
        """Reads data from a JSON file."""
        try:
            with open(file_name, 'r') as file:
                student_data.extend(json.load(file))
        except FileNotFoundError:
            print("File not found. Creating new file.")
        except json.JSONDecodeError:
            print("Error decoding JSON data.")

    @staticmethod
    def write_data_to_file(file_name: str, student_data: list):
        """Writes data to a JSON file."""
        try:
            serialized_students = [student.__dict__ for student in student_data]
            with open(file_name, 'w') as file:
                json.dump(serialized_students, file, indent=4)
            print("Data saved successfully.")
        except IOError as e:
            print(f"Error writing to file: {e}")

class IO:
    """Class to handle input/output operations."""
    @staticmethod
    def output_error_messages(message: str, error: Exception = None):
        """Outputs error messages."""
        print(message)
        if error:
            print(f"Error: {error}")

    @staticmethod
    def output_menu(menu: str):
        """Outputs the menu."""
        print(menu)

    @staticmethod
    def input_menu_choice():
        """Inputs menu choice from user."""
        return input("Enter your choice (1-4): ")

    @staticmethod
    def output_student_courses(student_data: list):
        """Outputs student data."""
        for student in student_data:
            print(f"First Name: {student.student_first_name}, Last Name: {student.student_last_name}, Course: {student.course_name}")

    @staticmethod
    def input_student_data(student_data: list):
        """Inputs student data."""
        student_first_name = input("Enter student's first name: ")
        student_last_name = input("Enter student's last name: ")
        course_name = input("Enter course name: ")
        student_data.append(Student(student_first_name, student_last_name, course_name))

class Person:
    """Base class for Person."""
    def __init__(self, student_first_name="", student_last_name="", course_name=""):
        self._student_first_name = student_first_name
        self._student_last_name = student_last_name
        self._course_name = course_name

    @property
    def student_first_name(self):
        """Property for student's first name."""
        return self._student_first_name

    @student_first_name.setter
    def student_first_name(self, value):
        """Setter for student's first name."""
        if not value:
            raise ValueError("First name cannot be empty.")
        self._student_first_name = value

    @property
    def student_last_name(self):
        """Property for student's last name."""
        return self._student_last_name

    @student_last_name.setter
    def student_last_name(self, value):
        """Setter for student's last name."""
        if not value:
            raise ValueError("Last name cannot be empty.")
        self._student_last_name = value

    @property
    def course_name(self):
        """Property for course name."""
        return self._course_name

    @course_name.setter
    def course_name(self, value):
        """Setter for course name."""
        if not value:
            raise ValueError("Course name cannot be empty.")
        self._course_name = value

class Student(Person):
    """Class representing a student."""
    def __init__(self, student_first_name="", student_last_name="", course_name=""):
        super().__init__(student_first_name, student_last_name, course_name)

    @staticmethod
    def extract_data(student):
        """Extracts data from student object."""
        return student

    @staticmethod
    def input_student():
        """Inputs student data."""
        student_first_name = input("Enter student's first name: ")
        student_last_name = input("Enter student's last name: ")
        course_name = input("Enter course name: ")
        return Student(student_first_name, student_last_name, course_name)

# Main program
def main():
    FileProcessor.read_data_from_file(FILE_NAME, students)
    while True:
        IO.output_menu(MENU)
        menu_choice = IO.input_menu_choice()
        if menu_choice == "1":
            student = Student.input_student()
            if student:
                students.append(Student.extract_data(student))
        elif menu_choice == "2":
            IO.output_student_courses(students)
        elif menu_choice == "3":
            FileProcessor.write_data_to_file(FILE_NAME, students)
        elif menu_choice == "4":
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()