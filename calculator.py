import re

def calculate(expression):
    try:
        result = eval(expression)
        return result
    except Exception as e:
        raise ValueError(f"Error in expression: {expression}. {e}")

def validate_expression(expression):
    pattern = re.compile(r'^[0-9+\-*/(). ]+$')
    if not pattern.match(expression):
        raise ValueError("Invalid characters in expression.")

def main():
    try:
        expression = input("Enter arithmetic expression: ")
        validate_expression(expression)
        result = calculate(expression)
        print(f"Result: {result}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()

