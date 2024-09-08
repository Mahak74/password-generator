import random
import string

# Function to generate password
def generate_password(length):
    # Define the character set: letters, digits, and punctuation
    characters = string.ascii_letters + string.digits + string.punctuation

    # Randomly select characters from the character set to form a password
    password = ''.join(random.choice(characters) for i in range(length))

    return password

# Main program
try:
    # Input from the user: Desired password length
    length = int(input("Enter the desired length for the password: "))

    if length < 4:
        print("Password length should be at least 4 for better security.")
    else:
        # Generate and display the password
        password = generate_password(length)
        print(f"Generated Password: {password}")

except ValueError:
    print("Error: Please enter a valid number for the password length.")
