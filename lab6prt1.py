import re

def find_phone_number(text):
    # Define a regular expression pattern for valid phone numbers
    phone_pattern = r'\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}'

    # Search for the pattern in the input text
    match = re.search(phone_pattern, text)

    if match:
        return match.group()
    else:
        return None

# Get user input
input_text = input("Enter a text to search for a valid phone number: ")

phone_number = find_phone_number(input_text)

if phone_number:
    print("Valid phone number found:", phone_number)
else:
    print("No valid phone number found.")
