import random
import string

def generate_password(length):
    # Define the characters to choose from: letters (upper and lowercase), digits, and punctuation
    characters = string.ascii_letters + string.digits + "!@#$%^&*()_-+=<>?{}[]"
    
    # Generate a random password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    try:
        # Prompt the user for the desired length of the password
        length = int(input("Enter the desired length of the password: "))
        if length < 1:
            print("Password length must be at least 1.")
            return

        # Generate the password
        password = generate_password(length)

        # Display the generated password
        print(f"Generated Password: {password}")
    except ValueError:
        print("Please enter a valid number.")

if __name__ == "__main__":
    main()
