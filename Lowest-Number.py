# Program 2: Find the lowest number
# Create a program that ask 3 numbers. 
# Find the lowest number using only if-else statement.
# Display the lowest number.

def ask_num(num1, num2, num3):
    if num1 < num2 and num1 < num3:
        print(f"The lowest number is {num1}.")
        return num1


number1 = float(input("Enter first number: "))
number2 = float(input("Enter second number: "))
number3 = float(input("Enter third number: "))

ask_num(num1 = number1, num2 = number2, num3 = number3)