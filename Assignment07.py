# ------------------------------------------------------------------------------------------ #
# Title: Assignment07
# Desc: Classes and Objects
# Change Log: (Who, When, What)
#   ADawood,05/29/2024,Created Script
# ------------------------------------------------------------------------------------------ #

import json

class Person:
    """
    A class representing a person.
    """

    def __init__(self, first_name="", last_name=""):
        if not isinstance(first_name, str):
            raise ValueError("First name should be a string.")
        if not isinstance(last_name, str):
            raise ValueError("Last name should be a string.")
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def to_json(self):
        """Returns JSON representation of the person"""
        return {"first_name": self.first_name, "last_name": self.last_name}

    @staticmethod
    def from_json(json_data):
        """Creates a Person object from JSON data"""
        return Person(json_data["first_name"], json_data["last_name"])

    @staticmethod
    def from_csv(csv_data):
        """Creates a Person object from comma-separated data"""
        first_name, last_name = csv_data.split(',')
        return Person(first_name.strip(), last_name.strip())

class Student(Person):
    """
    A class representing a student.
    Inherits from the Person class.
    """

    def __init__(self, student_first_name="", student_last_name="", course_name=""):
        super().__init__(student_first_name, student_last_name)
        if not isinstance(course_name, str):
            raise ValueError("Course name should be a string.")
        self.course_name = course_name

    def __str__(self):
        return f"Student: {super().__str__()}, Course: {self.course_name}"

    def to_json(self):
        """Returns JSON representation of the student"""
        person_json = super().to_json()
        person_json["course_name"] = self.course_name
        return person_json

    @staticmethod
    def from_json(json_data):
        """Creates a Student object from JSON data"""
        person = Person.from_json(json_data)
        return Student(person.first_name, person.last_name, json_data["course_name"])

    @staticmethod
    def from_csv(csv_data):
        """Creates a Student object from comma-separated data"""
        person = Person.from_csv(csv_data)
        return Student(person.first_name, person.last_name, csv_data[2].strip())

class FileProcessor:
    """
    A class to handle file processing operations.
    """

    @staticmethod
    def read_data_from_file(file_name: str, student_data: list):
        """
        Read data from a JSON file and load it into a list.

        Parameters:
            file_name (str): The name of the file to read from.
            student_data (list): The list to store the loaded data.
        """
        try:
            with open(file_name, "r") as file:
                data = json.load(file)
                for item in data:
                    student_data.append(Student.from_json(item))
        except Exception as e:
            IO.output_error_messages("Error reading file:", e)

    @staticmethod
    def write_data_to_file(file_name: str, student_data: list):
        """
        Write data from a list to a JSON file.

        Parameters:
            file_name (str): The name of the file to write to.
            student_data (list): The list containing data to write.
        """
        try:
            with open(file_name, "w") as file:
                json.dump([student.to_json() for student in student_data], file)
        except Exception as e:
            IO.output_error_messages("Error writing to file:", e)

class IO:
    """
    A class to handle input/output operations.
    """

    @staticmethod
    def output_error_messages(message: str, error: Exception = None):
        """
        Output error messages along with the exception details.

        Parameters:
            message (str): The error message to display.
            error (Exception): The exception object.
        """
        print(message)
        if error:
            print("Error details:", error)

    @staticmethod
    def output_menu(menu: str):
        """
        Output the menu to the console.

        Parameters:
            menu (str): The menu string to display.
        """
        print(menu)

    @staticmethod
    def input_menu_choice():
        """
        Prompt the user to input a menu choice.

        Returns:
            str: The user's menu choice.
        """
        return input("What would you like to do: ")

    @staticmethod
    def output_student_courses(student_data: list):
        """
        Output the student data to the console.

        Parameters:
            student_data (list): The list containing student data.
        """
        print("-" * 50)
        for student in student_data:
            print(f'Student {student.first_name} {student.last_name} is enrolled in {student.course_name}')
        print("-" * 50)

    @staticmethod
    def input_student_data(student_data: list):
        """
        Prompt the user to input student data and add it to the list.

        Parameters:
            student_data (list): The list to store the student data.
        """
        try:
            student_first_name = input("Enter the student's first name: ")
            if not student_first_name.isalpha():
                raise ValueError("The first name should only contain alphabets.")
            student_last_name = input("Enter the student's last name: ")
            if not student_last_name.isalpha():
                raise ValueError("The last name should only contain alphabets.")
            course_name = input("Please enter the name of the course: ")
            student_data.append(Student(student_first_name, student_last_name, course_name))
            print(f"You have registered {student_first_name} {student_last_name} for {course_name}.")
        except ValueError as e:
            IO.output_error_messages("Value Error:", e)
        except Exception as e:
            IO.output_error_messages("Error:", e)

# Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course
    2. Show current data  
    3. Save data to a file
    4. Exit the program
----------------------------------------- 
'''
FILE_NAME: str = "Enrollments.json"

# Variables
student_data: list = []

# Initial file read
FileProcessor.read_data_from_file(FILE_NAME, student_data)

# Menu loop
while True:
    IO.output_menu(MENU)
    menu_choice = IO.input_menu_choice()

    if menu_choice == "1":
        IO.input_student_data(student_data)

    elif menu_choice == "2":
        IO.output_student_courses(student_data)

    elif menu_choice == "3":
        FileProcessor.write_data_to_file(FILE_NAME, student_data)
        IO.output_student_courses(student_data)

    elif menu_choice == "4":
        break

    else:
        print("Please only choose option 1, 2, 3, or 4")

print("Program Ended")