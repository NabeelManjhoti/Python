import random

def rock_paper_scissors():
    print('\nDeveloped by: Nabeel Ali\n')
    print("Welcome to Rock, Paper, Scissors! Let's play!")

    choices = {'r': 'rock', 'p': 'paper', 's': 'scissors'}

    while True:
        print('')
        user_input = input(
            "Enter rock (R), paper (P), or scissors (S) (or 'quit' to exit): ").lower()

        if user_input == 'quit':
            print('\nThanks for playing!')
            break

        if user_input not in choices:
            print('\nInvalid choice. Please try again.')
            continue

        user_choice = choices[user_input]
        computer_choice = random.choice(list(choices.values()))

        print(f"\nThe computer chose: {computer_choice}")

        if user_choice == computer_choice:
            print(f"\nBoth players selected {user_choice}. It's a tie!")
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "paper" and computer_choice == "rock") or \
             (user_choice == "scissors" and computer_choice == "paper"):
            print(f"\n{user_choice.capitalize()} beats {computer_choice}! You win!")
        else:
            print(
                f"\n{computer_choice.capitalize()} beats {user_choice}! You lose!")

        print("\nLet's play again!")


if __name__ == '__main__':
    rock_paper_scissors()