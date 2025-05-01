import random

def guess_the_number():
    print('')
    print('Developed by: Nabeel Ali')
    print('')
    print("Welcome to 'Guess the Number'! Try to guess the number I'm thinking of.\n")
    secret_number = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            guess = int(input("Enter your guess (between 1 and 100): "))
            attempts += 1

            if guess < 1 or guess > 100:
                print("Please enter a number within the valid range.")
            elif guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print('')
                print(
                    f"Congratulations! You guessed the number {secret_number} correctly in {attempts} attempts.")
                break
        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    guess_the_number()