try:
    dividend = int(input("Enter a dividend: "))
    divisor = int(input("Enter a divisor: "))
    result = dividend / divisor
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except ValueError:
    print("Error: Please enter valid numbers.")
finally:
    print("Execution completed.")

# You can raise a custom exception if needed
if divisor == 0:
    raise Exception("Divisor cannot be zero.")
