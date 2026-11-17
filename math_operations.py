def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b


def get_user_input():
    """Read two numbers and an arithmetic operator from the user."""
    try:
        a = float(input("Enter the first number: "))
        b = float(input("Enter the second number: "))
    except ValueError as e:
        print(f"Invalid input. Please enter numeric values: {e}")
        return None, None, None

    operation = input("Enter the operation (+, -, *, /): ")
    return a, b, operation


def main():
    """Get user input and perform the selected arithmetic operation."""
    a, b, operation = get_user_input()
    if a is None or b is None:
        print("Failed to process input.")
        return

    operations = {
        "+": add,
        "-": subtract,
        "*": multiply,
        "/": divide,
    }
    if operation not in operations:
        print("Unknown operation.")
        return

    try:
        print(f"The result is {operations[operation](a, b)}")
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()
