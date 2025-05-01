import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

def password_generator():
    try:
        num_passwords = int(
            input("\nEnter the number of passwords to generate: "))
        password_length = int(input("Enter the length of each password: "))

        if num_passwords <= 0 or password_length <= 0:
            print("Please enter valid positive numbers.")
            return

        print("\nGenerated Passwords:")
        for i in range(num_passwords):
            print(f'{i+1}: {generate_password(password_length)}')

    except ValueError:
        print("Invalid input! Please enter a valid number.")

if __name__ == "__main__":
    password_generator()