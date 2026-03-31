
# Hello and welcome! This is a continued version of my old calculator. calculator_reworked! Made by 4zuj.
# At the start a friendly greeting, because why not right?

print("\nWelcome to the calculator!\n")

# Here is the code asking for the Numbers that should be used to calculate.

def addition(first_calculating_number, second_calculating_number):
    result = first_calculating_number + second_calculating_number
    return result

def subtraction(first_calculating_number, second_calculating_number):
    result = first_calculating_number - second_calculating_number
    return result

def multiplication(first_calculating_number, second_calculating_number):
    result = first_calculating_number * second_calculating_number
    return result

def division(first_calculating_number, second_calculating_number):
    result = first_calculating_number / second_calculating_number
    return result

while True:
    first_number = float(input("First Number to calculate?: "))
    second_number = float(input("Second Number to use for the other Number?: "))

    print("\nGreat! What Operator do you want to use to calculate? The available operators are : +, -, *, /") # Now the code is going to ask the user what Operator he wants to use.
    operator = input("> ")

    if operator == "+":
        result = addition(first_calculating_number = first_number, second_calculating_number = second_number)

    elif operator == "-":
        result = subtraction(first_calculating_number = first_number, second_calculating_number = second_number)
        
    elif operator == "*":
        result = multiplication(first_calculating_number = first_number, second_calculating_number = second_number)

    elif operator == "/":
        result = division(first_calculating_number = first_number, second_calculating_number = second_number)

    print(f"Your result is:\n> {result}\n")
