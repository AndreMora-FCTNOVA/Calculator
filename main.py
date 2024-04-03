import math


def add(x, y):
    """Function to add two numbers"""
    return x + y


def inverse(x):
    """Function to do the inverse"""
    return 1/x



def mySqrt(x):
    """Function to square root"""
    return math.sqrt(x)




print("Select operation:")
print("1. Add")
print("2. Sqrt")
print("8. Inverse")




while True:
    choice = input("Enter choice (1- ADD MORE ): ")

    if choice in ('1'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print("Result:", add(num1, num2))

        break
    elif choice in ('2','8'):
        num1 = float(input("Enter the number: "))

        if choice == '2':
            print("Result:", mySqrt(num1))
        elif choice == '8':
            print("Result:", inverse(num1))


    else:
        print("Invalid input. Please enter a valid number (1/2/3/4).")