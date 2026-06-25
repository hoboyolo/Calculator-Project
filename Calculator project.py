
operations = {
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
    "*": lambda a, b: a * b,
    "/": lambda a, b: a / b,
    "%": lambda a, b: a % b,
    "**": lambda a, b: a ** b,
}


def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")


def calculate(operator, num1, num2):
    if operator not in operations:
        raise ValueError(f"{operator} is not a valid operator.")
    return operations[operator](num1, num2)


def main():
    print("Simple calculator. Type 'q' to quit.")
    while True:
        operator = input("Enter operator (+, -, *, /, %, **) or 'q' to quit: ").strip()
        if operator.lower() == "q":
            print("Goodbye!")
            break

        if operator not in operations:
            print("Invalid operator! Try again.")
            continue

        num1 = get_number("Enter the first number: ")
        num2 = get_number("Enter the second number: ")

        try:
            result = calculate(operator, num1, num2)
        except ZeroDivisionError:
            print("Error: division by zero is not allowed.")
            continue
        except ValueError as error:
            print(f"Error: {error}")
            continue

        print(f"Result: {round(result, 3)}")


if __name__ == "__main__":
    main()

