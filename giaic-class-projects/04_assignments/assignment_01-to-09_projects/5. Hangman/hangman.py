import random
words = ["python", "hangman", "programming", "developer", "challenge"]
import string


def get_valid_word(words):
    word = random.choice(words)  # randomly chooses
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()


def hangman():
    word = get_valid_word(words)
    word_letters = set(word)  # letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    lives = 6

    while len(word_letters) > 0 and lives > 0:
        print('\nDeveloped by: Nabeel Ali\n')
        print('You have', lives, 'lives left and you have used these letters: ',
              ' '.join(used_letters))

        word_list = [
            letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))

        user_letter = input('\nEnter a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)

            else:
                lives = lives - 1
                print(f'\nLetter {user_letter} is not in word.')

        elif user_letter in used_letters:
            print('\nYou have already used that character. Please try again.')
        else:
            print('\nInvalid character. Please try again.')

    if lives == 0:
        print(f'\nYou died, sorry. The word was {word}')
    else:
        print(
            f'\nCongratulations! You have guessed the word {word} correctly!')


hangman()

while input('\nDo you want to play again? (Y/N): ').upper() == 'Y':
    hangman()