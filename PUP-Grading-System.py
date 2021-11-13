# Program 1: PUP Grading System
# Section 8 of https://www.pup.edu.ph/studentservices/files/ThePUPStudentHandbook2014.pdf
# Create a program that will ask for grade percentage. Display the equivalent Grade/Mark and Description
# Example:
# Input grade: 87.6
# Grade/Mark: 1.75
# Description: Very Good
import math

def ask_user_name():
    user_ = input("Enter name: ")
    print(f"Welcome to PUP Grading System, {user_}!")
    return user_

def grade_percentage():
    input_grade = float(input("Input Grade: "))
    round_up = math.floor(input_grade)
    if round_up >= 97 and round_up <= 100:
        print(f"Grade/Mark: 1.0 \nDescription: Excellent")
    elif round_up >= 94 and round_up <= 96:
        print(f"Grade/Mark: 1.25 \nDescription: Excellent")
    elif round_up >= 91 and round_up <= 93:
        print(f"Grade/Mark: 1.50 \nDescription: Very Good")
    elif round_up >= 88 and round_up <= 90:
        print(f"Grade/Mark: 1.75 \nDescription: Very Good")
    elif round_up >= 85 and round_up <= 87:
        print(f"Grade/Mark: 2.0 \nDescription: Good")
    elif round_up >= 82 and round_up <= 84:
        print(f"Grade/Mark: 2.25 \nDescription: Good")
    elif round_up >= 79 and round_up <= 81:
        print(f"Grade/Mark: 2.25 \nDescription: Satisfactory")
    elif round_up >= 76 and round_up <= 78:
        print(f"Grade/Mark: 2.25 \nDescription: Satisfactory")
    return input_grade
    

ask_user_name()
grade_percentage()