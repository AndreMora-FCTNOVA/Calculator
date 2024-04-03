import math


def add(x, y):
    """Function to add two numbers"""

    return x + y

def myPow(x,y):
    return math.pow(x,y)

def inverse(x):
    """Function to do the inverse"""
    return 1/x



def mySqrt(x):
    """Function to square root"""
    return math.sqrt(x)
def divide(x,y):
    """Function to divide two numbers"""
    return x / y


def modulo(x):
    """Function to get absolute value of x"""
    return abs(x)

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
print("3. Division")
print("4. Modulo")
print("7. Factorial")
print("8. Inverse")
print("9. Pow")


while True:
    choice = input("Enter choice (1- ADD MORE ): ")

    if choice in ('1','9'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '9':
            print("Result:", myPow(num1, num2))
        if choice == '1':
            print("Result:", add(num1, num2))

        break
    elif choice in ('2','8'):
        num1 = float(input("Enter the number: "))

        if choice == '2':
            print("Result:", mySqrt(num1))
        elif choice == '8':
            print("Result:", inverse(num1))


    elif choice in ('4'):
            num1 = float(input("Enter first number: "))

            if choice == '4':
                print("Result:", modulo(num1))


    elif choice in ('3'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '3':
            print("Result:", divide(num1, num2))

    elif choice in ('7'):
        num1 = float(input("Enter the number: "))

        if choice == '7':
            print(("Result:", factorial(int(num1))))

    else:
        print("Invalid input. Please enter a valid number (1/2/3/4).")
