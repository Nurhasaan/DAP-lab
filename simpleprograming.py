import math

# 1. Program to add two numbers
def add_two_numbers():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    sum = num1 + num2
    print(f"The sum of {num1} and {num2} is {sum}")

# 2. Maximum of two numbers in Python
def max_of_two_numbers():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    maximum = max(num1, num2)
    print(f"The maximum of {num1} and {num2} is {maximum}")

# 3. Python Program for factorial of a number
def factorial():
    def calculate_factorial(n):
        if n == 0 or n == 1:
            return 1
        else:
            return n * calculate_factorial(n-1)

    num = int(input("Enter a number: "))
    print(f"The factorial of {num} is {calculate_factorial(num)}")

# 4. Python Program for simple interest
def simple_interest():
    def calculate_simple_interest(principal, rate, time):
        return (principal * rate * time) / 100

    principal = float(input("Enter principal amount: "))
    rate = float(input("Enter rate of interest: "))
    time = float(input("Enter time (in years): "))
    simple_interest = calculate_simple_interest(principal, rate, time)
    print(f"The simple interest is {simple_interest}")

# 5. Python Program for compound interest
def compound_interest():
    def calculate_compound_interest(principal, rate, time):
        return principal * (1 + rate / 100)**time - principal

    principal = float(input("Enter principal amount: "))
    rate = float(input("Enter rate of interest: "))
    time = float(input("Enter time (in years): "))
    compound_interest = calculate_compound_interest(principal, rate, time)
    print(f"The compound interest is {compound_interest}")

# 6. Python Program to check Armstrong Number
def armstrong_number():
    def is_armstrong_number(num):
        order = len(str(num))
        sum = 0
        temp = num
        while temp > 0:
            digit = temp % 10
            sum += digit ** order
            temp //= 10
        return num == sum

    number = int(input("Enter a number: "))
    if is_armstrong_number(number):
        print(f"{number} is an Armstrong number")
    else:
        print(f"{number} is not an Armstrong number")

# 7. Python Program for Program to find the area of a circle
def area_of_circle():
    radius = float(input("Enter the radius of the circle: "))
    area = math.pi * (radius ** 2)
    print(f"The area of the circle with radius {radius} is {area}")

# Call the functions
add_two_numbers()
max_of_two_numbers()
factorial()
simple_interest()
compound_interest()
armstrong_number()
area_of_circle()
