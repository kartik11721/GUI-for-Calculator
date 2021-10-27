def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

while True:
    # take input from the user
    operation = input("Enter The Operation (+,-,*,/): ")

    if operation in ('+', '-', '*', '/'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if operation == '+':
            print(f"{num1} + {num2} = {num1 + num2}")

        elif operation == '-':
            print(f"{num1} - {num2} = {num1 - num2}")

        elif operation == '*':
            print(f"{num1} * {num2} = {num1 * num2}")

        elif operation == '/':
            print(f"{num1} / {num2} = {num1 / num2}")
        break
    
    else:
        print("Please Enter A Valid Input")