def function_with_uncommon_error(a, b):
    try:
        if isinstance(a, str) or isinstance(b, str):
            raise TypeError("Operands must be numbers")
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        result = a / b
        return result
    except TypeError as e:
        print(f"TypeError: {e}")
        return None
    except ZeroDivisionError as e:
        print(f"ZeroDivisionError: {e}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None