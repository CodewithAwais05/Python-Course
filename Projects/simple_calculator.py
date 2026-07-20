#   Question:  2. Simple Calculator

# Take two numbers and an operator (+, -, *, /) as input
# Use a function for each operation
# Handle division by zero gracefully
# Stretch: Loop so user can keep calculating until they type "no". Support % and **.

def addition(num1, num2):
    print("Result:  ", num1 + num2)

def subtraction(num1, num2):
    print("Result:  ", num1 - num2)

def multiplication(num1, num2):
    print("Result:  ", num1 * num2)

def division(num1, num2):
    if num2 != 0:
        print("Result:  ", num1 / num2)
    else:
        print("Cannot perform division by zero!!!")

def modulus(num1, num2):
    if num2 != 0:
        print("Result:  ", num1 % num2)
    else:
        print("Cannot perform modulus by zero!!!")

def power(num1, num2):
    print("Result:  ", num1 ** num2)


while True:
    num1 = float(input("Enter first number:  "))
    num2 = float(input("Enter second number:  "))
    op = input("Enter operator (+, -, *, /, %, **):  ")

    if op == "+":
        addition(num1, num2)
    elif op == "-":
        subtraction(num1, num2)
    elif op == "*":
        multiplication(num1, num2)
    elif op == "/":
        division(num1, num2)
    elif op == "%":
        modulus(num1, num2)
    elif op == "**":
        power(num1, num2)
    else:
        print("Invalid Operator....")

    command = input("\nDo you want to continue? (yes / no):  ").lower()
    if command == "no":
        print("Calculator Closed!!!")
        break

