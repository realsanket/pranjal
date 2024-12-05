def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def find_even(numbers):
    return [num for num in numbers if num % 2 == 0]

def find_odd(numbers):
    return [num for num in numbers if num % 2 != 0]

import random

def main():
    a = random.randint(1, 100)
    b = random.randint(1, 100)
    numbers = [random.randint(1, 100) for _ in range(10)]

    print(f"Random numbers: {a}, {b}")
    print(f"Addition: {add(a, b)}")
    print(f"Subtraction: {subtract(a, b)}")
    print(f"Multiplication: {multiply(a, b)}")
    print(f"Division: {divide(a, b)}")
    print(f"Even numbers: {find_even(numbers)}")
    print(f"Odd numbers: {find_odd(numbers)}")

if __name__ == "__main__":
    main()
