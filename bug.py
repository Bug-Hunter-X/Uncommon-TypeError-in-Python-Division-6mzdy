def function_with_uncommon_error(a, b):
    try:
        result = a / b
    except TypeError:
        print("TypeError: Unsupported operand type(s) for /: 'str' and 'int'")
        return None
    except ZeroDivisionError:
        print("ZeroDivisionError: division by zero")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None
    return result