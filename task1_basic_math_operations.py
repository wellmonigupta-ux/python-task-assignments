# Task 1: Basic Mathematical Operations
# This program takes two numbers and performs basic arithmetic operations

# Get two numbers from the user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Perform arithmetic operations
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2 if num2 != 0 else "Cannot divide by zero"

# Display results
print("\n--- Results ---")
print(f"Addition: {num1} + {num2} = {addition}")
print(f"Subtraction: {num1} - {num2} = {subtraction}")
print(f"Multiplication: {num1} * {num2} = {multiplication}")

if isinstance(division, str):
    print(f"Division: {division}")
else:
    print(f"Division: {num1} / {num2} = {division}")
