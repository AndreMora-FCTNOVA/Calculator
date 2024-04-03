import math


def add(x, y):
    """Function to add two numbers"""
    return x + y


def mySqrt(x):
    """Function to square root"""
    return math.sqrt(x)


def factorial(x):
    result = x
    for i in range(x-1):
        print(result)
        print(i+1)
        result = result * (i+1)
    return result


print("Select operation:")
print("1. Add")
print("2. Sqrt")

while True:
    choice = input("Enter choice (1- ADD MORE ): ")

    if choice in ('1'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print("Result:", add(num1, num2))

        break
    elif choice in ('2'):
        num1 = float(input("Enter the number: "))

        if choice == '2':
            print("Result:", mySqrt(num1))

    elif choice in ('7'):
        num1 = float(input("Enter the number: "))

        if choice == '7':
            print(("Result:", factorial(int(num1))))

    else:
        print("Invalid input. Please enter a valid number (1/2/3/4).")
