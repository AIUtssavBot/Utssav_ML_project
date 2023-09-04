import secrets
import string

def generate_password(length=12, use_uppercase=True, use_digits=True, use_special_chars=True):
    # Define character sets
    lowercase_chars = string.ascii_lowercase
    uppercase_chars = string.ascii_uppercase if use_uppercase else ''
    digit_chars = string.digits if use_digits else ''
    special_chars = '!@#$%^&*()_+-=[]{}|;:,.<>?/' if use_special_chars else ''

    # Combine character sets based on user preferences
    all_chars = lowercase_chars + uppercase_chars + digit_chars + special_chars

    if len(all_chars) == 0:
        print("Error: Password cannot be generated with no character set.")
        return None

    # Check if the password length is valid
    if length < 1:
        print("Error: Password length must be at least 1.")
        return None

    # Use secrets module for secure random selection
    password = ''.join(secrets.choice(all_chars) for _ in range(length))

    return password

if __name__ == "__main__":
    # User-defined settings
    length = int(input("Enter the desired password length: "))
    use_uppercase = input("Include uppercase letters? (yes/no): ").lower() == 'yes'
    use_digits = input("Include digits? (yes/no): ").lower() == 'yes'
    use_special_chars = input("Include special characters? (yes/no): ").lower() == 'yes'

    # Generate the password
    password = generate_password(length, use_uppercase, use_digits, use_special_chars)

    if password:
        print(f"Generated Password: {password}")
    else:
        print("Password generation failed.")
