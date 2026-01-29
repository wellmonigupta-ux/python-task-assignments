# Taking two numbers as input from the user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Performing operations 
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2

# Handling division safely
if num2 != 0:
    division = num1 / num2
else:
    division = "Cannot divide by zero"

# Displaying results
print("Addition:", addition)
print("Subtraction:", subtraction)
print("Multiplication:", multiplication)
print("Division:", division)
