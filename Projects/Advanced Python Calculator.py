import math

def add(x, y):
    return x + y
def subtract(x, y):
    return x - y 
def multiply(x, y):
    return x * y
def divide(x, y):
    if y == 0:
        return "Cannot divide by zero"
    return x / y
def square_root(x):
    if x < 0:
        return "Cannot calculate the square root of a negative number"
    return math.sqrt(x)
def exponentiate(x, y):
    return x**y
while True:
    print("Options:")
    print("Enter 'add' for addition")
    print("Enter 'subtract' for subtraction")
    print("Enter 'multiply' for multiplication")
    print("Enter 'divide' for division")
    print("Enter 'sqrt' for square root")
    print("Enter 'exp' for exponentiation")
    print("Enter 'quit' to end the program")
    
    user_input = input(": ")
    
    if user_input == "quit":
        break
    elif user_input in ("add", "subtract", "multiply", "divide", "exp"):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        if user_input == "add":
            print("Result: ", add(num1, num2))
        elif user_input == "subtract":
            print("Result: ", subtract(num1, num2))
        elif user_input == "multiply":
            print("Result: ", multiply(num1, num2))
        elif user_input == "divide":
            print("Result: ", divide(num1, num2))
        elif user_input == "exp":
            print("Result: ", exponentiate(num1, num2))
    elif user_input == "sqrt":
        num = float(input("Enter a number: "))
        print("Result: ", square_root(num))
    else:
        print("Invalid input")
