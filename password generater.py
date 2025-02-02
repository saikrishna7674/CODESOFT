import random
import string

# Function to generate a strong password
def generate_password(length):
    if length < 4:
        print("Password length should be at least 4 characters.")
        return None
    
    # Define character sets
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    # Ensure password includes at least one character from each set
    all_chars = lower + upper + digits + symbols
    password = random.choice(lower) + random.choice(upper) + random.choice(digits) + random.choice(symbols)

    # Generate remaining characters randomly
    password += ''.join(random.choice(all_chars) for _ in range(length - 4))

    # Shuffle the password to make it more random
    password = ''.join(random.sample(password, len(password)))

    return password

# Get user input for password length
try:
    length = int(input("Enter password length: "))
    password = generate_password(length)
    
    if password:
        print(f"Generated Password: {password}")
except ValueError:
    print("Please enter a valid number!")
