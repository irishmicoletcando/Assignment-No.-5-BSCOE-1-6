# Program 1: PUP Grading System
# Section 8 of https://www.pup.edu.ph/studentservices/files/ThePUPStudentHandbook2014.pdf
# Create a program that will ask for grade percentage. Display the equivalent Grade/Mark and Description
# Example:
# Input grade: 87.6
# Grade/Mark: 1.75
# Description: Very Good

def ask_user_name():
    user_ = input("Enter name: ")
    print(f"Welcome to PUP Grading System, {user_}!")
    return user_

def grade_percentage():
    input_grade = float(input("Input Grade: "))
    if input_grade >= 97 and input_grade <= 100:
        print(f"Grade/Mark: 1.0 \nDescription: Excellent")
    elif input_grade >= 94 and input_grade <= 96:
        print(f"Grade/Mark: 1.25 \nDescription: Excellent")
    elif input_grade >= 91 and input_grade <= 93:
        print(f"Grade/Mark: 1.50 \nDescription: Very Good")
    elif input_grade >= 88 and input_grade <= 90:
        print(f"Grade/Mark: 1.75 \nDescription: Very Good")
    elif input_grade >= 85 and input_grade <= 87:
        print(f"Grade/Mark: 2.0 \nDescription: Very Good")
    elif input_grade >= 82 and input_grade <= 84:
        print(f"Grade/Mark: 2.25 \nDescription: Very Good")
    return input_grade
    

ask_user_name()
grade_percentage()