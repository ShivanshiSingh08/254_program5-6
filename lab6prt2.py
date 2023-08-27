import re

def is_strong_password(password):
    # Define a regular expression pattern for a strong password
    password_pattern = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@#$%^&+=!]).{8,}$'

    # Check if the password matches the pattern
    if re.match(password_pattern, password):
        return True
    else:
        return False

# Get user input
password = input("Enter a password to check if it's strong: ")

if is_strong_password(password):
    print("The password is strong.")
else:
    print("The password is not strong. It should have at least 8 characters, one uppercase letter, one lowercase letter, one digit, and one special character.")
