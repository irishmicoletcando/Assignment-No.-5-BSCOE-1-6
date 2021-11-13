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
    input_grade = input("Input Grade: ")
    if input_grade.upper() == "INC":
        print(f"Description: Incomplete")
    elif input_grade.upper() == "W":
        print(f"Description: Withdrawn")
    elif input_grade.upper() == "D":
        print(f"Description: Dropped")
    else:
        round_up = round(float(input_grade))
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
            print(f"Grade/Mark: 2.5 \nDescription: Satisfactory")
        elif round_up >= 76 and round_up <= 78:
            print(f"Grade/Mark: 2.75 \nDescription: Satisfactory")
        elif round_up == 75:
            print(f"Grade/Mark: 3.0 \nDescription: Passing")
        elif round_up >= 65 and round <= 74:
            print(f"Grade/Mark: 5.0 \nDescription: Failure")
        else:
            print("Please enter grades between 65 to 100 only.")
        return
    

ask_user_name()
grade_percentage()

# Had a lot of errors in the beginning and got confused on how I will place INC, W, D since I started with a float input
# Program completed!