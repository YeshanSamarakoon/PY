def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero is not allowed."
    else:
        return x / y

print("Welcome to the Calculator!")
print("Operations: +, -, *, /")

while True:
    operation = input("Enter an operation (+, -, *, /) or 'q' to quit: ")
    if operation == 'q':
        break

    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    if operation == '+':
        result = add(num1, num2)
        print(f"{num1} + {num2} = {result}")
    elif operation == '-':
        result = subtract(num1, num2)
        print(f"{num1} - {num2} = {result}")
    elif operation == '*':
        result = multiply(num1, num2)
        print(f"{num1} * {num2} = {result}")
    elif operation == '/':
        result = divide(num1, num2)
        print(f"{num1} / {num2} = {result}")
    else:
        print("Invalid operation. Please try again.")

print("Thank you for using the calculator!")